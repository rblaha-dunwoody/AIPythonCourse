# Introduction to Cross-Validation

# What is Cross-Validation?
#   - Technique used to assess how well a machine learning model generalizes to an independent dataset
#
# Types of Cross-Validation
#   - K-Fold Cross-Validation
#       - Splits the dataset into K folds of approximately equal size
#       - The model is trained on K-1 folds and validated on the remaining fold
#       - This process is repeated K times, and the average performance is computed
#
#   - Stratified K-Fold
#       - Ensures that each fold maintains the same class distribution as the original dataset
#       - Useful for imbalanced datasets
#
#   - Leave-One-Out Cross-Valiation (LOOCV)
#       - Uses a single data point for validation and the rest for training
#       - Repeats this process for all data points
#       - Computationally expensive but provides the most robust evaluation


# Hyperparameter Tuning
#   What is Hyperparameter Tuning?
#       - Hyperparameters are parameters that are not learned by the model but are set before training
#       - Tuning these hyperparameters is crucial for optimizing model performance
#
#   Techniques for Hyperparameter Tuning
#       - Grid Search
#           - Exhaustively searches over a predefined hyperparameter space
#           - Example: Testing all combinations of values for max_depth and learning_rate
#
#       - Random Search
#           - Randomly samples combinations of hyperparameters from the predefined space
#           - More efficient than Grid Search when the parameter space is large
#
#       - Importance of Hyperparameter Tuning
#           - Prevents overfitting and underfitting by selecting the best configuration
#           - Enhances model performance by optimizing critical settings


# Importance of Tuning Hyperparameters for Model Performance
#   - Without tuning, the model might not reach its optimal performance, leading to:
#       - Underfitting: Model fails to capture the underlying patterns
#       - Overfitting: Model memorizes the training data and performs poorly on unseen data