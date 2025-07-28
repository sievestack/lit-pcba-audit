# LIT-PCBA Audit

This repository contains scripts and curated data to reproduce the audit of the LIT-PCBA benchmark, as detailed in our paper:  
*“Data Leakage and Redundancy in the LIT-PCBA Benchmark Dataset.”*

## Overview

The LIT-PCBA benchmark is widely used for evaluating virtual screening models. However, our audit reveals fundamental data integrity failures that invalidate its use for fair model evaluation.

Key issues identified include:

- **Inter-set Identity Leakage:** Identical molecules duplicated across supposedly disjoint sets.  
  - 3 query ligands leaked into training and validation sets.  
  - 2,491 unique inactive compounds shared between training and validation.

- **Intra-set Identity Redundancy:** Molecule duplicates within single sets.  
  - 2,945 unique inactives duplicated in training set.  
  - 789 unique inactives duplicated in validation set.

- **Analog Leakage & Redundancy:** High similarity saturation reduces chemical diversity.  
  - ALDH1 target: 323 highly similar active compound pairs between training and validation.  
  - MTORC1 target: 9 of 11 query ligands are near-duplicates.

- **Incorrect Ligand Information:** Query ligands provided as `.mol2` files lack bond order, causing unreliable SMILES.  

These flaws enable models to appear highly performant through memorization rather than true generalization.

## Purpose of this Repository

- To enable full reproduction of our audit and verification of data integrity failures.
- To provide manually curated query ligand data with correct PDB codes, ligand IDs, and canonical SMILES strings.
  
*Note:* We do **not** provide a “cleaned” LIT-PCBA dataset; the issues are systemic and require new benchmark development rather than filtering.

## Usage

1. Clone the repository.  
2. Install dependencies (e.g., RDKit, requests).  
3. Run audit scripts to verify findings of leakage and redundancy.  
4. Use `pdb_to_ligand_mapping_with_smiles.csv` for corrected query ligand data.

## Citation

If you use the scripts or data, please cite our work.  

Repository: https://github.com/sievestack/LIT-PCBA-audit