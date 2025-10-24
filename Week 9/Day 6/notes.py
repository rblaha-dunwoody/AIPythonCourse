# Building Neural Networks with PyTorch

# Introduction to PyTorch and Its Core Components
#   What is PyTorch?
#       - Open-source deep learning framework that provides flexibility and dynamic computation for building and training machine learning models
#       - Core Components of PyTorch
#           - Tensors: Multi-dimensional arrays similar to NumPy arrays but with GPU support for accelerated computation
#           - Autograd: Automatic differentiation engine that computes gradients for optimization
#           - torch.nn Module: Provides tools to define and train neural networks with layers, activation functions, and loss functions


# Building a Neural Network in PyTorch
#   Steps:
#       - Define the Model
#           - Use torch.nn.Module to create a neural network with layers and forward propagation
# 
#       - Define the Loss Function
#           - Use built-in loss functions like Cross-Entropy Loss
#
#       - Define the Optimizer
#           - Use optimizers like SGD or Adam for weight updates


# Training, Evaluating, and Saving a Model in PyTorch
#   Training
#       - Forward pass to compute predictions
#       - Compute loss and gradients using backpropagation
#       - Update weights using an optimizer
#
#   Evaluation
#       - Test the model on unseen data and calculate metrics like accuracy
#
#   Saving and Loading
#       - Save the model's parameters using torch.save() and load them using torch.load()