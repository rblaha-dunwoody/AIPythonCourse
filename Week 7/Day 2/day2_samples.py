# Bagging and Random Forests

# Understanding Bagging (Bootstrap Aggregating)
#   What is Bagging?
#       - Ensemble learning technique that trains multiple models on different subsets of the data
#       - Created by random sampling with replacement
#       - Regression: Average the predictions of individual models
#       - Classification: Use majority voting to determine the final class
#
#   Why Use Bagging?
#       - Reduces Variance
#       - Improves Robustness
#  
#   Applications
#       - Bagging is commonly used with decision trees, which are prone to high variance


# Introduction to Random Forests
#   What is a Random Forest?
#       - Ensemble learning method that builds multiple decision trees using bagging
#       - Key Features of Random Forests:
#           - Bootstrap Sampling
#           - Feature Randomness
#           - Prediction Aggregation
#
#       - Advantages
#           - Handles both regression and classificatoni tasks effectively
#           - Works well with high-dimensional data
#           - Reduces overfitting compared to single decision trees


# Key Parameters in Random Forests
#   - Number of Trees (n_estimators)
#       - The number of decision trees in the forest
#       - Larger values reduce variance but increase computational cost
#
#   - Maximum Depth (max_depth)
#       - Limits the depth of each tree to prevent overfitting
#       - Shallower trees generalize better but may underfit
#
#   - Feature Selection (max_features)
#       - Number of features to consider when looking for the best split
#       - Options:
#           - sqrt | log2 | None
#
#   - Minimum Samples per Leaf (min_samples_leaf)
#       - Minimum number of samples required in a leaf node
#       - Prevents overly complex trees by ensuring each leaf contains enough samples