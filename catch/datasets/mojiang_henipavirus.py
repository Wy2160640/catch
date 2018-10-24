"""Dataset with 'Mojiang henipavirus' sequences.

A dataset with 1 'Mojiang henipavirus' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/mojiang_henipavirus.fasta.gz", relative=True)
sys.modules[__name__] = ds
