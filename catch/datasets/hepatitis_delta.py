"""Dataset with 'Hepatitis delta virus' sequences.

A dataset with 470 'Hepatitis delta virus' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/hepatitis_delta.fasta.gz", relative=True)
sys.modules[__name__] = ds
