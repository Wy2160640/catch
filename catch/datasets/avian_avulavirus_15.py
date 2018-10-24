"""Dataset with 'Avian avulavirus 15' sequences.

A dataset with 1 'Avian avulavirus 15' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/avian_avulavirus_15.fasta.gz", relative=True)
sys.modules[__name__] = ds
