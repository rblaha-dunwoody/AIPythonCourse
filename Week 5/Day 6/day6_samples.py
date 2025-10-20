# Introduction to k-Nearest Neightbors (k-NN) Algorithm and Its Applications

# What is k-Nearest Neighbors?
#   - Non-parametric, instnace-based machine learning algorithm used for both classification and regression tasks
#   - Relies on the similarity between data points to make predictions
#
#   - Key Characterstics
#       - Instance-Based Learning
#       - Distance Metric
#       - Classification
#       - Regression
#
#   - Applications
#       - Image Recognition
#       - Recommendation Systems
#       - Medical Diagnostics
#       - Customer Segmentation

# How k-NN Works for Classification and Regression
#
# Step-by-step Process
#   - Feature Scaling
#   - Calculate Distances
#   - Identify k Nearest Neighbors
#   - Make Predictions
#       - Classification
#       - Regression

# Choosing the Optimal Value of k
# 
# Choosing k
#   - Small k
#       - High sensitivity to noise
#       - Captures local variations in data
#   - Large k
#       - Smoother decision boundaries but can miss finer details
#
# Common Practices
#   - Use cross-validation to determine the optimal value of k
#   - A common starting point is k = sqrt(n), where n is the number of training samples

# Understanding the Model's Limitations
#
# Computationally Expensive
#   - Predictions require distance computation for all training samples
#
# Feature Scaling Dependence
#   - Requires proper scaling to avoid feature dominance
#
# Not Robust to Imbalanced Data
#   - Classes with more smaples can dominate predictions


