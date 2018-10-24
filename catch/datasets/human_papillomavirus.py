"""Dataset with 'Human papillomavirus' sequences.

A dataset with 12 'Human papillomavirus' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/human_papillomavirus.fasta.gz", relative=True)
sys.modules[__name__] = ds
