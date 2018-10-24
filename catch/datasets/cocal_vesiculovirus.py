"""Dataset with 'Cocal vesiculovirus' sequences.

A dataset with 1 'Cocal vesiculovirus' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/cocal_vesiculovirus.fasta.gz", relative=True)
sys.modules[__name__] = ds
