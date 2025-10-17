# Common Probability Distributions
#   - Gaussian (Normal) Distribution
#       - Bell-shaped curve characterized by mean and standard deviation
#       - Probability Density Function (PDF)
#       - Application in ML:
#           - Common assumption in many algorithms
#           - Used in feature scaling (standardization)
#
#   - Binomial Distribution
#       - Models the number of successes in n independent Bernoulli trials
#       - Probability Mass Function (PMF)
#       - Applications in ML:
#           - Logistic regression assumes a binomial distribution for binary classification
#
#   - Poisson Distribution
#       - Models the number of events in a fixed interval
#       - Probability Mass Function (PMF)
#       - Applications in ML:
#           - Used in event modeling
#
#   - Uniform Distribution
#       - Equal probability for all outcomes in a range
#       - Probability Density Function (PDF)
#       - Applications in ML:
#           - Random initialization of weights in neural networks


# Visualizing Distributions and understanding their properties
#   - Visualization helps understand skewness, kurtosis, and outliers
#   - Skewness
#       - Measure of symmetry: Positive skew | Negative skew
#
#   - Kurtosis
#       - Measure of the "tailedness" of the distribution: High kurtosis | Low kurtosis

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, uniform
import seaborn as sns

# Gaussian Distribution (Normal)
x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x, loc=0, scale=1), label="Gaussian (u=0, s=1)")

# Binomial Distribution
n, p = 10, 0.5
x = np.arange(0, n+1)
plt.bar(x, binom.pmf(x, n, p), alpha=0.7, label="Binomial (n=10, p=0.5)")

# Poisson Distribution
lam = 3
x = np.arange(0, 10)
plt.bar(x, poisson.pmf(x, lam), alpha=0.7, label="Poisson (l = 3)")

# Uniform Distribution
x = np.random.uniform(low=0, high=10, size=1000)
sns.histplot(x, kde=True, label="Uniform", color="red")

plt.title("Probaility Distributions")
plt.legend()
plt.show()