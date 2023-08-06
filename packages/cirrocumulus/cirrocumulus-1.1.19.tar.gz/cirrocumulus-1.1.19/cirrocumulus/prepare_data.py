import argparse
import gzip
import logging
import os

import numpy as np
import pandas as pd
import scipy.sparse

from cirrocumulus.anndata_util import get_scanpy_marker_keys, datasets_schema, DataType
from cirrocumulus.io_util import get_markers, filter_markers, add_spatial, SPATIAL_HELP, unique_id
from cirrocumulus.util import to_json

logger = logging.getLogger("cirro")

cluster_fields = ['anno', 'cell_type', 'celltype', 'leiden', 'louvain', 'seurat_cluster', 'cluster']
categorical_fields_convert = ['seurat_clusters']


def read_adata(path, backed=False, spatial_directory=None, use_raw=False):
    import anndata
    adata = anndata.read_loom(path) if path.lower().endswith('.loom') else anndata.read(path,
                                                                                        backed=backed)
    if use_raw and adata.raw is not None and adata.shape[0] == adata.raw.shape[0]:
        logger.info('Using adata.raw')
        adata = anndata.AnnData(X=adata.raw.X, var=adata.raw.var, obs=adata.obs, obsm=adata.obsm, uns=adata.uns)

    if spatial_directory is not None:
        if not add_spatial(adata, spatial_directory):
            print('No spatial data found in {}'.format(spatial_directory))
    if not backed:
        if scipy.sparse.issparse(adata.X) and scipy.sparse.isspmatrix_csr(adata.X):
            adata.X = adata.X.tocsc()

    def fix_column_names(df):
        rename = {}
        for c in df.columns:
            if c.find(' ') != -1:
                rename[c] = c.replace(' ', '_')
        return df.rename(rename, axis=1) if len(rename) > 0 else df

    adata.obs = fix_column_names(adata.obs)
    adata.var = fix_column_names(adata.var)
    for field in categorical_fields_convert:
        if field in adata.obs and not pd.api.types.is_categorical_dtype(adata.obs[field]):
            logger.info('Converting {} to categorical'.format(field))
            adata.obs[field] = adata.obs[field].astype('category')
    for key in adata.obsm:
        if key.find(' ') != -1:
            new_key = key.replace(' ', '_')
            adata.obsm[new_key] = adata.obsm[key]
            del adata.obsm[key]
    return adata


def make_unique(index, join='-1'):
    index = index.str.replace('/', '_')
    lower_index = index.str.lower()
    if lower_index.is_unique:
        return index
    from collections import defaultdict

    indices_dup = lower_index.duplicated(keep="first")
    values_dup_lc = lower_index.values[indices_dup]
    values_dup = index.values[indices_dup]
    counter = defaultdict(lambda: 0)
    for i, v in enumerate(values_dup_lc):
        counter[v] += 1
        values_dup[i] += join + str(counter[v])
    values = index.values
    values[indices_dup] = values_dup
    index = pd.Index(values)
    return index


class PrepareData:

    def __init__(self, datasets, output, dimensions=None, groups=[], group_nfeatures=10, markers=[],
                 output_format='parquet'):
        self.datasets = datasets
        self.groups = groups
        self.group_nfeatures = group_nfeatures
        self.markers = markers
        self.output_format = output_format
        primary_dataset = datasets[0]
        for i in range(1, len(datasets)):
            dataset = datasets[i]
            name = dataset.uns['name']
            prefix = name + '-'
            dataset.var.index = prefix + dataset.var.index.astype(str)
            # add prefix, check for duplicates
            obs_exclude = []
            dataset.uns['cirro_obs_exclude'] = obs_exclude
            for key in list(dataset.obs.keys()):
                if key in primary_dataset.obs.columns and dataset.obs[key].equals(primary_dataset.obs[key]):
                    obs_exclude.append(key)
                    continue
                dataset.obs[prefix + key] = dataset.obs[key]
                del dataset.obs[key]

            obsm_exclude = []
            dataset.uns['cirro_obsm_exclude'] = obsm_exclude
            for key in list(dataset.obsm.keys()):
                if key in primary_dataset.obsm and np.array_equals(dataset.obsm[key], primary_dataset.obsm[key]):
                    obsm_exclude.append(key)
                    continue
                dataset.obsm[prefix + key] = dataset.obsm[key]
                del dataset.obsm[key]

        for dataset in datasets:
            if dataset.uns.get('name', '').lower().startswith('module'):  # TODO hack
                dataset.uns['data_type'] = DataType.MODULE
            index = make_unique(dataset.var.index.append(pd.Index(dataset.obs.columns)))
            dataset.var.index = index[0:len(dataset.var.index)]
            dataset.obs.columns = index[len(dataset.var.index):]

        self.base_output_dir = output
        dimensions_supplied = dimensions is not None and len(dimensions) > 0
        self.dimensions = [] if not dimensions_supplied else dimensions
        self.measures = []
        self.others = []
        for dataset in datasets:
            for i in range(len(dataset.obs.columns)):
                name = dataset.obs.columns[i]
                c = dataset.obs[name]
                if pd.api.types.is_object_dtype(c):
                    dataset.obs[name] = dataset.obs[name].astype('category')
                    c = dataset.obs[name]
                if not dimensions_supplied and pd.api.types.is_categorical_dtype(c):
                    if 1 < len(c.cat.categories) < 2000:
                        self.dimensions.append(name)
                        if c.isna().sum() > 0:
                            logger.info('Replacing nans in {}'.format(name))
                            dataset.obs[name] = dataset.obs[name].astype(str)
                            dataset.obs.loc[dataset.obs[name].isna(), name] = ''
                            dataset.obs[name] = dataset.obs[name].astype('category')
                    else:
                        self.others.append(name)
                elif not pd.api.types.is_string_dtype(c) and not pd.api.types.is_object_dtype(c):
                    self.measures.append('obs/' + name)
                else:
                    self.others.append(name)

    def get_path(self, path):
        return os.path.join(self.base_output_dir, path)

    def execute(self):
        output_format = self.output_format
        if not os.path.exists(self.base_output_dir):
            os.makedirs(self.base_output_dir, exist_ok=True)
        if self.groups is None:
            groups = []
            for dataset in self.datasets:
                existing_fields = set()
                scanpy_marker_keys = get_scanpy_marker_keys(dataset)
                for key in scanpy_marker_keys:
                    existing_fields.add(dataset.uns[key]['params']['groupby'])
                for field in dataset.obs.columns:
                    field_lc = field.lower()
                    for cluster_field in cluster_fields:
                        if field_lc.find(cluster_field) != -1 and cluster_field not in existing_fields:
                            groups.append(field)
                            break
            self.groups = groups
        if self.groups is not None and len(self.groups) > 0:
            use_pegasus = False
            use_scanpy = False
            try:
                import pegasus as pg
                use_pegasus = True
            except ModuleNotFoundError:
                pass
            if not use_pegasus:
                try:
                    import scanpy as sc
                    use_scanpy = True
                except ModuleNotFoundError:
                    pass
            if not use_pegasus and not use_scanpy:
                raise ValueError('Please install pegasuspy or scanpy to compute markers')
            for dataset in self.datasets:
                for group in self.groups:
                    field = group
                    if group not in dataset.obs:  # test if multiple comma separated fields
                        split_groups = group.split(',')
                        if len(split_groups) > 1:
                            use_split_groups = True
                            for split_group in split_groups:
                                if split_group not in dataset.obs:
                                    use_split_groups = False
                                    break
                            if use_split_groups:
                                dataset.obs[field] = dataset.obs[split_groups[0]].str.cat(dataset.obs[split_groups[1:]],
                                                                                          sep=',')

                    if field in dataset.obs:
                        if not pd.api.types.is_categorical_dtype(dataset.obs[field]):
                            dataset.obs[field] = dataset.obs[field].astype('category')
                        if len(dataset.obs[field].cat.categories) > 1:
                            print('Computing markers for {}'.format(field))
                            key_added = 'rank_genes_' + str(field)
                            if use_pegasus:
                                pg.de_analysis(dataset, cluster=field, de_key=key_added)
                            else:
                                sc.tl.rank_genes_groups(dataset, field, key_added=key_added, method='t-test')

        for i in range(1, len(self.datasets)):
            for key in dataset.uns.get('cirro_obs_exclude', []):
                del dataset.obs[key]
            for key in dataset.uns.get('cirro_obsm_exclude', []):
                del dataset.obsm[key]
        schema = self.get_schema()
        results = schema.get('results', [])
        if len(results) > 0:
            uns_dir = os.path.join(self.base_output_dir, 'uns')
            os.makedirs(uns_dir, exist_ok=True)
            for i in range(len(results)):  # keep id, name, type in schema, store rest in file
                result = results[i]
                result_id = result.pop('id')
                results[i] = dict(id=result_id, name=result.pop('name'), type=result.pop('type'),
                                  content_type='application/json', content_encoding='gzip')
                with gzip.open(os.path.join(uns_dir, result_id + '.json.gz'), 'wt') as f:
                    f.write(to_json(result))

        for dataset in self.datasets:
            images = dataset.uns.get('images')
            if images is not None:
                image_dir = os.path.join(self.base_output_dir, 'images')
                if not os.path.exists(image_dir):
                    os.mkdir(image_dir)
                for image in images:
                    path = image['image']
                    import shutil
                    shutil.copy(path, os.path.join(image_dir, os.path.basename(path)))
                    image['image'] = 'images/' + os.path.basename(path)

        if output_format == 'parquet':
            from cirrocumulus.parquet_io import save_adata_pq
            save_adata_pq(self.datasets, schema, self.base_output_dir)
        elif output_format == 'json':
            from cirrocumulus.json_io import save_adata_json
            save_adata_json(self.datasets, schema, self.base_output_dir)
        elif output_format == 'jsonl':
            from cirrocumulus.jsonl_io import save_adata_jsonl
            save_adata_jsonl(self.datasets, schema, self.base_output_dir)
        else:
            raise ValueError("Unknown format")

    def get_schema(self):
        result = datasets_schema(self.datasets)
        markers = result.get('markers', [])

        if self.markers is not None:  # add results specified from file
            markers += get_markers(self.markers)
            markers = filter_markers(self.datasets[0], markers)  # TODO check if markers are in union of all features

        for marker in markers:
            if marker.get('id') is None:
                marker['id'] = unique_id()
            marker['readonly'] = True
        result['markers'] = markers
        result['format'] = self.output_format
        return result


def main(argsv):
    parser = argparse.ArgumentParser(
        description='Prepare a dataset for cirrocumulus server.')
    parser.add_argument('dataset', help='Path to a h5ad, loom, or Seurat file', nargs='+')
    parser.add_argument('--out', help='Path to output directory')
    parser.add_argument('--backed', help='Load h5ad file in backed mode', action='store_true')
    parser.add_argument('--markers',
                        help='Path to JSON file of precomputed markers that maps name to features. For example {"a":["gene1", "gene2"], "b":["gene3"]',
                        action='append')
    parser.add_argument('--groups',
                        help='List of groups to compute markers for (e.g. louvain). Note that markers created with scanpy or cumulus are automatically included.',
                        action='append')
    parser.add_argument('--group_nfeatures', help='Number of marker genes/features to include', type=int, default=10)
    parser.add_argument('--spatial', help=SPATIAL_HELP)
    args = parser.parse_args(argsv)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    out = args.out

    input_datasets = args.dataset  # multimodal
    if len(input_datasets) == 0:
        raise ValueError('Please provide a dataset')
    output_format = 'parquet'  # args.output_format
    if out is None:
        out = os.path.splitext(os.path.basename(input_datasets[0]))[0]
    if out.endswith('/'):
        out = out[:len(out) - 1]
    if not out.endswith('.cpq'):
        out += '.cpq'

    datasets = []
    tmp_files = []
    for input_dataset in input_datasets:
        use_raw = False
        if input_dataset.lower().endswith('.rds'):
            import subprocess
            import tempfile
            import pkg_resources

            _, h5_file = tempfile.mkstemp(suffix='.h5ad')
            os.remove(h5_file)
            subprocess.check_call(
                ['Rscript', pkg_resources.resource_filename("cirrocumulus", 'seurat2h5ad.R'), input_dataset, h5_file])
            input_dataset = h5_file
            tmp_file = h5_file
            use_raw = True
            tmp_files.append(tmp_file)

        adata = read_adata(input_dataset, backed=args.backed, spatial_directory=args.spatial, use_raw=use_raw)
        datasets.append(adata)
        adata.uns['name'] = os.path.splitext(os.path.basename(input_dataset))[0]
    prepare_data = PrepareData(datasets=datasets, output=out, dimensions=args.groups, groups=args.groups,
                               group_nfeatures=args.group_nfeatures,
                               markers=args.markers, output_format=output_format)
    prepare_data.execute()
    for tmp_file in tmp_files:
        os.remove(tmp_file)


if __name__ == '__main__':
    import sys

    main(sys.argv)
