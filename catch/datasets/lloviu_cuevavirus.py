"""Dataset with 'Lloviu cuevavirus' sequences.

A dataset with 1 'Lloviu cuevavirus' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/lloviu_cuevavirus.fasta.gz", relative=True)
sys.modules[__name__] = ds
