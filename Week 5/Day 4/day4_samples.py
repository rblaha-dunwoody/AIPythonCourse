# Classification Problems and Common Use Cases

# What is Classification?
#   - Supervised learning task where the objective is to predict a discrete label
#   - While Regression predicts continuous outcomes, Classification assigns categories to data points
#
#   - Types of Classification
#       - Binary Classification (True or false)
#       - Multi-Class Classification
#       - Multi-Label Classification
#
#   - Common Use Cases
#       - Healthcare | Finance | Retail | Natural Language Processing | Autonomous Systems

# Logistical Regression for Binary Classification
#
# What is Logistic Regression?
#   - A statistical method used for binary classification. It predicts the probability that a given input belongs to a specific class.
#   - Logistical Regression Model
#       - P(y = 1|x) = sigma(B0 + B1*x + B2*x^2 + ... + Bn*x^n)
#       - P(y = 1|x): Probability of the positive class
#       - sigma: sigmoid function
#
#   - Sigmoid Function
#       - Maps the output to a range between 0 and 1
#       - sigma = 1 / (1 + e^-z)
#       - If P(y = 1|x) >= 0.5, the prediction is class 1; otherwise it is class 0
#
#   - Decision Boundary
#       - The threshold (default is 0.5) used to classify instances
#       - Decision boundaries can be adjusted to optimize for precision or recall
#
#   - Interpretation of Coefficients:
#       - B0: Intercept, the baseline probability
#       - Bi: The feature xi on the log-odds of the positive class

# Sigmoid Function, Decision Boundary, and Interpretation
# 
# Sigmoid Function in Action
#   - The sigmoid function ensures outputs are interpretable as probabilities
#   - Visualization of the sigmoid function can illustrate how probabilities are mapped from raw model predictions
#
# Decision Boundary
#   - Default threshold is 0.5
#   - Adjusting the threshold can balance precision and recall depending on the use case

import numpy as np
import matplotlib.pyplot as plt

# Sigmoid Function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Generate some values
z = np.linspace(-10, 10, 100)
sigmoid_values = sigmoid(z)

# Plot
plt.plot(z, sigmoid_values)
plt.title("Sigmoid Function")
plt.xlabel("z")
plt.ylabel("Sigma(z)")
plt.grid()
plt.show()