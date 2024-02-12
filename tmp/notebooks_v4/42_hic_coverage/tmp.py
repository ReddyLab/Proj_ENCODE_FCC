### stream hic file
hic = hicstraw.HiCFile(args.fpath_hic)
assert args.resolution in hic.getResolutions(), f"Hi-C data does not have the resolution specified;\nexpect: {hic.getResolutions()};\ngot{args.resolution}"

### extract hic matrix
mat_object = hic.getMatrixZoomData(
    args.chrom, 
    args.chrom, 
    "observed", 
    args.normalization, 
    "BP", 
    args.resolution)

mat_numpy = mat_object.getRecordsAsMatrix(
    args.x1,
    args.y1,
    args.x2,
    args.y2
)

### create vectors from hic matrix and combine them into a dataframe
vec_track = np.sum(mat_numpy, axis=1)
vec_chrom = np.repeat(args.chrom, len(vec_track))
vec_start = np.arange(args.x1, args.y1 + args.resolution, args.resolution)
vec_end   = vec_start + args.resolution

dat_track = pd.DataFrame(
    list(zip(
        vec_chrom, 
        vec_start, 
        vec_end, 
        vec_track)),
    columns =['Chrom', 'Start', 'End', 'Score']
)

### save the results
dat_track.to_csv(args.fpath_out, sep="\t", header=False, index=False)