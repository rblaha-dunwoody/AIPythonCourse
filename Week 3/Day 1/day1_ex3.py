# Exercise 3: Special matrices
import numpy as np

# Identity Matrix
I = np.eye(3)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("A x I:\n", np.dot(A, I))

# Diagonal and Zero Matrix
D = np.diag([1, 7, 9])
Z = np.zeros((3, 3))
print("Diagonal Matrix:\n", D)
print("Zero Matrix:\n", Z)