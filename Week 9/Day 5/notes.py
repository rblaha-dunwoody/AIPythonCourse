# Building Neural Networks with TensorFlow and Keras

# Introduction to TensorFlow and Keras
#   What is TensorFlow?
#       - Open-source library for numerical computation and machine learning
#       - Provides tools for building and training deep learning models
#
#   What is Keras?
#       - High-level API integrated with TensorFlow that simplifies the process of creating and training neural networks
#       - Key Features of Keras
#           - User-Friendly: Intuitive syntax for rapid prototyping
#           - Modular: Building blocks for defining layers, optimizers and loss functions
#           - Integration: Compatible with TensorFlow for scalable deep learning tasks


# Defining Layers, Models, and Compiling Networks in Keras
#   Defining Layers
#       - Layers are the building blocks of neural networks
#       - Common types include:
#           - Dense (Fully Connected) Layers
#               - Each neuron is connected to every neuron in the previous layer
#           - Dropout Layers
#               - Randomly drops connections to prevent overfitting
#           - Activation Layers
#               - Acpply activation functions to introduce non-linearity
#
#   Building a Model
#       - Keras supports two primary ways to define models
#           - Sequential API: A linear stack of layers
#           - Functional API: More flexible, allows for complex architectures
#
#   Compiling a Model
#       - Specifies:
#           - Optimizer: Alorithm to update weights
#           - Loss Function: Metric to minimize during training
#           - Metrics: Additional performance measures


# Training, Evaluating and Saving a Model
#   Training
#       - Fit the model using model.fit()
#   
#   Evaluation
#       - Test the model on unseen data using model.evaluate()
#
#   Saving and Loading
#       - Save a trained model using model.save() and reload it with keras.models.load_model()