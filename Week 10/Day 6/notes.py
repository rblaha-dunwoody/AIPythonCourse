# Regularization and Data Augmentation for CNN's

# Overfitting in CNN's and Methods to Prevent It
#   What is Overfitting?
#       - Occurs when a model performs well on the training data but fails to generalize to unseen data
#       - In CNN's, overfitting is common due to the large number of parameters in deep networks
#       - Methods to Prevent Overfitting
#           - Dropout
#               - Randomly sets a fraction of neurons to zero during training
#               - Prevents co-adaptation of neurons
#               - Controlled by a dropout rate (e.g., 0.5)
#
#           - Batch Normalization
#               - Normalizes the input of each layer to stabilize training
#               - Reduces internal covariate shift and allows higher learning rates
#
#           - Data Augmentation
#               - Increases dataset size artificially by applying transformations to images
#               - Examples: rotation, flipping, scalilng, cropping, brightness adjustment


# Introduction to Data Augmentation Techniques
#   Common Techniques
#       - Rotation
#           - Rotates the image by a specified angle (e.g., -30 degrees to 30 degrees)
#       - Flipping
#           - Horizontally or vertically flips the image
#       - Scaling
#           - Resizes the image by zooming in or out
#       - Cropping
#           - Extracts random portions of the image


# Implementing Regularization and Data Augmentation in CNN Training
#   Why Use Both?
#       - Regularization reduces the complexity of the model
#       - Data augmentation increases the diversity of the training data, improving generalization