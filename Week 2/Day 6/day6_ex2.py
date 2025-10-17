# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

# Exercise 2: Create a heatmap with Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Drop non-numerical column from the dataset
del df['species']

# Calculate correlation matrix
correlation_matrix = df.corr()

# Plot the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()