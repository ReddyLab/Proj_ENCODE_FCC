### set environment
import numpy  as np
import pandas as pd
import argparse
import pickle
import os

import hdbscan

### get parameters
parser = argparse.ArgumentParser()
parser.add_argument("finp",             type = str, help = "input file")
parser.add_argument("fout",             type = str, help = "output file")
parser.add_argument("metric",           type = str, help = "metric for distance calculation")
parser.add_argument("min_cluster_size", type = str, help = "smallest size grouping to consider a cluster")

### set global variables
args = parser.parse_args()

NUM_SEED      = 123
TXT_FPATH_INP = args.finp
TXT_FPATH_OUT = args.fout
TXT_METRIC    = args.metric
NUM_MIN_CLUSTER_SIZE = int(float(args.min_cluster_size))

### show env
print(f"Input  File:")
print(f"{TXT_FPATH_INP}")
print()
print(f"Output File:")
print(f"{TXT_FPATH_OUT}")
print()
print(f"Metric:")
print(f"{TXT_METRIC}")
print()
print(f"Min Cluster Size:")
print(f"{NUM_MIN_CLUSTER_SIZE}")
print()

### import data
mat = pd.read_csv(TXT_FPATH_INP, sep="\t")
vec = mat.Region
mat = mat.set_index('Region')

### execute
fit = hdbscan.HDBSCAN(metric=TXT_METRIC, min_cluster_size=NUM_MIN_CLUSTER_SIZE, gen_min_span_tree=True)
fit = fit.fit(mat)

### save results
with open(TXT_FPATH_OUT, 'wb') as file:
    pickle.dump(fit, file)
