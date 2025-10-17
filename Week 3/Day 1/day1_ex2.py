# Exercise 2: Multiply matrix by a vector
import numpy as np

# Create Matrix and Vector
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([1, 0, -1])

# Matrix-Vector Multiplication
result = np.dot(M, v)
print("Matrix-Vector Multiplication:\n", result)