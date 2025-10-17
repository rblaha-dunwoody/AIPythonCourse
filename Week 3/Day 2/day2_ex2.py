# Exercise 2: Create Eigenvalues and Eigenvectors
import numpy as np

A = np.array([[4, -2], [1, 1]])

eigvals, eigvec = np.linalg.eig(A)
print("EVals:\n", eigvals)
print("EVec:\n", eigvec)