"""Dataset with 'Human betaherpesvirus 6A' sequences.

A dataset with 3 'Human betaherpesvirus 6A' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/human_betaherpesvirus_6a.fasta.gz", relative=True)
sys.modules[__name__] = ds
