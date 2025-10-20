# Exercise 1: Use correlation and mutual information to select important features from a dataset
from sklearn.datasets import load_diabetes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression

# Load the dataset
data = load_diabetes()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Display dataset Information
""" print(df.head())
print(df.info()) """

# Calculate the Correlation Matrix
correlation_matrix = df.corr()

# Plot the heatmap
""" plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show() """

# Select features with high correlation to the target
correlation_features = correlation_matrix['target'].sort_values(ascending=False)
""" print("Features Most Correlated with target are: ")
print(correlation_features) """

# Separate features and target
X = df.drop(columns=['target'])
y = df['target']

# Calculate mutual information
mutual_info = mutual_info_regression(X, y)

# Create a DataFrame for better visualization
mi_df = pd.DataFrame({'Feature': X.columns, "Mutual Information": mutual_info})
mi_df = mi_df.sort_values(by="Mutual Information", ascending=False)

""" print("Mutual Information Scores:")
print(mi_df) """

# Exercise 2: Apply a tree-based model (e.g., Random Forest) to identify the most important features
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Train a Random Forest Model
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

# Get feature importance
feature_importance = model.feature_importances_
importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importance})
importance_df = importance_df.sort_values(by="Importance", ascending=False)

print("Feature Importance from Random Forest: ")
print(importance_df)

# Plot feature importance
plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'], importance_df['Importance'])
plt.gca().invert_yaxis()
plt.title("Feature Importance from Random Forest")
plt.show()


