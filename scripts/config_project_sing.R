### import library: basic
library("tidyverse")
library("vroom")
library("pryr")

### import library: visualization
library("RColorBrewer")
library("cowplot")
library("gridExtra")
library("grid")

### workspace info
PROJECT = "ENCODE FCC"
SERVER  = "Singularity: singularity_proj_encode_fcc"
#SERVER = "Duke Server: DCC"
#SERVER = "Duke Server: HARDAC"

### set workspace info
SERVER="Singularity"
PROJECT="ENCODE FCC"

### main paths
FD_BASE="/mount"
FD_WORK="/mount/work"
FD_REPO="/mount/repo"
FD_DATA="/mount/data"
FD_RLAB="/mount/reddylab"

### set project related paths
FD_PRJ = file.path(FD_REPO, "Proj_ENCODE_FCC")

FD_RES = file.path(FD_PRJ,  "results")
FD_EXE = file.path(FD_PRJ,  "scripts")
FD_DAT = file.path(FD_PRJ,  "data")
FD_NBK = file.path(FD_PRJ,  "notebooks")
FD_DOC = file.path(FD_PRJ,  "docs")
FD_LOG = file.path(FD_PRJ,  "log")
FD_APP = file.path(FD_PRJ,  "app")
FD_REF = file.path(FD_PRJ,  "references")

### helper function to print out the path info
show_env = function(){
    cat("You are working on       ", SERVER,  "\n")
    cat("BASE DIRECTORY (FD_BASE):", FD_BASE, "\n") 
    cat("REPO DIRECTORY (FD_REPO):", FD_REPO, "\n")
    cat("WORK DIRECTORY (FD_WORK):", FD_WORK, "\n")
    cat("DATA DIRECTORY (FD_DATA):", FD_DATA, "\n")
    cat("\n")
    
    cat("You are working with     ", PROJECT, "\n") 
    cat("PATH OF PROJECT (FD_PRJ):", FD_PRJ,  "\n") 
    cat("PROJECT RESULTS (FD_RES):", FD_RES,  "\n") 
    cat("PROJECT SCRIPTS (FD_EXE):", FD_EXE,  "\n") 
    cat("PROJECT DATA    (FD_DAT):", FD_DAT,  "\n") 
    cat("PROJECT NOTE    (FD_NBK):", FD_NBK,  "\n") 
    cat("PROJECT DOCS    (FD_DOC):", FD_DOC,  "\n") 
    cat("PROJECT LOG     (FD_LOG):", FD_LOG,  "\n") 
    cat("PROJECT APP     (FD_APP):", FD_APP,  "\n") 
    cat("PROJECT REF     (FD_REF):", FD_REF,  "\n") 
    cat("\n")
}

### helper function to show table
fun_display_table = function(dat){
    dat %>%
        kableExtra::kable("html") %>%
        as.character() %>%
        IRdisplay::display_html()
}

### helper function to get genome location
fun_gen_region = function(txt_chrom, num_chrom_start, num_chrom_end){
    txt_chrom_start = format(num_chrom_start, scientific = FALSE)
    txt_chrom_end   = format(num_chrom_end,   scientific = FALSE)
    txt_region      = paste0(txt_chrom, ":", txt_chrom_start, "-", txt_chrom_end)
    txt_region      = stringr::str_remove_all(txt_region, " ")
    return(txt_region)
}

### helper function to detect and map string
### Reference:
###     [A general vectorised if-else](https://dplyr.tidyverse.org/reference/case_when.html)
###     [Display text with Quotes](https://stackoverflow.com/questions/15204442/how-to-display-text-with-quotes-in-r)
###     [Recoding using str_detect](https://forum.posit.co/t/recoding-using-str-detect/5141)
###     [Build two sided formulas](https://stackoverflow.com/questions/78042986/how-to-build-a-sequence-of-two-sided-formulas-from-vectors)
fun_str_map_detect = function(
    vec_txt_input,
    vec_txt_pattern,
    vec_txt_replace,
    ...
){
    ### define inner function to generate formula with str_detect
    fun_match = function(x, y){
        txt = paste0(
            "stringr::str_detect(vec_txt_input,", 
            "'", x, "'", 
            ")~", 
            "'", y, "'"
        )
        return(as.formula(txt))
    }

    ### create a seqeunce of str_detect formulae
    lst_match = purrr::map2(vec_txt_pattern, vec_txt_replace, fun_match)

    ### map strings with str_detect
    vec_txt_output = dplyr::case_when(!!!lst_match, ...)
    return(vec_txt_output)
}

### helper function to match and map string
### Reference:
###     [A general vectorised switch](https://dplyr.tidyverse.org/reference/case_match.html)
###     [Display text with Quotes](https://stackoverflow.com/questions/15204442/how-to-display-text-with-quotes-in-r)
###     [Recoding using str_detect](https://forum.posit.co/t/recoding-using-str-detect/5141)
###     [Build two sided formulas](https://stackoverflow.com/questions/78042986/how-to-build-a-sequence-of-two-sided-formulas-from-vectors)
fun_str_map_match = function(
    vec_txt_input,
    vec_txt_pattern,
    vec_txt_replace,
    ...
){
    ### create a seqeunce of str_detect formulae
    lst_match = purrr::map2(vec_txt_pattern, vec_txt_replace, rlang::new_formula)
    
    ### map strings with str_detect
    vec_txt_output = dplyr::case_match(vec_txt_input, !!!lst_match, ...)
    return(vec_txt_output)
}
