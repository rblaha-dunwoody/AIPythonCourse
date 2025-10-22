# Ensemble Learning Project - Comparing Models on a Real Dataset

# Building and Evaluating Multiple Ensemble Models
#   Why Compare Ensemble Models?
#       - Excel in different scenarios
#       - Helps identify the most effective model for a specific dataset or problem
#
#   Ensemble Methods to Consider
#       - Bagging (e.g., Random Forest)
#           - Reduces variance by averaging predictions from multiple independent models
#           - Works well with high variance models like decision trees
#
#       - Boosting (e.g., Gradient Boost, XGBoost, LightGBM)
#           - Reduces bias by sequentially correcting errors from previous models
#           - Effective for complex patterns and imbalanced datasets


# Comparing Bagging and Boosting
#   Bagging
#       - Builds models independently using random subsets of data
#       - Robust against overfitting with strong base learners
#
#   Boosting
#       - Sequentially builds models, focusing on hard-to-predict samples
#       - Requires careful tuning to prevent overfitting


# Model Performance on Balanced vs Imbalanced Data
#   Challenges with Imbalanced Data
#       - Models may prioritize the majority class, leading to poor performance on the minority class
#
#   Evaluation Metrics
#       - Accuracy
#           - May not reflect true performance for imbalanced datasets
#       - F1-Score
#           - Balances precision and recall, focusing on the minority class
#       - ROC-AUC
#           - Evaluates the model's ability to distinguish between classes across thresholds
