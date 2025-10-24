# Loss Functoins and Backpropagation

# Understanding Loss Functions
#   What are Loss Functions?
#       - Quantify the difference between the predicted output of a model and the actual target value
#       - Guide the training process by providing a metric to minimize during optimization
#       - Role in Neural Networks
#           - Error Measurement
#               - Evaluate the accuracy of predictions
#           - Feedback for Optimization
#               - Provide gradients for weight updates via backpropagation
#
#   Common Types of Loss Functions
#       - Mean Squared Error (MSE)
#           - Commonly used for regression tasks
#           - Penalizes larger errors more heavily than smaller ones
#
#       - Cross-Entropy Loss
#           - Used for classification tasks
#           - Measures the difference between true labels and predicted probabilities


# Introduction to Backpropagation
#   What is Backpropagation?
#       - Process of computing gradients for each weight and bias in a neural network
#       - This is for enabling optimization algorithms (like gradient descent) to minimize the loss function
#       - Steps in Backpropagation
#           - Forward Pass: Compute the output and loss for the current weights
#           - Backward Pass: Calculate the gradient of the loss with respect to each parameter
#           - Weight Update: Use the gradients to update parameters
#
#       - Key Concepts
#           - Gradient: The rate of change of the loss with respect to a parameter
#           - Gradient Descent: An optimization algorithm that minimizes the loss by updating parameters in the direction of the negative gradient
