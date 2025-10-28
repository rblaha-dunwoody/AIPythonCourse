# Excercise: Visualize images in a dataset, explore their pixel data, and set up an environment for building CNN's using TensorFlow or PyTorch
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
import numpy as np

# Load Dataset
transform = transforms.ToTensor()       # Defines a transformation to convert images from the dataset to PyTorch tensors
train_dataset = datasets.CIFAR10(root="./data", train=True, transform=transform, download=True)     # Loads CIFAR10 dataset

# Visualize sample images
""" fig, axes = plt.subplots(1, 5, figsize=(12, 3))     # Creates a figure with 1 row and 5 columns of subplots for displaying images
for i in range(5):      # Loop through first 5 images in training data set, and for each image, retrieves the image and image data
    image, label = train_dataset[i]
    axes[i].imshow(image.permute(1, 2, 0))  # Diplay image (imshow) while calling the permute method to restructure the dimensions from (channels, height, width) to (height, width, channels)
    axes[i].axis('off') # Hide the axis for a cleaner display of the image
    axes[i].set_title(f"Label: {label}")    # Set title of each subplot to the title of the image
plt.show() """

# Display pixel values for the first image
""" image, label = train_dataset[0]
print(f"Label: {label}")
print(f"Image Shape: {image.shape}")
print("Pixel Values:")
print(image) """

import tensorflow as tf

# Define a simple CNN model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),   # Reduce the dimensions of previous input
    tf.keras.layers.Flatten(),       # Flattens 2D feature maps into a 1D Vector for fully connected layers
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

print("Tensorflow CNN Model is ready")

import torch.nn as nn

# Define a simple CNN model
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, activation="relu")
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(32 * 15 * 15, 128)     # Converts input size to output size
        self.fc2 = nn.Linear(128, 10)       # Once again converts input size to output size
    
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = x.view(-1, 32 * 15 * 15)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)

print("PyTorch CNN model ready")


