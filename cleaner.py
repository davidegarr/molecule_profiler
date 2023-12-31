import csv
from rdkit import Chem

def main():
    #opens source file and creates the reader
    with open("raw_data.csv", "r") as raw_data:
        csvreader = csv.DictReader(raw_data, delimiter = ";")
        
        #opens target file and creates the writer
        with open("clean_data.csv", "w", newline='') as clean_data:
            headers = ["ChEMBL_ID", "SMILES", "MolecularWeight", "MaxClinicalPhase", "csp3_quota", "AlogP"]
            csvwriter = csv.DictWriter(clean_data, fieldnames=headers)
            
            csvwriter.writeheader()
            #copies only the indicated values in the new row if all of them are present in source
            for row in csvreader:
                if row["AlogP"] == "None" or row['Molecular Weight'] == "" or row['Max Phase'] == "" or row["Smiles"] == "":
                    continue
                
                #sends the smiles to get the csp3 quota. If the molecules has no carbons, ie returns None, skip it.
                csp3_quota = get_csp3_quota(str(row["Smiles"]))
                if csp3_quota == None:
                    continue

                #writes into the new file only relevant fields.
                csvwriter.writerow({
                    'ChEMBL_ID': str(row['ChEMBL ID']), 
                    'SMILES': str(row['Smiles']), 
                    'MolecularWeight': float(row['Molecular Weight']), 
                    'MaxClinicalPhase': float(row['Max Phase']),
                    "csp3_quota": csp3_quota,
                    "AlogP": float(row["AlogP"])
                })


#calculates csp3 proportions with respect total amount of carbon atoms.
def get_csp3_quota(smiles):
    #creates molecule from smiles
    molecule = Chem.MolFromSmiles(smiles)
    num_atoms = molecule.GetNumAtoms()
    sp3_carbons = 0
    total_carbons = 0

    for atom_idx in range(num_atoms):
        atom = molecule.GetAtomWithIdx(atom_idx)
        symbol = atom.GetSymbol()


        if symbol != "C":
            continue

        total_carbons += 1
        hybridization = get_hybridization(molecule, atom_idx)

        if hybridization == Chem.rdchem.HybridizationType.SP3:
            sp3_carbons += 1
    
    #try/except block handles inorganic (no C) molecules
    try:
        quota = float(sp3_carbons/total_carbons)
        return round(quota, 3)
    except ZeroDivisionError:
        return None
    

#returns hybridization of a given atom
def get_hybridization(molecule, atom_idx):
    atom = molecule.GetAtomWithIdx(atom_idx)  # Get atom by index
    hybridization = atom.GetHybridization()  # Retrieve hybridization
    return hybridization

main()