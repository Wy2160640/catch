"""Dataset with 'Influenza C virus' sequences.

A dataset with 743 'Influenza C virus' sequences. The virus is
segmented and has 7 segments. Based on their strain and/or isolate,
these sequences were able to be grouped into 239 genomes. Many genomes
may have fewer than 7 segments.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetMultiChrom


def seq_header_to_chr(header):
    import re
    c = re.compile(r'\[segment (1|2|3|4|5|6|7)\]')
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


chrs = ["segment_" + seg for seg in ['1', '2', '3', '4', '5', '6', '7']]
ds = GenomesDatasetMultiChrom(__name__, __file__, __spec__,
                              chrs, seq_header_to_chr,
                              seq_header_to_genome=seq_header_to_genome)
for seg in ['1', '2', '3', '4', '5', '6', '7']:
    ds.add_fasta_path("data/influenza_c_segment" + seg + ".fasta.gz",
        relative=True)
sys.modules[__name__] = ds
