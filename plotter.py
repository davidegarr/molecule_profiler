import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# Read the CSV file into a DataFrame
df = pd.read_csv("clean_data.csv")

# Group by 'MaxClinicalPhase' and calculate the mean for 'MolecularWeight', 'csp3_quota', and 'AlogP'
grouped = df.groupby('MaxClinicalPhase').mean().reset_index()

# Prepare a figure
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Assigning variables to DataFrame columns
x = grouped['MolecularWeight']
y = grouped['csp3_quota']
z = grouped['AlogP']
colors = grouped['MaxClinicalPhase']

# Create the 3D scatter plot
scatter = ax.scatter(x, y, z, c=colors, cmap='coolwarm', s=100, alpha=0.6, edgecolors='w')

# Add labels and title
ax.set_xlabel('Average Molecular Weight (g/mol)')
ax.set_ylabel('Csp3 proportion')
ax.set_zlabel('Average AlogP')
plt.title('Clinical success based on MW, csp3 proportion, and average AlogP.')

# Add a color bar for the clinical phase scale
cbar = plt.colorbar(scatter, orientation='vertical')
cbar.set_label('Clinical Phase')

# Show the plot
plt.show()




