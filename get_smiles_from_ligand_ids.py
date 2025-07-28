import csv
import requests

from rdkit import Chem
from rdkit import RDLogger

RDLogger.DisableLog('rdApp.*')

input_file = 'pdb_to_ligand_mapping.csv'
output_file = 'pdb_to_ligand_mapping_with_smiles.csv'

rows = []
with open(input_file, 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ligand_id = row['ligand_id']
        print(f"Processing ligand_id: {ligand_id}")
        
        url = f"https://files.rcsb.org/ligands/download/{ligand_id}_ideal.sdf"
        print(f"Fetching SDF from: {url}")
        response = requests.get(url)
        response.raise_for_status()
        sdf_data = response.text
        print(f"Downloaded SDF for {ligand_id}, parsing molecule...")
        mol = Chem.MolFromMolBlock(sdf_data, removeHs=True)
        smiles = Chem.MolToSmiles(mol, isomericSmiles=True, canonical=True)
        print(f"SMILES for {ligand_id}: {smiles}")
        row['smiles'] = smiles
        rows.append(row)

fieldnames = ['pdb_id', 'ligand_id', 'smiles']
with open(output_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)