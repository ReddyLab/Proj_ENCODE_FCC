### set environment
import numpy as np
import pandas as pd
import argparse
import os

import igraph as ig
import phenograph

### get parameters
parser = argparse.ArgumentParser()
parser.add_argument("finp",        type=str, help="input file")
parser.add_argument("fout_prefix", type=str, help="output file prefix")
parser.add_argument("n_neighbors", type=int, help="number of neighbors for phenograph")
args = parser.parse_args()

NUM_SEED       = 123
NUM_NEIGHBORS  = args.n_neighbors
TXT_FPATH_INP  = args.finp
TXT_FPATH_OUT_PREFIX = args.fout_prefix

### show env
print(f"Input  File: {TXT_FPATH_INP}")
print(f"Output File Prefix: {TXT_FPATH_OUT_PREFIX}")
print(f"k (neighbors): {NUM_NEIGHBORS}")
print()

### import data
mat = pd.read_csv(TXT_FPATH_INP, sep="\t")
vec = mat.Region
mat = mat.set_index("Region")

### execute PhenoGraph
communities, graph, Q = phenograph.cluster(mat, k=NUM_NEIGHBORS, seed=NUM_SEED)

### save cluster assignment
dat_cluster = pd.DataFrame({
    "Region": vec,
    f"Cluster_k{NUM_NEIGHBORS}": communities
})
txt_fpath_out = f"{TXT_FPATH_OUT_PREFIX}.cluster.tsv"
dat_cluster.to_csv(txt_fpath_out, sep="\t", index=False)

### build igraph
sources, targets = graph.nonzero()
g = ig.Graph(list(zip(sources, targets)), directed=False)
g.es["weight"] = graph.data.tolist()

### compute graph/cluster stats
sizes = pd.Series(communities).value_counts().sort_index()
deg   = g.degree()
summary = {
    "k": NUM_NEIGHBORS,
    "Q": Q,
    "n_clusters": sizes.shape[0],
    "smallest_cluster": sizes.min(),
    "largest_cluster":  sizes.max(),
    "mean_degree": np.mean(deg),
    "min_degree":  np.min(deg),
    "max_degree":  np.max(deg),
    "mean_edge_weight": np.mean(g.es["weight"]),
    "min_edge_weight":  np.min(g.es["weight"]),
    "max_edge_weight":  np.max(g.es["weight"]),
}

### write summary to file
txt_fpath_out = f"{TXT_FPATH_OUT_PREFIX}.summary.tsv"
pd.DataFrame([summary]).to_csv(txt_fpath_out, sep="\t", index=False)

### save graph in GraphML format for later inspection
txt_fpath_out = f"{TXT_FPATH_OUT_PREFIX}.graph.graphml"
g.write_graphml(txt_fpath_out)
