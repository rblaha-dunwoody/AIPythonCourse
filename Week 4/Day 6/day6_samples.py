# Correlation and Regression Analysis

# What is Correlation?
#   - Measures the strength and direction of the relationship between two variables
#   - Values range from -1 to 1, with 0 indicating no correlation
#
# Types of Correlation:
#   - Pearson Correlation Coefficient: r
#   - Spearman Correlation Coefficient: rho

import numpy as np
from scipy.stats import pearsonr, spearmanr

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Pearson Correlation
r, _ = pearsonr(x, y)
print("Pearson Correlation Coefficient: ", r)

# Spearman Correlation
rho, _ = spearmanr(x, y)
print("Spearman Correlation Coefficient: ", rho)


# Linear Regression Basics
#   - Method to model the relationship between a dependent variable (y) and one or more independent variables (x)
#   - Formula for simple linear regression: ...
#
# Key Metrics:
#   - Slope (B1)
#       - Indicates the magnitude and direction of the relationship
#   - Intercept(B0)
#       - Starting point of the regression line
#   - R-Squared (R2)
#       - Closer to 1 indicates a better fit

from sklearn.linear_model import LinearRegression
import numpy as np

# Sample Data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 8, 10])

# Fit Linear Regression
model = LinearRegression()
model.fit(x, y)

print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)
print("R-Squared: ", model.score(x, y))



