# Building CNN Architectures with Keras and TensorFlow

# Building a CNN Architecture in Keras
#   Steps to Build a CNN
#       - Convolutional Layers: Extract features from the input images
#       - Pooling Layers: Downsample feature maps to reduce dimensions and retain key features
#       - Dense (Fully Connected) Layers: Combine features for final predictions
#
#   Basic CNN Architecture
#       - Input Layer -> Convolutional Layer -> Acivation -> Pooling -> Fully Connected Layer -> Output Layer
#       - Repeat convolution and pooling layers for deeper networks


# Compiling, Training, and Evaluating a CNN
#   Steps
#       - Compile the Model
#           - Define loss, optimizer, and metrics
#           - Example loss functions
#               - Categorical Cross-Entropy: Multi-class classification
#           - Example optimizers
#               - Adam: Efficient optimization for large networks
#           - Example metrics: Accuracy
#
#       - Train the Model
#           - Use model.fit() with training data, validation data, epochs and batch size
#
#       - Evaluate the Model
#           - Use model.evaluate() with test data to calculate metrics


# Introduction to Popular CNN Architectures
#   LeNet
#       - One of the earliest CNN's for handwritten digit classification (e.g., MNIST)
#
#   AlexNet
#       - Revolutionized deep learning for image classification in 2012
#       - Introduced ReLU activation and dropout for regularizaton
#
#   VGG
#       - Uses deep networks with small filters (e.g., 3x3 3x3)
#       - Known for its simplicity and effectiveness