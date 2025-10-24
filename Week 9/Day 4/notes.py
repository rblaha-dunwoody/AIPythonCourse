# Gradient Descent and Optimization Techniques

# Gradient Descent and Its Variants
#   What is Gradient Descent?
#       - Optimization algorithm used to minismize the loss function
#       - It does this by iteratively adjusting the model's parameters in the direction of the negative gradient
#       - Variants of Gradient Descent
#           - Batch Gradient Descent
#               - Uses the entire dataset to compute gradients at each step
#               - Pros: Accurate gradients
#               - Cons: Computationally expensive for large datasets
#
#           - Stochastic Gradient Descent (SGD)
#               - Updates parameters using one data point at a time
#               - Pros: Faster updates
#               - Cons: High variance in updates; can lead to oscillations
#
#           - Mini-batch Gradient Descent
#               - Updates parameters using a small subset (batch) of the dataset
#               - Pros: Combines the efficiency of SGD with the stability of Batch Gradient Descent


# Advanced Optimization Techniques
#   Adagrad
#       - Adapts learning rates for each parameter by scaling inversely with the sum of gradients squared
#       - Pros: Suitable for sparse data
#       - Cons: Learning rate decresses too aggressively over time
#
#   RMSprop
#       - Modifies Adagrad by using an exponentially weighted moving average of squared gradients
#       - Pros: Addresses Adagrad's aggressive learning rate decay; works well for non-convex problems
#
#   Adam (Adaptive Moment Estimation)
#       - Combines momentum and RMSprop to adapt learning rates for each parameter
#       - Pros: Works well in practice for most problems; computationally efficient


# Importance of Learning Rate and Choosing the Right Optimizer
#   Learning Rate
#       - Determines the step size for parameter updates
#       - Too High: May overshoot the minimum or cause divergence
#       - Too Low: Leads to slow convergence
#
#   Choose the Right Optimizer
#       - SGD: Works well for simple, convex problems
#       - Adam: Generally performs well across tasks
#       - RMSprop: Often preferred for RNNs and sequence-based tasks