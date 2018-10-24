"""Dataset with 'Influenza B virus [segment 2]' sequences.

A dataset with 8293 'Influenza B virus [segment 2]' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/influenza_b_segment2.fasta.gz", relative=True)
sys.modules[__name__] = ds
