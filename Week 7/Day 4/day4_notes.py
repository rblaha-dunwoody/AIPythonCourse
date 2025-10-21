# Introduction to XGBoost

# Overview of XGBoost
#   What is XGBoost?
#       - eXtreme Gradient Boosting
#       - Advanced implementation of the Gradient Boosting algorithm designed for speed and performance
#       - It introduces various enhancements that make it faster, more efficient, and capable of handling complex datasets
#
#   Improvements Over Traditional Gradient Boosting
#       - Speed (parallel processing)
#       - Handling Missing Data Automatically
#       - Regularization (Ridge and Lasso)
#       - Custom Loss Functions
#       - Tree Pruning


# Key Features of XGBoost
#   Handling Missing Data
#       - Automatically assigns missing values to the branch that minimizes the loss function
#       - Reduces preprocessing steps for datasets with missing values
#
#   Regularization
#       - Includes penalties for overly complex models, reducing overfitting
#       - Hyperparameters
#           - lambda: L2 regularization term
#           - alpha: L1 regularization term
#
#   Parallel Processing
#       - Splits calculations for tree construction across multiple cores, significantly improving training time


# Hyperparameters in XGBoost and How to Tune Them
#   Key Hyperparameters
#       - Learning Rate (eta)
#           - Controls the contribution of each tree to the model
#           - Typical Range: 0.01-0.3
#
#       - Number of Trees (n_estimators)
#           - Determines the number of boosting rounds
#           - Larger values may improve performance but increase computation time
#
#       - Tree depth (max_depth)
#           - Limits the depth of trees, balancing bias and variance
#           - Shallower trees generalize better, while deeper trees may overfit
#
#       - Subsample
#           - Fraction of data used to train each tree
#           - Helps reduce overfitting; typical range: 0.5-1.0
#
#       - Colsample_bytree
#           - Fraction of features used for each tree split
#           - Typical range: 0.5-1.0
#
#       - Regularization Parameters: lambda and alpha control L2 and L1 regularization, respectively