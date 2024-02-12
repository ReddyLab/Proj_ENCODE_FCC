### import libraries
suppressMessages(suppressWarnings(library("tidyverse")))

### parse arguments
args = commandArgs(TRUE)
REGION    = as.character(args[1])
COLUMN    = as.character(args[2])
NUM_PARTS = as.integer(  args[3])
IDX_PARTS = as.integer(  args[4])

### set path and global variables
FD_RES = "/data/reddylab/Kuei/out/proj_combeffect_encode_fcc"
FD_INP = file.path(FD_RES, "results", "comparison", "comparison_local")
FD_OUT = file.path(FD_RES, "results", "comparison", "comparison_local", "cor_size_200bp_step_50bp")
FN_OUT = paste(
    "cor",
    COLUMN,
    REGION,
    NUM_PARTS,
    IDX_PARTS, #stringr::str_pad(IDX_PARTS, 2, pad = "0"),
    "csv",
    sep=".")
FP_OUT = file.path(FD_OUT, FN_OUT)

### show script running info
cat("\nParse argument:\n")
cat("    Region:               ", REGION,    "\n")
cat("    Column:               ", COLUMN,    "\n")
cat("    Number of total parts:", NUM_PARTS, "\n")
cat("    Index  of this  parts:", IDX_PARTS, "\n")

### check if the output file exist or not
cat("\nCheck if output file exist: if yes, stop.\n")
cat("Output file:\n", FP_OUT, "\n")
if (file.exists(FP_OUT)) {
    cat("Output file exists. Stop the program.\n")
    stop("Please delete the output file before running this script.")
} else {
    cat("Output file not exists. Create the output file.\n")
    file.create(FP_OUT)
}
    
### import track and windows
cat("\nImport track data\n")
fname = paste("track", COLUMN, REGION, "tsv", sep=".")
fpath = file.path(FD_INP, fname)
dat_track = read_tsv(fpath)

cat("\nImport sliding windows\n")
fname = paste("window", "size_200bp", "step_50bp", REGION, "tsv", sep=".")
fpath = file.path(FD_INP, fname)
dat_window = read_tsv(fpath)

### split windows
cat("\nSplitting windows:\n")
dat = dat_window
idx = sort(1:nrow(dat) %% NUM_PARTS)
lst = split(dat, idx)
dat = lst[[IDX_PARTS]]

dat_window_sub = dat
cat("Split into",    length(lst), "parts\n")
cat("Current part:", IDX_PARTS,   "\n")
cat("Number of rows:", nrow(dat), "\n")
print(head(dat))


### Set output file header
cnames = data.frame(
    "Chrom", "Start", "End", "Loc", 
    "cor_astarr_wstarr", 
    "cor_astarr_tmpra",
    "cor_wstarr_tmpra")
write.table(
    cnames, file = FP_OUT, sep=",", 
    row.names = FALSE, 
    col.names = FALSE, 
    append    = TRUE,
    quote     = FALSE,)

### Calculate rolling correlation:
###     calculate spearman correlation for each window
cat("\nCalculate rolling correlation:\n")
for (idx in 1:nrow(dat_window_sub)) {
    
    ### show progress
    if (idx %% 100 == 0) {
        cat("Process line:", 
            stringr::str_pad(idx, 3, pad = " "), 
            "\n")
    }
    
    ### get each sliding window
    x_window = dat_window_sub[idx,] 
    x_chrom  = x_window[["Chrom"]]
    x_start  = x_window[["Start"]]
    x_end    = x_window[["End"]]
    x_loc    = x_window[["Loc"]]
    
    ### calculate the correlation
    dat = dat_track %>% dplyr::filter(Chrom == x_chrom, Start >= x_start, End <= x_end) %>% na.omit
    cor_astarr_wstarr = cor(dat$ASTARR, dat$WSTARR, method = "spearman") 
    cor_astarr_tmpra  = cor(dat$ASTARR, dat$TMPRA,  method = "spearman") 
    cor_wstarr_tmpra  = cor(dat$WSTARR, dat$TMPRA,  method = "spearman")
    
    ### concatenate the results
    res = data.frame(
        x_chrom, x_start, x_end, x_loc,
        cor_astarr_wstarr, 
        cor_astarr_tmpra, 
        cor_wstarr_tmpra)
    
    write.table(
        res, file = FP_OUT, sep=",", 
        row.names = FALSE, 
        col.names = FALSE, 
        append    = TRUE,
        quote     = FALSE,)
}