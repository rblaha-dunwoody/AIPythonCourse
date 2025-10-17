import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
#print(s)

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
#print(df)

# Import from spreadsheet
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# Export to spreadsheet
df.to_csv("data.csv", index=False)
df.to_excel("data.xlsx", index=False)

# ==== DataFrame operations ====
print(df.head())            # Prints first 5 rows of a DF
print(df.tail(3))           # Prints last 3 rows of a DF
print(df.info())            # Provides high level info
print(df.describe())        # Provides more intricate detail of a DF

# ==== Selecting and indexing ====
print(df["Name"])           # Gets a single column from a DF
print(df["Name", "Age"])    # Gets a multiple columns from a DF
print(df[df["Age"] > 25])   # Gets rows where the "Age" property is greater than 25
print(df.iloc[0])           # Gets a row by index
print(df.iloc[:, 0])