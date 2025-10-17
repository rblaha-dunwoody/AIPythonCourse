# Exercise 1: Calculate Determinant and Inverse of a Matrix
import numpy as np

A = np.array([[1, 3, 4], [4, 5, 6], [7, 8, 9]])

det = np.linalg.det(A)
inverse = np.linalg.inv(A)

print("Determinant: \n", det)
print("Inverse: \n", inverse)
