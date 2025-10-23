# Forward Propagation and Activation Functions

# Understanding Forward Propagation
#   - Process by which input data flows through the layers of a neural network to produce an output
#   - Input Layer
#       - Accepts input features and passes them to the next layer
#
#   - Hidden Layers
#       - Compute weighted sums of inputs, apply biases, and pass the result through activation functions
#
#   - Output Layer
#       - Produces predictions, typically using an activation function suitable for the task
#
#   Steps in Forward Propagation
#       - Compute Weighted Sum
#           - z = W * X + b
#               - W: Weights | X: Inputs | b: Bias
# 
#       - Apply Activation Function
#           - a = sig(z)
#               - sig: Activation function
#
#       - Repeat for Each Layer
#           - Outputs of one layer become inputs to the next


# Common Activation Functions
#   Sigmoid
#       - Use Case: Binary classification in the output layer
#       - Limitation: Can suffer from vanishing gradients for large positive/negative z
#
#   Tanh (Hyperbolic Tangent)
#       - Use Case: Hidden layers where zero-centered outputs are preferred
#       - Limitation: Also prone to vanishing gradients
#
#   ReLU (Rectified Linear Unit)
#       - Use Case: Most commonly used in hidden layers due to simplicity and efficiency
#       - Limitation: Can suffer from the "dying ReLU" problem (neurons stuck at zero)
#
#   Softmax
#       - Use Case: Multi-class classification in the output layer


# Choosing Activation Function
#   |-----------------------|-----------------------------------|
#   | Layer Type            | Recommended Activation Function   |
#   |-----------------------|-----------------------------------|
#   | Hidden Layers         | ReLU or Tanh                      |
#   | Output (Binary)       | Sigmoid                           |
#   | Output (Multi-Class)  | Softmax                           |
#   | Output (Regression)   | None or Linear                    |
#   |-----------------------|-----------------------------------|