# Planning for data and results


# Working directory

```
PROJECT
├── app
│   └── singularity_proj_encode_fcc.sif
├── data
│   ├── external
│   └── processed
├── results
├── scripts
├── references
├── notebooks
├── docs
├── site
├── log
├── README.md
└── .gitignore
```


## Working directory: `Reference file`
```
PROJECT/reference
├── fcc_trackhub_jinwoo
│   ├── 
│   └── 
├── encode_chipseq_flagship
└── encode_open_chromatin
```

## Working directory: `Data` (Get processed data and download external data)
Data: original files and names
why do I want to split the folder into processed and external
=> to distinguish the downloadable data and 
```
PROJECT/data
├── external
│   ├── encode_open_chromatin
│   │   ├── 
│   │   └── 
│   ├── encode_ccres
│   ├── encode_chromhmm
│   ├── encode_astarr_csaw (???)
│   ├── 
│   ├── encode_chipseq_flagship
│   ├── encode_chipseq_tf_subset
│   ├── encode_chipseq_histone
│   ├── 
│   ├── encode_crispri_hcrff_casa (???)
│   ├── encode_e2g
│   ├── encode_tss_jinwoo (X)
│   ├── encode_rnaseq
│   ├── 
│   ├── (genome_gencode)
│   ├── (genome_ncbi_refseq)
│   ├── 
│   ├── 
│   ├── hic_insitu_K562_ENCSR545YBD
│   ├── hic_intact_K562_ENCSR479XDG
│   ├── hic_intact_K562_deep
│   ├── chrom.sizes.hg19
│   └── chrom.sizes.hg38
│
└── processed
    ├── KS91_K562_hg38_ASTARRseq_210401
    │   ├── fragments
    │   │   ├── KS91_K562_hg38_ASTARRseq_Input_rep1.masked.dedup.fragments.counts.txt.gz
    │   │   ├── KS91_K562_hg38_ASTARRseq_Input_rep2.masked.dedup.fragments.counts.txt.gz
    │   │   ├── KS91_K562_hg38_ASTARRseq_Input_rep3.masked.dedup.fragments.counts.txt.gz
    │   │   ├── KS91_K562_hg38_ASTARRseq_Input_rep4.masked.dedup.fragments.counts.txt.gz
    │   │   ├── KS91_K562_hg38_ASTARRseq_Input_rep5.masked.dedup.fragments.counts.txt.gz
    │   │   ├── KS91_K562_hg38_ASTARRseq_Input_rep6.masked.dedup.fragments.counts.txt.gz
    │   │   ├── KS91_K562_hg38_ASTARRseq_Output_rep1.f3q10.fragments.counts.txt.gz
    │   │   ├── KS91_K562_hg38_ASTARRseq_Output_rep2.f3q10.fragments.counts.txt.gz
    │   │   ├── KS91_K562_hg38_ASTARRseq_Output_rep3.f3q10.fragments.counts.txt.gz
    │   │   └── KS91_K562_hg38_ASTARRseq_Output_rep4.f3q10.fragments.counts.txt.gz
    │   └── peaks
    │       ├── KS91_K562_hg38_ASTARRseq_Input.all_reps.masked.union_narrowPeak.q5.bed
    │       └── KS91_K562_hg38_ASTARRseq_Input.q5.in_all.max_overlaps.bed
    │   
    ├── A001_K562_hg38_WSTARRseq
    │   ├── fragments
    │   │   ├── A001-input-K562-rep1.masked.dedup.fragments.counts.txt.gz
    │   │   ├── A001-input-K562-rep2.masked.dedup.fragments.counts.txt.gz
    │   │   ├── A001-input-K562-rep3.masked.dedup.fragments.counts.txt.gz
    │   │   ├── A001-input-K562-rep4.masked.dedup.fragments.counts.txt.gz
    │   │   ├── A001-K562-rep1.masked.dedup.fragments.counts.txt.gz
    │   │   ├── A001-K562-rep2.masked.dedup.fragments.counts.txt.gz
    │   │   └── A001-K562-rep3.masked.dedup.fragments.counts.txt.gz
    │   └── peaks
    │   
    ├── MPRA_Tiling_K562_Tewhey_hannah
    │   └── tiling_counts
    │       ├── OL13_20220512_counts.out
    │       ├── OL13_20220512_normalized_counts.out
    │       ├── OL43_20211228_counts.out      
    │       ├── OL43_20211228_normalized_counts.out
    │       ├── OL43_20221003_counts.out 
    │       ├── OL43_20221003_K562_normalized_counts.out
    │       ├── OL45_20220927_counts.out 
    │       └── OL45_20220927_K562_normalized_counts.out
    │
    ├── MPRA_Lenti_K562_Nadav_vikram
    │
    │
    ├── CRISPRi_Growth_K562_Gersbach_alex
    │   ├── guides
    │   └── region
    │
    ├── fcc_trackhub_jinwoo
    │   ├── track_bedgraph
    │   │   ├── 
    │   │   └── 
    │   ├── track_bigwig
    │   └── region
    │       ├── tss_pol2
    │       └── tss_tse_crispri_hcrff
    │
    ├── fcc_enhancer_junke_zscore
    │
    ├── TF_modules_K562_shannon
    │
    └── 
```


## Working directory: `Results` (After data preparation)
- Process files in data (arrange/extract)
- SymLink files in data (file aliases)
```
PROJECT/results
├── assay_fcc
│   ├── STARR_ATAC_K562_Reddy_KS91
│   │   ├── fragment_counts
│   │   │   ├── ASTARRseq_K562_KS91.hg38.Input.rep1.WGS.unstranded.bed.gz
│   │   │   ├── ASTARRseq_K562_KS91.hg38.Input.rep2.WGS.unstranded.bed.gz
│   │   │   ├── ASTARRseq_K562_KS91.hg38.Input.rep3.WGS.unstranded.bed.gz
│   │   │   ├── ASTARRseq_K562_KS91.hg38.Input.rep4.WGS.unstranded.bed.gz
│   │   │   ├── ASTARRseq_K562_KS91.hg38.Input.rep5.WGS.unstranded.bed.gz
│   │   │   ├── ASTARRseq_K562_KS91.hg38.Input.rep6.WGS.unstranded.bed.gz
│   │   │   ├── ASTARRseq_K562_KS91.hg38.Output.rep1.WGS.unstranded.bed.gz
│   │   │   ├── ASTARRseq_K562_KS91.hg38.Output.rep2.WGS.unstranded.bed.gz
│   │   │   ├── ASTARRseq_K562_KS91.hg38.Output.rep3.WGS.unstranded.bed.gz
│   │   │   └── ASTARRseq_K562_KS91.hg38.Output.rep4.WGS.unstranded.bed.gz
│   │   └── fragment (???)
│   │
│   ├── STARR_WHG_K562_Reddy_A001
│   │   ├── fragment_counts
│   │   │   ├── WSTARRseq_K562_A001.hg38.Input.rep1.WGS.unstranded.bed.gz
│   │   │   ├── WSTARRseq_K562_A001.hg38.Input.rep2.WGS.unstranded.bed.gz
│   │   │   ├── WSTARRseq_K562_A001.hg38.Input.rep3.WGS.unstranded.bed.gz
│   │   │   ├── WSTARRseq_K562_A001.hg38.Input.rep4.WGS.unstranded.bed.gz
│   │   │   ├── WSTARRseq_K562_A001.hg38.Output.rep1.WGS.unstranded.bed.gz
│   │   │   ├── WSTARRseq_K562_A001.hg38.Output.rep2.WGS.unstranded.bed.gz
│   │   │   └── WSTARRseq_K562_A001.hg38.Output.rep3.WGS.unstranded.bed.gz
│   │   └── fragment
│   │
│   ├── MPRA_Tiling_K562_Tewhey_hannah
│   │   ├── fragment_counts
│   │   │   ├── TMPRA_K562_OL13_20220512.hg19.raw. Input .rep[1-4].stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL13_20220512.hg19.raw. Output.rep[1-4].stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL13_20220512.hg19.norm.Input .rep[1-4].stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL13_20220512.hg19.norm.Output.rep[1-4].stranded_pos.bed
│   │   │   │ 
│   │   │   ├── TMPRA_K562_OL13_20220512.hg19.norm.Input .mean.stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL13_20220512.hg19.norm.Output.mean.stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL13_20220512.hg19.norm.Log2FC.mean.stranded_pos.bed
│   │   │   │ 
│   │   │   ├── TMPRA_K562_OL43_20221003.hg38.raw. Input .rep[1-6].stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL43_20221003.hg38.raw. Output.rep[1-5].stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL43_20221003.hg38.norm.Input .rep[1-6].stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL43_20221003.hg38.norm.Output.rep[1-5].stranded_pos.bed
│   │   │   │ 
│   │   │   ├── TMPRA_K562_OL43_20221003.hg38.norm.Input .mean.stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL43_20221003.hg38.norm.Output.mean.stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL43_20221003.hg38.norm.Log2FC.mean.stranded_pos.bed
│   │   │   │ 
│   │   │   ├── TMPRA_K562_OL45_20220927.hg38.raw. Input .rep[1-4].stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL45_20220927.hg38.raw. Output.rep[1-4].stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL45_20220927.hg38.norm.Input .rep[1-4].stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL45_20220927.hg38.norm.Output.rep[1-4].stranded_pos.bed
│   │   │   │ 
│   │   │   ├── TMPRA_K562_OL45_20220927.hg38.norm.Input .mean.stranded_pos.bed
│   │   │   ├── TMPRA_K562_OL45_20220927.hg38.norm.Output.mean.stranded_pos.bed
│   │   │   └── TMPRA_K562_OL45_20220927.hg38.norm.Log2FC.mean.stranded_pos.bed
│   │   └── fragment
│   │
│   ├── MPRA_Lenti_K562_Nadav_Vikram
│   ├── CRISPRi_FlowFISH_K562_Riley_JinWoo
│   └── CRISPRi_Growth_K562_Gersbach_Alex
├── assay_hic
│   ├── hic_insitu_K562_ENCSR545YBD
│   ├── hic_intact_K562_ENCSR479XDG
│   └── hic_intact_K562_deep
├── region
│   ├── fcc_starr_macs
│   │   ├── ASTARRseq_K562_KS91.hg38.Input.rep_all.union.q5.bed
│   │   └── ASTARRseq_K562_KS91.hg38.Input.rep_all.max_overlaps.q5.bed
│   ├── fcc_starr_csaw
│   │   └── 
│   ├── fcc_enhancer_junke_zscore
│   ├── 
│   └── 
└── annotation
    ├── ASTARRseq_K562_KS91_Input_rep_all_union
    └── ASTARRseq_K562_KS91_Input_rep_all_max_overlap
```

## Some naming convention in this documentation

- Assay folder name
    - `<Assay Type>_<Cell Type>_<Lab>_<Label>`
    - Label
        - batch, source, people, id numbers

```
STARR_ATAC_K562_Reddy_KS91
STARR_WHG_K562_Reddy_A001
MPRA_Tiling_K562_Tewhey_hannah
MPRA_Lenti_K562_Nadav_vikram

CRISPRi_FlowFISH_K562_Riley_jinWoo
CRISPRi_Growth_K562_Gersbach_alex
```

- Assay file name
    - `<Prefix>.<Genome>.<Input/Output/Log2FC>.<Replicate>.<Region>.<Unstranded/Stranded>.<File Extension>`
    - Prefix
        - ASTARRseq_K562_KS91
        - WSTARRseq_K562_A001
        - TMPRA_K562_OL13
        - TMPRA_K562_OL43
        - TMPRA_K562_OL45
        - TMPRA_K562_Merge
        - LMPRA_K562
        - CRISPRi_HCRFF_K562
        - CRISPRi_Growth_K562
    - Replicate
        - rep1/2/3/4
        - rep1_vs_rep2
        - rep_all
    - Region
        - WHG = whole genome
        - MYC = MYC region
        - GATA1 = GATA1 region
       
- ENCODE region file name
    - `<Prefix>.<Genome>.<Experiment ID>.<File ID>.<Description>.<File Extension>`
    - Prefix: biosample
        - K562: a human erythroleukemic cell line
        - A549: a human lung epithelial Cell line
        - Hsa: Human
        - Mmu: Mouse
    - Genome: reference for alignment
        - hg38: GRCh38
        - hg19: GRCh37
        - mm10: GRCm38
    