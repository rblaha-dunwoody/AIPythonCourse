# Determinants and Inverse of a Matrix
import numpy as np


# Determinants
#   - Scalar value that provides information about a matrix's properties
#   - Only for square matrices
#   - det(A) = 0, the matrix A is singular
#   - det(A) != 0, A is invertible
#   - Geometric Interpretation: For a 2x2 matrix, the determinant represents the scaling factor of the area formed by its column vectors
A = np.array([[2, 3], [1, 4]])  # Det(A) = ad - bc, so 2*4 - 3*1, which is equal to 8 - 3, so 5
det = np.linalg.det(A)
print("Determinant: ", det)


# Inverse of a Matrix
#   - Denoted as A^-1
#   - Product of a matrix and its inverse is the identity matrix: A x A^-1 = I
#   - A matrix is invertible only if det(A) != 0
#   - Formula: A^-1 = 1 / det(A) * [[d, -b], [-c, a]]
inverse = np.linalg.inv(A)
print("Inverse of A: \n", inverse)


# Eigenvalues and Eigenvectors - Properties of square matrices that describe transformations
#   - If A * v = l * v, then v is the eigenvector and l is the eigenvalue

# Geometric Interpretation
#   - Eigenvectors point in the direction where the matrix transformation stretches or compresses vectors
#   - Eigenvalues indicate the factor of stretching/compression

# Properties
#   - Matrix of size n x n has n eigenvalues and eigenvectors
#   - Eigenvalues can be real or complex
#   - For a symmetric matrix, eigenvalues are always real

# Computing Eigenvalues and Eigenvectors in NumPy
eigenValues, eigenVectors = np.linalg.eig(A)
print("Eigenvalues\n", eigenValues)
print("Eigenvectors\n", eigenVectors)

B = np.array([[4, 2], [1, 1]])
eigVal, eigVec = np.linalg.eig(B)
print("EigVal: ", eigVal)
print("EigVec: \n", eigVec)


# Matrix Decomposition
#   - Process of breaking a matrix into simpler components to analyze or solve problems
#   - Singular Value Decomposition (SVD)
#       - SVD decomposes a matrix A into three matrices: A = U * E * V^T
#       - U: Left singular matrix (orthogonal matrix)
#       - E: Diagonal matrix of singular values (non-negative)
#       - V^T: Right singular vectors (orthogonal matrix)
#   - Applications of SVD: Dimensionality reduction, noise reduction, image compression
U, S, Vt = np.linalg.svd(A)
print("U:\n", U)
print("E:\n", S)
print("Vt:\n", Vt)