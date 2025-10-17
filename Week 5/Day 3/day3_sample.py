# Polynomial Regression for Modeling Non-Linear Relationships

# Polynomial Regression is an extension of linear regression that models non-linear relationships by introducing higher-order terms of the input features
#   - In a typical linear regression: y = B0 + B1*x + e
#   - In a polynomial regression, we extend this to include higher-degree terms: y = B0 + B1*x + B2*x^2 + ... + Bn*x^n + e
#   - The inclusion of higher-order terms allows the model to capture non-linear patterns in the data
#
# Steps:
#   - Feature Transformation
#       - Create polynomial features from the original input data
#       - Example: x -> [x, x^2, x^3]
#   - Model Training
#       - Perform linear regression on the transformed features
#   - Evaluation
#       - Assess the model's ability to capture the data's non-linear structure
#
# Advantages:
#   - Captures non-linear relationships effectively
#
# Limitations:
#   - Prone to overfitting with high degree polynomials
#   - May require regularization to avoid overfitting
#
# Example Use Case: Predicting growth patterns in biological systems where relationships are non-linear

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate synthetic data
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 3 * X**2 + 2 * X + np.random.randn(100, 1) * 5

# Transform features to polynomial
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)

# Fit Polynomial Regression
model = LinearRegression()
model.fit(X_poly, y)
y_pred = model.predict(X_poly)

# Plot results
plt.scatter(X, y, color="blue", label="Actual Data")
plt.scatter(X, y_pred, color="red", label="Predicated Data")
plt.title("Polynomial Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# Evaluate Model
mse = mean_squared_error(y, y_pred)
print("Mean Square Error (MSE): ", mse)


