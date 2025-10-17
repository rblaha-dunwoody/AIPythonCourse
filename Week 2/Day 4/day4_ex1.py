# Clean a dataset by handling missing values and renaming columns
import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Age": [25, np.nan, 30, 35],
    "Score": [85, 90, np.nan, 88]
}

df = pd.DataFrame(data)

print("Original Dataset:\n", df)

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

print("Cleaned Dataset:\n", df)

# Rename columns
df = df.rename(columns={"Name":"Student_name", "Score":"Exam:Score"})
print("New Names:\n", df)