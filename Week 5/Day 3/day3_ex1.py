# Exercise 1: Implement Polynomial Regression and Visualize the Fit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the California Housing Dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

# Select feature (Median Income) and Target (Median House Value)
X = df[['MedInc']]
y = df[['MedHouseVal']]

# Transform feature to polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Fit polynomial regression model
model = LinearRegression()
model.fit(X_poly, y)

# Make predictions
y_pred = model.predict(X_poly)

# Plot actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="blue", label="Actual Data", alpha=0.5)
plt.scatter(X, y_pred, color="red", label="Predicted Data", alpha=0.5)
plt.title("Polynomial Regression")
plt.xlabel("Median Income in CA")
plt.ylabel("Median House Value in CA")
plt.legend()
plt.show()

# Evaluate model performance
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error (MSE): ", mse)

