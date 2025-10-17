# Exercise 1: Group data by categorical column
import pandas as pd
import numpy as np

data = {
    "Class": ["A", "B", "A", "B", "C", "C"],
    "Score": [85, 90, 88, 72, 95, 80],
    "Age": [15, 16, 15, 17, 16, 15]
}

df = pd.DataFrame(data)

print("Original:\n", df)

grouped = df.groupby("Class").mean()
print("Grouped by Class:\n", grouped)