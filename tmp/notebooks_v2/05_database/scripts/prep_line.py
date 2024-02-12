
def prep_line_fragment(line, sample=None):
    """Function to process each line"""
    ### parse info: Chrom, Start, Stop, Name, Score, Strand
    key = f"{line[0]}_{line[1]}_{line[2]}"
    val = [key, *line[0:3], *line[6:14]]
    return val

def prep_line_motif(line, sample=None):
    """Function to process each line"""
    ### parse info: Chrom, Start, Stop, Motif, Score
    key = f"{line[0]}_{line[1]}_{line[2]}_{line[3]}"
    val = [key, *line]
    return val

### helper function to process each row
def prep_line_count(line, sample=None):
    """Function to process each line"""
    key = f"{line[0]}_{line[1]}_{line[2]}"
    val = [key, sample, line[4]]
    return val

def prep_line_annotation(line, sample=None):
    """Function to process each line"""
    ### parse info: Chrom, Start, Stop, Name, Score, Strand
    fragment = f"{line[0]}_{line[1]}_{line[2]}"
    binding  = f"{line[6]}_{line[7]}_{line[8]}_{line[9]}"
    return fragment, binding

def prep_line_coverage(line, sample=None):
    """Function to process each line"""
    return [line[0], line[1], line[3], sample]


dct_prep_line = {
    "Fragment":   prep_line_fragment,
    "Motif":      prep_line_motif,
    "Count":      prep_line_count,
    "Annotation": prep_line_annotation,
    "Coverage":   prep_line_coverage
}