# Model Evaluation Techniques

# Evaluation Metrics for Regression
#
# Regression Metrics
#   - Mean Absolute Error (MAE)
#       - Measures the average magnitude of errors without considering their direction
#       - Use Case: Suitable when all errors have equal importance
#
#   - Mean Squared Error (MSE)
#       - Measures the average of squared differences between actual and predicted values
#       - Use Case: Penalizes larger errors more than MAE, making it sensitive to outliers
#
#   - Root Mean Squared Error (RMSE)
#       - Square Root of MSE, providing errors in the same units as the target variable
#       - Use Case: A common metric for interpretability in real-world units
#
#   - R-Squared (R^2)
#       - Measures how well the model explains the variability of the target variable
#       - Use Case: Indicates the porportion of variance explained by the model


# Evaluation Metrics for Classification
#
# Classification Metrics
#   - Accuracy
#       - Percentage of correctly classified instances
#       - Use Case: Suitable for balanced datasets but misleading for imbalanced data
#
#   - Precision
#       - Fraction of true positive predictions among all positive predictions
#       - Use Case: Important when false positives are costly (e.g., spam detection)
#
#   - Recall (Sensitivity)
#       - Fraction of true positives identified among all actual positives
#       - Use Case: Critical in situations where missing positives is costly (e.g., medical diagnosis)
#
#   - F1 Score
#       - Harmonic mean of precision and recall
#       - Use Case: Useful for imbalanced datasets
#
#   - ROC-AUC
#       - Measures the ability of the model to distinguish between classes
#       - Use Case: Important for evaluating binary classifiers


# Understanding When to Use Each Metric
#
# Regression
#   - Use MAE for interpretability and uniform importance of errors
#   - Use MSE/RMSE when larger errors need greater penalization
#   - Use R^2 to explain variance but not as a sole performace metric
#
# Classification
#   - Use accuracy for balanced datasets
#   - Use precision and recall for imbalanced datasets, depending on the problem's focus (e.g., minimizing false positives or false negatives)
#   - Use F1 Score for a balanced evaluation of precision and recall
#   - Use ROC-AUC for overall model performance evaluation in binary classification