# Encoding Categorical Variables


# One-Hot Encoding, Label Encoding
#
# What are Categorical Variables?
#   - Binary Categorical Featuers: Gender (Male/Female)
#   - Multi-Class Categorical Features: Country (USA, Canada, UK, etc...)
#   - Since machine learning algorithms require numerical inputs, categorical variables must be transformed into numerical representations
#
# One-Hot Encoding
#   - Creates binary columns for each category in a categorical features
#   - Each row is marked with a 1 for its respected category and 0 elsewhere
#   - Example: Feature: Color = ['Red', 'Blue', 'Green']
#       ---------------------------
#       Red     | Blue      | Green
#       ---------------------------
#       1       | 0         | 0
#       0       | 1         | 0
#       0       | 0         | 1
#       ---------------------------
#   - Applications
#       - Categorical features with a small number of unique categories
#       - Tree-based models, logistic regression, and neural networks
#
# Label Encoding
#   - Label Encoding assigns a unique integer to each category
#   - Example: Red = 0, Blue = 1, Green = 2
#   - Applications
#       - Ordinal features where the order matters
#       - Can introduce unintended ordinal relationships for nominal features
#   - Limitations
#       - Can mislead algorithms into interpreting categories as ordered, espeically when the variable is nominal


# Dealing with High-Cardinality Categorical Features
#   - High-cardinality categorical features contain a large number of unique categories (names, locations, etc)
#   - Challenges
#       - Dimensionality
#       - Sparse representation (sometimes many categories will have 0 counts, leading to sparsity in the data set)
#   - Solutions
#       - Frequency Encoding
#           - Replace categories with their occurence frequency in the dataset
#           - Example: City=['NY', 'LA', 'NY', 'SF', 'LA'], Encoded=['NY'=2, 'LA'=2, 'SF'=1]
#       - Target Encoding
#           - Replace categories with the mean of the target variable for each category


# When to Use Different Encoding Techniques
# |-------------------------|-------------------------------------------------------------------------------|
# | Encoding Technique      | Use Case                                                                      |
# |-------------------------|-------------------------------------------------------------------------------|
# | One-Hot Encoding        | Nominal features with a small number of unique categories                     |
# | Label Encoding          | Ordinal features or when used with algorithms like tree-based models          |
# | Frequency Encoding      | High-cardinality features in both regression and classification tasks         |
# | Target Encoding         | High-cardinality features in supervised learning tasks                        |
# |-------------------------|-------------------------------------------------------------------------------|