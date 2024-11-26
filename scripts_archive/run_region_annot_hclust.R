### set environment
suppressMessages(suppressWarnings(library("tidyverse")))
args = commandArgs(TRUE)

### get variables
txt_fpath_inp = args[1]
txt_fdiry_inp = dirname( txt_fpath_inp)
txt_fname_inp = basename(txt_fpath_inp)

txt_fdiry_out     = txt_fdiry_inp
txt_fname_out_row = txt_fname_inp %>% 
    stringr::str_replace("matrix", "hclust.row") %>% 
    stringr::str_replace("tsv", "rds")
txt_fpath_out_row = file.path(txt_fdiry_out, txt_fname_out_row)

txt_fdiry_out     = txt_fdiry_inp
txt_fname_out_col = txt_fname_inp %>% 
    stringr::str_replace("matrix", "hclust.col") %>% 
    stringr::str_replace("tsv", "rds")
txt_fpath_out_col = file.path(txt_fdiry_out, txt_fname_out_col)

### show progress
cat("Directory:  ", txt_fdiry_inp,     "\n")
cat("Input  File:", txt_fname_inp,     "\n")
cat("Output File:", txt_fname_out_row, "\n")
cat("Output File:", txt_fname_out_col, "\n")

### import data
txt = txt_fpath_inp
mat = readr::read_tsv(txt, show_col_types = FALSE)
mat = mat %>% tibble::column_to_rownames("Region")

mat_region_annot = mat

### cluster rows
mat = mat_region_annot
mat = dist(mat,  method = "manhattan")
res = fastcluster::hclust(mat, method = "ward.D2")

res_hcl_row = res

### cluster columns
mat = mat_region_annot
mat = t(mat)
mat = dist(mat,  method = "manhattan")
res = fastcluster::hclust(mat, method = "ward.D2")

res_hcl_col = res

### save results
saveRDS(res_hcl_row, txt_fpath_out_row)
saveRDS(res_hcl_col, txt_fpath_out_col)