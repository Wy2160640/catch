"""Dataset with 'Torque teno mini virus ALH8' sequences.

A dataset with 1 'Torque teno mini virus ALH8' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/torque_teno_mini_virus_alh8.fasta.gz", relative=True)
sys.modules[__name__] = ds
