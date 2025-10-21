# Creating and Transforming Features

# Feature Creation
#   What is Feature Creation?
#       - Feature Creation involves deriving new, meaningful features from existing ones to enhance a model's ability to capture important patterns in data
#       - Examples:
#           - Date-Time Features
#           - Interaction Features
#           - Aggregations
#       - Importance
#           - Adds domain knowledge to the dataset
#           - Captures hidden patterns and trends not evident in the original features


# Transforming Features
#   What is Feature Transformation?
#       - Feature transformation modifies existing features to better suit the learning algorithm
#       - Common Transformations
#           - Logarithmic Transformation
#               - Reduces skewness in highly skewed distributions
#           - Square Root Transformation
#               - Moderately reduces skewness, often used for count data
#           - Polynomial Transformation
#               - Adds higher-order terms (x^2, x^3, etc) to capture non-linear relationships
#       - Importance
#           - Enhances the model's ability to fit non-linear relationships
#           - Makes distributions more normal-like, aiding algorithms that assume normality


# Importance of Feature Transformation in Non-Linear Relationships
#   Transformations allow linear models to handle non-linear relationships
#       - For example:
#           - Polynomial transformations enable linear regression to model quadratic patterns
#           - Logarithmic transformations stabilize variance and handle skewness
#
#   By transforming features, models become more robust and capable of capturing complex patterns in data

