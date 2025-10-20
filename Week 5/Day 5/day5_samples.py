# Model Evaluation Metrics for Regression and Classification

# Model Evaluation for Regression
#   - Regression models predict continuous values and their performance is measured using error metrics
#   - Error Metrics:
#       - Mean Square Error (MSE)
#           - Measures the average squared difference between predicted and actual values
#           - Sensitive to outliers due to squaring of errors
#       - Mean Absolute Error (MAE)
#           - Measures the average absolute difference between predicted and actual values
#           - Provides a more interpretable measure but less sensitive to outliers
#       - Root Mean Squared Error (RMSE)
#           - Square root of MSE, providing errors in the same units as the target available

# Model Evaluation for Classification
#   - Classification models predict discrete classes and their performance is measured using metrics derived from confusion matrices
#       - Accuracy
#           - Proportion of correctly predicted instances
#           - Useful when the dataset is balanced
#       - Precision
#           - Fraction of positive predictions that are correct
#           - Important for applications like fraud detection, where false positives are costly
#       - Recall (Sensitivity)
#           - Fraction of actual positives that are correctly identified
#           - Useful in cases where missing positive instances is critical
#       - F1 Score
#           - Harmonic mean of precision and recall
#           - Balances precision and recall, especially useful for imbalanced datasets

# Introduction to Cross-Validation
#   - Key Cross-Valudation Techniques
#       - K-Fold Cross-Validation
#           - Splits the dataset into K equal parts
#           - Trains the model on K-1 folds and tests ton the remaining fold, repeating the process K times
#           - The averages of the K test scores provides the final evaluation metric
#       - Stratified K-Fold
#           - Ensures each fold has a proportional representation of classes in classification problems
#       - Leave-One-Out Cross-Validation (LOOCV)
#           - Trains the model on n-1 samples and tests on the remaining one. Repeated for all samples.
#           - Compulationally expensive for large datasets
#   - Advantages
#       - Reduces the risk of overfitting by testing on multiple subsets of data
#       - Provides a more generalized evaluation of model performance

# Understanding the Confusion Matrix
#   - The confusion matrix is a table that summarizes the performance of a classification model by comparing predicted and actual values
#   - Structure of a Confusion Matrix
#       ---------------------------------------------------------------------
#       |                   | Predicted Positive    | Predicted Negative    |
#       ---------------------------------------------------------------------
#       | Actual Positive   | True Positive (TP)    | False Negative (FN)   |
#       | Actual Negative   | False Positive (FP)   | True Negative (TN)    |
#       ---------------------------------------------------------------------
#
#   - Key Matrics Derived
#       - True Positive Rate (TPR)
#           - Same as Recall
#       - False Positive Rate (FPR)
#           - Porportion of negatives incorrectly classified as positives
#       - Specificity
#           - Porportion of negatives correctly classified

