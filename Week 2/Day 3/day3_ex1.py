# Exercise 1: Create and explore a sample dataset
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

# Load the dataset from the URL
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Explore the structure
#print("First 5 rows\n", df.head())
#print("Last 5 rows\n", df.tail())
#print(df.info())
print(df.describe())
