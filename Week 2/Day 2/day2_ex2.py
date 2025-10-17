# Exercise 2: Generate and filter a random data set
import numpy as np

# Generate original random dataset
dataset = np.random.randint(1, 51, size=(5, 5))
print("Original:\n", dataset)

# Filter values greater than 25 and replace with 0
dataset[dataset > 25] = 0
print("Modified data:\n", dataset)

# Calculate summary stats
print("Sum: ", np.sum(dataset))
print("Mean: ", np.mean(dataset))
print("Std: ", np.std(dataset))