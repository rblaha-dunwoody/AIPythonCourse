import pandas as pd

# ==== Handle missing values ====
df = df.dropna()            # Drop rows with missing values
df = df.dropna(axis=1)      # Drop columns with missing values

df["column_name"] = df["column_name"].fillna(0)     # Fills missing values with a default for a column

# Forward fill and backward fill
df.fillna(method="ffill")
df.fillna(method="bfill")

df["column_name"] = df["column_name".interpolate]   # Interpolated filling


# ==== Data Transformations ====
# Renaming columns
df = df.rename(columns={"old_name": "new_name"})

# Changing data types
df["column_name"] = df["column_name"].astype("float")
df["column_name"] = pd.to_datetime(df["column_name"])

# Creating or modifying columns
df["new_column"] = df["existing_column"] * 2


# ==== Combining and Merging DataFrames ====
# Concatenation
combined = pd.concat([df1, df2], axis=0)            # Combine DF's on rows
combined = pd.concat([df1, df2], axis=1)            # Combine DF's on columns

# Merging
merged = pd.merge(df1, df2, on="common_column")     # Merges DF's on common columns
merged = pd.merge(df1, df2, how="left", on="common_column") # Merges DF's on common columns using a left-join

# Joining
joined = df1.join(df2, how="inner")
