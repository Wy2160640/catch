"""Dataset with 'Gammapapillomavirus 27' sequences.

A dataset with 1 'Gammapapillomavirus 27' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/gammapapillomavirus_27.fasta.gz", relative=True)
sys.modules[__name__] = ds
