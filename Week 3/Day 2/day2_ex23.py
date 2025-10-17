# Exercise 3: Perform Singular Decomposition Values
import numpy as np

# Deconstruct
A = np.array([[3, 1, 1], [-1, 3, 1], [1, 1, 3]])
U, S, Vt = np.linalg.svd(A)

print("U: \n", U)
print("Singular values: \n", S)
print("V Transpose: \n", Vt)

# Reconstruct
Sigma = np.zeros((3, 3))
np.fill_diagonal(Sigma, S)
reconstructed = U @ Sigma @ Vt
print("Reconstructed Matrix:\n", reconstructed)
