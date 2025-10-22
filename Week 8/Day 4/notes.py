# Regularization Techniques for Model Optimization

# Understanding Overfitting and Underfitting
#   Overfitting
#       - Occurs when a model learns the noise in the training data along with the patterns
#       - Leads to poor generalization on unseen data
#       - Symptoms:
#           - High training accuracy but low test accuracy
#           - Large differences between training and valiation losses
#
#   Underfitting
#       - Occurs when a model is too simple to capture the underlying patterns in the data
#       - Symptoms:
#           - Low accuracy on both training and test sets
#           - High bias in predictions


# Regularization Techniques
#   - Regularization introduces a penalty term to the loss function during model training
#   - This prevents overfitting by discouraging overly complex models
#   - L1 Regularization (Lasso)
#       - Adds the absolute values of coefficients to the loss function
#       - Encourages sparsity by setting some coefficients to zero, effectively selecting features
#
#   - L2 Regularization (Ridge)
#       - Adds the squared values of coefficients to the loss function
#       - Shrinks coefficients toward zero but does not set them to zero
#
#   - Elastic Net
#       - Combines L1 and L2 regularization
#       - Useful when there are correlated predictors and when feature selectoin is desired


# Practical Applications of Regularization
#   Prevent Overfitting
#       - Penalizes large coefficients, reducing model complexity
#
#   Handle Multicollinearity
#       - Ridge regularization is effective when predictors are highly correlated
#
#   Feature Selection
#       - Lasso automatically performs feature selection by setting some coefficients to zero