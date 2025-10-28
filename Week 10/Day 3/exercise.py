# Exercise: Implement max pooling and average pooling layers on feature maps and observe their effects on size and representation
import numpy as np          # For array manipulations
import matplotlib.pyplot as plt     # For visualizing feature maps
from scipy.ndimage import maximum_filter, uniform_filter        # We'll used these for max pooling and average pooling

# Create a sample feature map
feature_map = np.array([
    [1, 2, 3, 0],
    [4, 5, 6, 1],
    [7, 8, 9, 2],
    [0, 1, 2, 3]
])

# Max pooling (2x2)
max_pooled = maximum_filter(feature_map, size=2, mode='constant')

# Average pooling (2x2)
avg_pooled = uniform_filter(feature_map, size=2, mode='constant')

# Plot
""" fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(feature_map, cmap='viridis')
axes[0].set_title("Original Feature Map")
axes[1].imshow(max_pooled, cmap='viridis')
axes[1].set_title("Max Pooled Feature Map")
axes[2].imshow(avg_pooled, cmap='viridis')
axes[2].set_title("Avg Pooled Feature Map")
plt.show() """

# Perform the pooling with TensorFlow
import tensorflow as tf

# Create a sample input tensor (1x4x4x1 for batch size, height, width, channels)
input_tensor = tf.constant(feature_map.reshape(1, 4, 4, 1), dtype=tf.float32)

# Max Pooling - This is an individual layer from TensorFlow that we are creating and then passing our tensor through
max_pool = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2, padding='valid')
max_pooled_tensor = max_pool(input_tensor)

# Average Pooling - This is an individual layer from TensorFlow that we are creating and then passing our tensor through
avg_pool = tf.keras.layers.AveragePooling2D(pool_size=(2, 2), strides=2, padding='valid')
avg_pooled_tensor = avg_pool(input_tensor)

print(f"Max Pooled Tensor:\n{tf.squeeze(max_pooled_tensor).numpy()}")
print(f"Average Pooled Tensor:\n{tf.squeeze(avg_pooled_tensor).numpy()}")
print("\n\n\n")



# Perform the pooling with PyTorch
import torch
import torch.nn as nn

# Create a sample input tensor (batch_size, channels, height, width)
input_tensor_pt = torch.tensor(feature_map, dtype=torch.float32).unsqueeze(0).unsqueeze(0)

# Max Pooling
max_pool_pt = nn.MaxPool2d(kernel_size=2, stride=2)
max_pooled_tensor_pt = max_pool_pt(input_tensor_pt)

# Average Pooling
avg_pool_pt = nn.AvgPool2d(kernel_size=2, stride=2)
avg_pooled_tensor_pt = avg_pool_pt(input_tensor_pt)

print(f"Max Pooled Tensor (PT):\n{max_pooled_tensor_pt.squeeze().numpy()}")
print(f"Average Pooled Tensor (PT):\n{avg_pooled_tensor_pt.squeeze().numpy()}")


# TensorFlow Example
model_tf = tf.keras.Sequential([
    tf.keras.Input(shape=(32, 32, 3)),
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
    tf.keras.layers.AveragePooling2D((2, 2))
])

# PyTorch example
class SimpleCNN(torch.nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.pool = nn.AvgPool2d(2, 2)
    
    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = self.pool1(x)
        x = torch.relu(self.conv2(x))
        x = self.pool2(x)
        return x