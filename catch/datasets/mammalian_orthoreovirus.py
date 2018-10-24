"""Dataset with 'Mammalian orthoreovirus' sequences.

A dataset with 587 'Mammalian orthoreovirus' sequences. The virus is
segmented and has 10 segments. Based on their strain and/or isolate,
these sequences were able to be grouped into 220 genomes. Many genomes
may have fewer than 10 segments.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetMultiChrom


def seq_header_to_chr(header):
    import re
    c = re.compile(r'\[segment (L1|L2|L3|M1|M2|M3|S1|S2|S3|S4)\]')
    m = c.search(header)
    if not m:
        raise Exception("Unknown or invalid segment in header %s" % header)
    seg = m.group(1)
    return "segment_" + seg

def seq_header_to_genome(header):
    import re
    c = re.compile(r'\[genome (.+)\]')
    m = c.search(header)
    if not m:
        raise Exception("Unknown genome in header %s" % header)
    return m.group(1)


chrs = ["segment_" + seg for seg in ['L1', 'L2', 'L3', 'M1', 'M2', 'M3', 'S1', 'S2', 'S3', 'S4']]
ds = GenomesDatasetMultiChrom(__name__, __file__, __spec__,
                              chrs, seq_header_to_chr,
                              seq_header_to_genome=seq_header_to_genome)
ds.add_fasta_path("data/mammalian_orthoreovirus.fasta.gz", relative=True)
sys.modules[__name__] = ds
