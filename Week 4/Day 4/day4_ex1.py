# Exercise 1: Perform a hypothesis test
import numpy as np
from scipy.stats import ttest_1samp

# Sample data
data = [12, 14, 15, 16, 17, 18, 19]

# Null hypothesis: mean = 15
population_mean = 15

# Perform the t-test
t_stat, p_value = ttest_1samp(data, population_mean)
print("T-Statistic: ", t_stat)
print("P-Value: ", p_value)

# Interpret the results
alpha = 0.05
if p_value <= alpha:
    print("Reject the null hypothesis: significant different")
else:
    print("Fail to reject null hypothesis: no significant difference")
