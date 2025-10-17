import numpy as np

# Array and scalar broadcasting
arr = np.array([1, 2, 3])
#print(arr + 10)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])
#print(matrix + vector)

# Aggregation functions
arr = np.array([[1, 2, 3], [4, 5, 6]])
#print("Sum: ", np.sum(arr))
#print("Mean: ", np.mean(arr))
#print("Max: ", np.max(arr))
#print("Min: ", np.min(arr))
#print("Std dev: ", np.std(arr))
#print("Sum along rows: ", np.sum(arr, axis=1))
#print("Sum along columns: ", np.sum(arr, axis=0))

# Boolean indexing and filtering
arr = np.array([1, 2, 3, 4, 5, 6])
evens = arr[arr % 2 == 0]
#print("Evens: ", evens)

arr[arr > 3] = 0
#print("Modified Array: ", arr)

# Setting seeds guarantees reproduceability
#np.random.seed(42)

# Random number generation and setting seeds
random_array = np.random.rand(3, 3)
print("Random array:\n", random_array)

random_integers = np.random.randint(0, 10, size=(2,3))
print("Random integers:\n", random_integers)

