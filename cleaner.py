import csv


#opens source file and creates the reader
with open("raw_data.csv", "r") as raw_data:
    csvreader = csv.DictReader(raw_data, delimiter = ";")
    
    #opens target file and creates the writer
    with open("clean_data.csv", "w", newline='') as clean_data:
        headers = ["ChEMBL_ID", "SMILES", "MolecularWeight", "MaxClinicalPhase"]
        csvwriter = csv.DictWriter(clean_data, fieldnames=headers)
        
        csvwriter.writeheader()
        #copies only the indicated values in the new row if all of them are present in source
        for row in csvreader:
            if any(value == "" for value in row.values()):
                continue
            csvwriter.writerow({
                'ChEMBL_ID': str(row['ChEMBL ID']), 
                'SMILES': str(row['Smiles']), 
                'MolecularWeight': float(row['Molecular Weight']), 
                'MaxClinicalPhase': float(row['Max Phase'])
            })


