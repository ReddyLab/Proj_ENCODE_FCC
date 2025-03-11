### set environment
import numpy as np
import pandas as pd
import argparse
import os

import umap

### get parameters
parser = argparse.ArgumentParser()
parser.add_argument("finp",        type = str, help = "input file")
parser.add_argument("fout",        type = str, help = "output file")
parser.add_argument("metric",      type = str, help = "metric for distance calculation")
parser.add_argument("n_neighbors", type = int, help = "numbers of neighbor points for UMAP")

### set global variables
args = parser.parse_args()

NUM_SEED      = 123
NUM_NEIGHBORS = args.n_neighbors
TXT_FPATH_INP = args.finp
TXT_FPATH_OUT = args.fout
TXT_METRIC    = args.metric

### show env
print(f"Input  File:")
print(f"{TXT_FPATH_INP}")
print()
print(f"Output File:")
print(f"{TXT_FPATH_OUT}")
print()

### import data
mat = pd.read_csv(TXT_FPATH_INP, sep="\t")
vec = mat.Region
mat = mat.set_index('Region')

### execute
fit = umap.UMAP(metric=TXT_METRIC, n_neighbors=NUM_NEIGHBORS, n_jobs=1, random_state=NUM_SEED)
mat = mat.to_numpy()
res = fit.fit_transform(mat)

### convert to dataframe
dat = pd.DataFrame(res, columns=["UMAP1", "UMAP2"])
dat = dat.assign(Region = vec)

### save the results
dat.to_csv(TXT_FPATH_OUT, sep="\t", index=False)