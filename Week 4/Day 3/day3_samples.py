# Introduction to Statistical Inference
#   - The process of making conclusions about a population based on sample data
#   - Population vs Sample
#   - Goal - Estimate population parameters and assess the reliability of these estimates

# Point estimation and interval estimation
#   - Point estimation: Single value estimate of a population parameter
#   - Interval estimation: Provides a range of values within which the population parameter is likely to lie
#   - Confidence Interval

# Constructing Confidence Intervals:
#   - For means: When the population standard deviation is unknown...
#   - For proportions: ...

import numpy as np
from scipy.stats import norm, t

# Sample data
data = [12, 14, 15, 16, 17, 18, 19]

# Calculate mean and standard deviation
mean = np.mean(data)
std = np.std(data, ddof=1)

# 95% Confidence Interval (using t-distribution)
n = len(data)
t_value = t.ppf(0.975, df=n-1)
margin_of_error = t_value * (std / np.sqrt(n))
ci = (mean - margin_of_error, mean + margin_of_error)
print("95% Confidence Interval: ", ci)
