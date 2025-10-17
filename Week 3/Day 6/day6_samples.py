# Measures of Central Tendency and Dispersion

# Central Tendency
#   - Mean: The average value of a dataset
#   - Median: The middle value when data is sorted
#   - Mode: The most frequently occurring value
""" from statistics import mode

data = [10, 20, 30, 40, 50]
mean = sum(data) / len(data)
print("Mean: ", mean)

sorted_data = sorted(data)
median = sorted_data[len(data) // 2] if len(data) % 2 != 0 else \
    (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2
print("Median: ", median)

print("Mode: ", mode(data)) """


# Dispersion
#   - Variance: The average squared deviation from the mean
""" variance = sum((x - mean) ** 2 for x in data) / len(data)
print("Variance: ", variance) """

#   - Standard Deviation: The square root of variance, indicating the spread of data
""" std_dev = variance ** 0.5
print("Standard Deviation: ", std_dev) """



# Hypothesis Testing
# Steps
#   - Formulate hypothesis (null hypothesis or alternative hypothesis)
#   - Calculate Test Statistic
#   - Determine P-Value
#   - Interpret results

# Confidence Intervals and Statistical Signficance
#   - Confidence Interval - Range of values within which the true population parameter is expected to lie
import scipy.stats as stats

data = [10, 20, 30, 40, 50]
mean = sum(data) / len(data)

variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = variance ** 0.5

sample_mean = mean
z_score = 1.96

ci = (sample_mean - z_score * (std_dev / len(data) ** 0.5), sample_mean + z_score * (std_dev / len(data) ** 0.5))
print("95% Confidence Interval: ", ci)


# Statistical Significance


