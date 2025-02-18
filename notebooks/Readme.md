# Notebook

## Naming convension

ACTION terms
- get
- setup
- check

- link
- linking

- create
- acquire
- prepare
- execute
- explore
- export
- summary
- combine
- arrange

## Folder setup

```
PROJECT/notebook
├── 0x setup and prepare
├── 1x STARR/MPRA
├── 2x CRISPR
├── 3x Region merge/coverage/annotation
├── 4x Hi-C
└── 5x integrated
```

## Notebooks

```
PROJECT/notebook
├── 01_setup
├── 02_prepare
├── 1x_STARR/MPRA
├── 2x_CRISPR
|
├── 31_region_explore/nuc/merge (???) ### properties, merge preparation, exploration
|
├── 32_region_covearge
|   ├── 01_region_coverage_count (???)
|   ├── 02_region_coverage_score (???)

|   ├── 11_region_cov_combine_starr
|   ├── 12_region_cov_combine_tmpra
|   ├── 13_region_cov_combine_lmpra
|   ├── 14_region_cov_combine_crispri_hcrff
|   ├── 15_region_cov_combine_crispri_growth

|   ├── 21_region_cov_deseq_starr
|   ├── 22_region_cov_deseq_tmpra

|   ├── 3x_region_cov_summary_{starr/mpra/crispri}
|   ├── 4x_region_cov_explore_{starr/mpra/crispri}
|
├── 33_region_annotation
|
├── 41_hic_explore/nuc/ (???)
├── 42_hic_coverage
├── 43_hic_annotation
├── 44_hic_meta
|
└── 5x integrated
```

## 32 Region coverage
- region coverage (STARR/TMPRA)
    - calculate coverage (count)
    - combine -> matrix
    - apply DESeq2
    - explore
    - summary
    
- region coverage (LMPRA/CRISPRi)
    - calculate coverage (z score)
    - explore
    - summary

- 0x_region_coverage
    - Cal coverage (counts/scores) for all assays
    - counts: `bedtools map`
    - scores: `bedtools intersect`

- 1x_region_cov_combine
    - Agg coverage into matrix form

- 2x_region_cov_deseq
    - Apply DESeq for counts

- 3x_region_cov_summary
    - Get normalized counts (CPM/TPM/DESeq)
    - Cal statistics of scores
    
- 4x_region_cov_exlore
    - visualizations 















