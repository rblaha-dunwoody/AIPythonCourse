# Types of hypothesis tests

# T-Test - Test whether the means of one or more groups differ significantly
#   - One-Sample T-Test: Tests if the mean of a sample differs from a known value or population mean
#   - Two-Sample T-Test (Independent T-Test): Compares the means of two independent groups
#   - Paired Sample T-Test: Compares means of two related groups (e.g., pre-test vs. post-test)

# Example Use Cases:
#   - One-Sample: Testing if the average test score of a class differs from the national average
#   - Two-Sample: Comparing test scores between two classes
#   - Paired Sample: Comparing weight before and after a diet program

# Chi-Square Test
#   - Test for independence of goodness-of-fit in categorical data
#   - Chi-Square Test of Independence: Tests if two categorical variables are independent
#   - Example Use Case: Testing if gender is independent of preference for a product
#   - Steps:
#       - Create a contingency table
#       - Calculate expected frequencies
#       - Compute x2 statistics and p-value

from scipy.stats import chi2_contingency

# Contingency Table
data = [[50, 30], [20, 40]]

# Perform Chi-Square Test
chi2, p, dof, expected = chi2_contingency(data)
print("Chi Square: ", chi2)
print("P-Value: ", p)
print("Expected Freq: ", expected)


# ANOVA (Analysis of Variance)
#   - Purpose: Compare the means of three or more groups
#   - Hypothesis:
#       - Null: All group means are equal
#       - Alternative: At least one group mean is different
# 
#   - Example Use Case: Testing if the mean scores of students from three schools differ
from scipy.stats import f_oneway

# Data for three groups
group1 = [12, 14, 15, 16, 17]
group2 = [11, 13, 14, 15, 16]
group3 = [10, 12, 13, 14, 15]

# Perform ANOVA
f_stat, p_value = f_oneway(group1, group2, group3)
print("F-Stat: ", f_stat)
print("P-Value: ", p_value)
