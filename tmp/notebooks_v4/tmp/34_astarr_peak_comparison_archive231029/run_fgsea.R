library(tidyverse)
library(fgsea)

### parse arguemnts
myargs = commandArgs(trailingOnly=TRUE)
FP_INP_SCORE = myargs[1]
FP_INP_ANNOT = myargs[2]
FP_OUT       = myargs[3]

### show
cat("\n")
cat("Input score:", FP_INP_SCORE, "\n\n")
cat("Input annot:", FP_INP_ANNOT, "\n\n")
cat("Output file:", FP_OUT,       "\n\n")
flush.console()

### import data
vec_score = readRDS(FP_INP_SCORE)
lst_annot = readRDS(FP_INP_ANNOT)

### run GSEA
cat("RUN GSEA: Start.\n")
set.seed(123)
fgseaRes = fgsea(
    pathways  = lst_annot, 
    stats     = vec_score,
    eps       = 0.0,
    scoreType = "pos"
)
cat("RUN GSEA: Done!\n\n")

### show results
cat("Show results:\n")
print(fgseaRes)
cat("\n")

### Save the results
cat("Save results.\n")
saveRDS(fgseaRes, FP_OUT)

