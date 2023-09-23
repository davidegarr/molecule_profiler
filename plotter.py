import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("clean_data.csv")

# Group by 'MaxClinicalPhase' and calculate the mean for 'MolecularWeight' and 'csp3_quota'
grouped = df.groupby('MaxClinicalPhase').mean().reset_index()

# Prepare a figure
plt.figure(figsize=(10, 10))

# Assigning variables to DataFrame columns
x = grouped['MolecularWeight']
y = grouped['csp3_quota']
colors = grouped['MaxClinicalPhase']

# Create the scatter plot
scatter = plt.scatter(x, y, c=colors, cmap='coolwarm', s=100, alpha=1, edgecolors='w')

# Add labels and title
plt.xlabel('Average Molecular Weight (g/mol)')
plt.ylabel('Csp3 proportion')
plt.title('Clinical success based on MW and csp3 proportion.')

# Add a color bar for the clinical phase scale
cbar = plt.colorbar(scatter, orientation='vertical')
cbar.set_label('Clinical Phase')

# Show the plot
plt.show()



