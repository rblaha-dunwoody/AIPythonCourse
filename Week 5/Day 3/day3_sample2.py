# Introduction to Regularization Techniques: Lasso and Ridge Regression
#
# What is Regularization?
#   - Technique used to prevent overfitting by adding a penalty term to the cost function of a regression model
#
# Types of Regularization
#   - Ridge Regression (L2 Regularization)
#       - Adds the sum of the squared coefficients to the cost function
#
#   - Lasso Regression (L1 Regularization)
#       - Adds the sum of the absolute coefficients to the cost function
#       - Encourages sparsity in the coefficients, effectively performing feature selection
#
# Key Differences
#   - Ridge shrinks coefficients but does not eliminate them
#   - Lasso can shrink some coefficients to zero, removing irrelevant features


# Avoiding Overfitting with Regularization
#   - Regularization reduces the risk of overfitting by controlling the complexity of the model
#   - The regularization parameter lambda (also called alpha in some libraries) plays a critical role:
#       - A high lambda value increases the penalty, forcing smaller coefficients and reducing overfitting
#       - A low lamdba value allows the model to fit the training data more closely, increasing the risk of overfitting

from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
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

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Ridge Regression
ridge_model = Ridge(alpha=1)
ridge_model.fit(X_train, Y_train)
ridge_predictions = ridge_model.predict(X_test)

# Lasso Regression
lasso_model = Lasso(alpha=1)
lasso_model.fit(X_train, Y_train)
lasso_predictions = lasso_model.predict(X_test)

# Evaluate Ridge
ridge_mse = mean_squared_error(Y_test, ridge_predictions)
print("Ridge Regression MSE: ", ridge_mse)

# Evaluate Lasso
lasso_mse = mean_squared_error(Y_test, lasso_predictions)
print("Lasso Regression MSE: ", lasso_mse)


