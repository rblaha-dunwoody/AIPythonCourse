# Grid Search and Random Search

# Introduction to Grid Search and Random Search
#   What is Grid Search?
#       - Method of hyperparameter tuning that systematically evaluates all possible combinations of hyperparameter values within a specified grid
#       - How it Works:
#           - Define a range of values for each hyperparameter
#           - Train and evaluate the model on each combination of hyperparameter values
#           - Select the combination that yields the best performance
#
#   What is Random Search?
#       - Alternative method where hyperparameter combinations are sampled randomly from the specified ranges
#       - How it Works:
#           - Define ranges or distributions for each hyperparameter
#           - Randomly sample a specified number of combinations
#           - Train and evaluate the model for each sampled combination


# Pros and Cons of Each Method
#   |-------------------|-------------------------------------------|-----------------------------------------------|
#   | Feature           | Grid Search                               | Random Search                                 |
#   |-------------------|-------------------------------------------|-----------------------------------------------|
#   | Exhaustiveness    | Evaluates all combinations                | Randomly samples combinations                 |
#   | Time Efficiency   | Computationally expensive for large grids | Faster for large parameter spaces             |
#   | Exploration       | Limited to predefined grid                | Explores more diverse ranges                  |
#   | Best Use Case     | Small parameter spaces                    | Large parameter spaces with time constraints  |
#   |-------------------|-------------------------------------------|-----------------------------------------------|


# Practical Guidance on Choosing Search Ranges
#   Start with Broad Ranges
#       - Use Random Search to explore large parameter spaces and identify promising ranges
#
#   Refine with Grid Search
#       - Narrow the search space based on Random Search results and perform exhaustive Grid Search for fine-tuning
#
#   Understand Model Sensitivity
#       - Some hyperparameters (e.g., learning rate) require fine granularity, while others (e.g., number of trees) can have coarser steps

