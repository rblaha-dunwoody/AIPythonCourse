# Basic probability concepts
#   - Sample Space: The set of all possible outcomes of a random experiment
#   - Events: A subset of the sample space
#   - Conditional Probability: The probability of an event A occurring, given that B has occurred
#   - Independence: Two events A and B are independent if P(A&B) = P(A) . P(B)

from itertools import product

# Sample space of a dice roll
sample_space = list(range(1, 7))

# Probability of rolling an even number
even_numbers = [2, 4, 6]
P_even = len(even_numbers) / len(sample_space)
print("P(Even): ", P_even)


# Random variables
#   - Maps outcomes of a random experiment to numerical values
#   - Types: Discrete|Continuous
#
# Probability Mass Function (PMF)
#   - Probability distribution of a discrete random variable
#
# Probability Density Function (PDF)
#   - Probability distribution of a continuous random variable

# Expectation, Variables, and Standard Deviation
#   - Expectation (E[X]) - Weighted average of a random variable's possible values
#   - Variance (Var[X]) - Measures the spread of a random variable
#   - Standard Deviation - Square root of variance

import numpy as np

# Random variable: dice roll
outcomes = np.array([1, 2, 3, 4, 5, 6])
probabilities = np.array([1/6] * 6)

# Expectation
expectation = np.sum(outcomes * probabilities)
print("Expectation (Mean): ", expectation)

# Variants and Standard Deviation
variance = np.sum((outcomes - expectation)**2 * probabilities)
std_dev = np.sqrt(variance)
print("Variance: ", variance)
print("Std Dev: ", std_dev)
