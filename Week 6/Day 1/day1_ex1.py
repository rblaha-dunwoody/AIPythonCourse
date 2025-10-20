# Exercise 1: Load a dataset and explore its features, identifying categorical and numerical features
import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

# Display dataset information
print("Dataset Info: \n")
print(df.info())

# Preview the first few rows
print("\nDataset Preview:\n")
print(df.head())

# Separate features
categorical_features = df.select_dtypes(include=["object"]).columns
numerical_features = df.select_dtypes(include=["int64", "float64"]).columns

print("\nCategorical Features: ", categorical_features.tolist())
print("\nNumerical Features: ", numerical_features.tolist())


# Exercise 2: Plan which feature engineering techniques might be the most suitable for the dataset

# Display summary of categorical features
print("\nCategorical Features Summary:\n")
for col in categorical_features:
    print(f"{col}:\n", df[col].value_counts(), "\n")

# Display summary of numerical features
print("\nNumerical Features Summary:\n")
print(df[numerical_features].describe())
