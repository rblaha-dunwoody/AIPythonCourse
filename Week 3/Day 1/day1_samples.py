import numpy as np

# ==== Matrix Operations ====
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Addition and subtraction
print("Addition: \n", A + B)
print("Subtraction: \n", A - B)

# Scalar multiplication
C = 2 * A
print("Scalar Multiplication: \n", C)

# Matrix multiplication (requires number of columns in the first matrix must be equal to the number if rows in the second matrix)
result = np.dot(A, B)
print("Matrix multiplication:\n", result)



# ==== Special Matrices ====

# Identity Matrix: I * A = A
I = np.eye(3)
print("Identity Matrix:\n", I)

# Zero Matrix: All elements are zero
Z = np.zeros((2, 3))
print("Zero Matrix:\n", Z)

# Diagonal Matrix: All elements except the diagonals are 0
D = np.diag([1, 2, 3])
print("Diagonal Matrix:\n", D)
