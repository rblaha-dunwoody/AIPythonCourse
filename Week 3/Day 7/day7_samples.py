# Applying Linear Algebra, Calculus and Statistics

# Linear Algebra
#   - Mathematical model: y^ = X * theta
#   - X: Feature matrix (with bias term) | theta: Parameters (weights and bias) | y^: Predicated values

# Calculus
#   - Optimization of theta involves minimizing the loss function

# Statistics
#   - Metrics like Mean Squared Error (MSE) are R^2 are used to evaluate model performance

# Using Gradient Descent for Paramter Optimization
#   - Gradient Descent Algorithm
#       - Iteratively update theta
#       - alpha is the learning rate
#  
#   - Key Steps
#       - Initialize parameters (theta)
#       - Compute gradients (vJ)
#       - Update parameters using the gradient descent rule

# Evaluating the Model using Statistical Metrics
#   - Mean Squared Error (MSE)
#       - Measures the average squared error
#
#   - R-squared (R^2)
#       - Measures how well the regression line explains the variance in the data

# Task 1: Implement the mathematical formula for Linear Regression
import numpy as np

def predict(X, theta):
    return np.dot(X, theta)

# Task 2: Use Gradient Descent to Optimize the Model Parameters
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        gradients = (1/m) * np.dot(X.T, (np.dot(X, theta) - y))
        theta -= learning_rate * gradients
    return theta

# Task 3: Calculate Evaluation Metrics
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1 - (ss_res / ss_tot)


# Generate synthetic data
np.random.rand(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add bias term to the feature metrics
X_b = np.c_[np.ones((100, 1)), X]

# Initialize parameters
theta = np.random.randn(2, 1)
learning_rate = 0.1
iterations = 1000

# Perform gradient descent
theta_optimized = gradient_descent(X_b, y, theta, learning_rate, iterations)

# Predictions and evaluations
y_pred = predict(X_b, theta_optimized)
mse = mean_squared_error(y, y_pred)
r2 = r_squared(y, y_pred)

print("Optimized Parameters (Theta): ", theta_optimized)
print("MSE: ", mse)
print("R2: ", r2)
