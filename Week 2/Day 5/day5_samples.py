# Grouping data and aggregates

grouped = df.groupby("column_name")

for name, group in grouped:
    print(name)
    print(group)

grouped.mean()
grouped.sum()

# ==== Aggregation functions ====
df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column").agg({"numeric_column":["mean", "max", "min"]})

pivot = df.pivot_table(
    values="numeric_column",
    index="category_column",
    aggfunc="mean"
)

def range_func(x):
    return x.max - x.min

df.groupby("category_column")["numeric_column"].agg(range_func)



# ==== Calculating summary statistics ====
df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column")["numeric_column"].max()
df.groupby("category_column")["numeric_column"].min()


# ==== Multi-aggregation ====
df.groupby("category_column").agg(
    {"numeric_column": ["mean", "max", "min"]}
)