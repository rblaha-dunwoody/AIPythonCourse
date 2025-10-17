#Exercise 2: Select specific columns and rows
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

# Load the dataset from the URL
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Select specific column(s)
selected_columns = df[["species", "sepal_length"]]
#print("Selected columns:\n", selected_columns)

# Filter rows
filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filtered rows: \n", filtered_rows)