# Pooling Layers and Dimensionality Reduction

# Introduction to Pooling Layers
#   What are Pooling Layers?
#       - Used to reduce the dimensions of feature maps while retaining the most important information
#       - Help make the network computationally efficient and robust to variations in the input
#       - Types of Pooling:
#           - Max Pooling:
#               - Selects the maximum value from each region of the input feature map
#               - Captures the strongest activations (features)
#
#           - Average Pooling:
#               - Computes the average value for each region of the input feature map
#               - Provides a more generalized summary of features


# Role of Pooling in Reducing Dimensionality
#   Dimensionality Reduction
#       - Pooling reduces the spatial dimensions (height and width) of feature maps, resulting in fewer parameters and faster computations
#
#   Robustness
#       - Makes the model invariant to small translations or distortions in the input image


# Combining Convolution and Pooling Layers
#   - Pooling layers typically follow convolutional layers to downsample the feature maps
#   - This combination helps extract hierarchical features
#       - Early layers focus on simple features (e.g., edges)
#       - Deeper layers capture complex patterns (e.g., objects)