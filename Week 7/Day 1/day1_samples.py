# Introduction to Ensemble Learning

# Concept of Ensemble Learning
#   What is Ensemble Learning?
#       - Machine Learning technique that combines the predictions of multiple models to produce a final output
#
# Why Does Ensemble Learning Improve Performance?
#   - Reduces Variance
#   - Reduces Bias
#   - Improves Robustness
#
# Applications
#   - Fraud detection, medical diagnosis, recommendation systems, and predictive analytics


# Types of Ensemble Methods
#   - Bagging (Bootstrap Aggregating)
#       - Trains multiple models independently on different subsets of data created through bootstrapping
#       - Combines predictions by averaging (regression) or majority voting (classification)
#       - Example: Random Forest
#       - Strengths: Reduces variance without increasing bias
#
#   - Boosting
#       - Trains models sequentially, where each model focuses on correcting the errors made by the previous ones
#       - Combines predictions through weighted averaging or voting
#       - Examples: AdaBoost, Gradient Boosting, XGBoost, LightGBM
#       - Strengths: Reduces both bias and variance by focusing on hard-to-predict instances
#
#   - Stacking
#       - Combines predictions from multiple base models (of different types) using a meta-model to learn how to best combine their outputs
#       - Strengths: Can utilize diverse model types to maximize performance


# Overview of Commonly Used Ensemble Methods
#   - Random Forest
#       - Combines multiple decision trees using bagging
#       - Reduces overfitting common in individual decision trees
# 
#   - Gradient Boosting
#       - Sequentially builds models that minimize errors in the previous ones
#       - Suitable for both regression and classification tasks
#
#   - AdaBoost
#       - Adjusts model weights based on performance
#       - Focuses on misclassified instances
#
#   - XGBoost
#       - Optimized version of gradient boosting, known for speed and accuracy
#
#   - Voting Classifier
#       - Combines predictions of multiple models using majority voting or averaging