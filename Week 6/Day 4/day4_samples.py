# Feature Selection Techniques

# Introduction to Feature Selection
#   - What is Feature Selection?
#       - Process of identifying and retaining the most relevant features (input variables) in a dataset while discarding irrelevant or redundant ones
#
#   - Why is Feature Selection Important?
#       - Improves Model Performance
#       - Reduces Overfitting
#       - Enhances Interpretability
#       - Increases Computational Efficiency
#
#   - When to Use Feature Selection?
#       - High-Dimensional Data
#       - Correlated Features
#       - Reducing Complexity

# Techniques for Feature Selection
#   - Filter Methods
#       - Evaluate the relevance of features by analyzing their statistical properties in relation to the target variable
#       - Examples: Correlation | Mutual Information
#       - When to Use: Quick evaluation of features before training a model
#
#   - Wrapper Methods
#       - Iteratively selects features by training and evaluating a model
#       - Examples: Forward Selection | Backward Elimination
#       - When to Use: USeful when feature interactions are important but computationally expensive
#  
#   - Embedded Methods
#       - Perform feature selection as part of the model training process
#       - Examples: Lasso Regression | Tree-Based Models
#       - When to Use: Effective when training tree-based models or regularized regression