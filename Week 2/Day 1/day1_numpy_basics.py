import numpy as np

# ==== Creating arrays ====

arr = np.array([1, 2, 3, 4])
# print(arr)

zeroes = np.zeros((3, 3))
# print(zeroes)

ones = np.ones((2, 4))
# print(ones)

range_array = np.arange(1, 10, 3)
#print(range_array)

linspace_array = np.linspace(0, 1, 5)
# print(linspace_array)


# ==== Manipulating arrays ====
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape((2, 3))
# print(reshaped)

arr = np.array([1, 2, 3])
expanded = arr[:, np.newaxis]
# print(expanded)

# ==== Basic Operations on Arrays ====
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
#print(a + b)
#print(a * b)
#print(a / b)

arr = np.array([4, 16, 25])
#print(np.sqrt(arr))
#print(np.sum(arr))
#print(np.mean(arr))
#print(np.max(arr))


# ==== Array Indexing, Slicing and Reshaping ====
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[2])
print(arr[-1])

print(arr[1:4])
print(arr[:3])
print(arr[3:])

reshaped = arr.reshape(2, 3)
print(reshaped)



