# Introduction to Hypothesis Testing
#   - Statistical method to determine if there is enough evidence in a sample to infer a conclusion about the population
#   - Null Hypothesis: Assumes no effect or difference
#   - Alternative Hypothesis: Indicates an effect or difference

# Steps
#   - Formulate a null hypothesis and alternative hypothesis
#   - Choose a significance level (alpha) - common values are 0.05 or 0.01
#   - Calculate the test statistic
#   - Determine the p-value
#   - Compare the p-value to alpha
#       - E.g., if p <= alpha, reject null hypotheses | if p > alpha, fail to reject null hypothesis

# Understanding P-Values and Signficance Levels
#   - P-Value
#       - The probability of observing results as extreme as the test statistic under Null Hypothesis
#       - Smaller p-values indicate stronger evidence against Null Hypothesis
#
#   - Significance Level (alpha)
#       - Threshold for deciding whether to reject
#       - E.g., alpha = 0.05 means a 5% risk of rejecting Null Hypothesis when it is true
#
#   - Decision Rule
#       - Reject Null Hypothesis: p <= alpha
#       - Fail to reject Null Hypothesis: p > alpha

# Types of Errors
#   - Type I Error (alpha)
#       - Incorrectly rejecting a Null Hypothesis when it is true
#       - E.g., Concluding a drug is effective when it is not
#
#   - Type II Error (beta)
#       - Failing to reject a Null Hypothesis when it is false
#       - E.g., Condlusing a drug is not effective when it is
