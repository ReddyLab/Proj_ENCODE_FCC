### ++++++++++++++++++++++++++++++++++++++++++++++++++++
### Set additional directories
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### fragments | region
FD_ALEX=/data/reddylab/Alex
FD_REGION=${FD_ALEX}/encode4_duke/ipynbs/jamborees/20211025_MPRA_STARR_Jamboree/data/gata1_myc/starrseq/fragments


### fragments | whole genome
FD_WGS_WSTARR=/data/reddylab/Alex/encode4_duke/data/starr_seq/fragments
FP_WGS_WSTARR=($(ls ${FD_WGS_WSTARR}/*.fragments.counts.txt.gz))

FD_WGS_ASTARR_INP=${FD_ALEX}/encode4_duke/processing/atac_seq/210401_KS91_K562ASTARR_NovaSeq.hg38-pe-blacklist-removal/merged2
FD_WGS_ASTARR_OUT=${FD_ALEX}/encode4_duke/processing/starr_seq/210401_KS91_K562ASTARR_NovaSeq.hg38-pe-umis

FP_WGS_ASTARR_INP=($(ls ${FD_WGS_ASTARR_INP}/*counts.txt.gz))
FP_WGS_ASTARR_OUT=($(ls ${FD_WGS_ASTARR_OUT}/*f3q10.fragments.counts.txt.gz))
FP_WGS_ASTARR=("${FP_WGS_ASTARR_INP[@]}" "${FP_WGS_ASTARR_OUT[@]}")

### peaks
FN_PEAKS_ASTARR_INP=KS91_K562_hg38_ASTARRseq_Input.all_reps.masked.union_narrowPeak.q5.bed