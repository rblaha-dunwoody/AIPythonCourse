# Boosting and Gradient Boosting

# Concept of Boosting
#   What is Boosting?
#       - Ensemble technique that sequentially combines weak learners to form a strong learner
#       - Each subsequent model focuses on correcting the errors made by previous models
#
#   How Does Boosting Differ from Bagging?
#       |---------------|-------------------------------------------------------|-----------------------------------------------|
#       | Feature       | Bagging                                               | Boosting                                      |
#       |---------------|-------------------------------------------------------|-----------------------------------------------|
#       | Approach      | Trains models independently on bootstrapped subsets   | Trains models sequentially to correct errors  |
#       | Purpose       | Reduces variance by averaging predictions             | Reduces bias by focusing on difficult cases   |
#       | Examples      | Random Forest                                         | Gradient Boosting, AdaBoost                   |
#       |---------------|-------------------------------------------------------|-----------------------------------------------|


# Gradient Boosting
#   What is Gradient Boosting?
#       - Boosting algorithm that builds models sequentially by minimizing a loss function using gradient descent
#       - Iteratively adds weak learners to improve overall model performance
#
#   How Gradient Boosting Works
#       - Initialize Model: Start with a simple model, often predicting the mean of the target variable
#       - Compute Residuals: Calculate the difference between the actual and predicted values
#       - Fit Weak Learner: Train a weak model to predict the residuals
#       - Update Prediction: Add the predictions of the weak learner to the overall model
#       - Repeat: Continue adding weak learners until the desired number of iterations or a stopping criterion is reached
#
#   Key Parameters in Gradient Boosting:
#       - Learning Rate
#           - Determines the contribution of each weak learner
#           - Smaller values reduce overfitting but require more iterations
#
#       - Number of estimators
#           - The number of weak learners (trees) added sequentially
#           - Larger values improve learning but increase computation time
#
#       - Regularization
#           - Techniques like limiting tree depth or adding penalties to prevent overfitting


# Understanding the Key Parameters
#   Learning Rate (learning_rate)
#       - Lower values improve model performance by reducing overfitting but require more iterations
#       - Typical range: 0.01 to 0.3
#
#   Number of Estimators (n_estimators)
#       - Represents the number of trees added to the ensemble
#       - Larger values can improve performance but risk overfitting
#
#   Tree Depth (max_depth)
#       - Limits the complexity of individual trees
#       - Shallower trees generalize better but might underfit