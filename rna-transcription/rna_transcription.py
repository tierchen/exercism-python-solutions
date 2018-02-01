def to_rna(dna_strand):
    if not set(dna_strand) <= set('GCTA'):
        raise ValueError('Invalid input')
    return dna_strand.translate(str.maketrans('GCTA', 'CGAU'))