"""Dataset with 'Torque teno virus 24' sequences.

A dataset with 1 'Torque teno virus 24' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/torque_teno_virus_24.fasta.gz", relative=True)
sys.modules[__name__] = ds
