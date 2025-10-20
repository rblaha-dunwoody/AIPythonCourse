# Data Scaling and Normalization

# Importance of Scaling and Normalization in Machine Learning
#
# What is Scaling and Normalization?
#   - Preprocessing techniques used to tranform numerical features to a common range or distribution
#   - Ensures that no numerical features dominate the model due to its magnitude
#
# Why is Scaling and Normalization important?
#   - Improves Algorithm Performance
#   - Ensures Fair Comparisons
#   - Stabilizes Training

# Methods: Min-Max Scaling, Standardization (Z-Score Scaling)
#
# Min-Max Scaling
#   - Transforms features to a specified range, typically [0, 1]
#   - Ensures all feature values are within the same range
#   - Use Cases: k-NN or neural networks
#   - Limitations: Sensitive to outliers, as extreme values can distort the scale
#
# Standardization (Z-Score Scaling)
#   - Centers the data around 0 and scales it to have a standard deviation of 1
#   - Ensures a standard normal distribution for each features
#   - Use Cases: SVM, logistic regression, and PCA
#   - Advantages: Handles outliers better than Min-Max Scaling

# What to Use Scaling and Normalization for Different Algorithms
# 
# Algorithms That Require Scaling
#   - Distance-Based Algorithms
#       - k-NN, SVM, K-Means clustering
#   
#   - Gradient-Based Models
#       - Linear regression, logistic regression and neural networks
#
# Algorithms Less Sensitive to Scaling
#   - Tree-Based Models
#       - Decision Trees, Random Forests, Gradient Boosting