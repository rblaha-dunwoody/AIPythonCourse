# Exercise: Familiarize yourself with common datasets in deep learning and set up an environment to work with TensorFlow or PyTorch

# Step 1: Explore Common Datasets
#   - MNIST: Handwritten digit dataset (28x28 grayscale images, 10 classes)
#   - CIFAR-10: 60,000 32x32 color images across 10 classes
#   - ImageNet: Large dataset for image classification with millions of labeled images

from tensorflow.keras.datasets import mnist, cifar10
import tensorflow as tf
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# Load MNIST
(X_train_mnist, y_train_mnist), (X_test_mnist, y_test_mnist) = mnist.load_data()
print(f"MNIST Dataset: Train = {X_train_mnist.shape}, Test = {X_test_mnist.shape}")

# Load CIFAR-10
(X_train_cifar, y_train_cifar), (X_test_cifar, y_test_cifar) = cifar10.load_data()
print(f"CIFAR-10 Dataset: Train = {X_train_cifar.shape}, Test = {X_test_cifar.shape}")

# Define a basic dense layer (tensorflow)
layer = tf.keras.layers.Dense(units = 10, activation='relu')
print(f"TensorFlow Layer: {layer}")

# Define a basic dense layer (pytorch)
layer = nn.Linear(in_features=10, out_features=5)
print(f"PyTorch Layer: {layer}")

# Visualize MNIST sample
plt.imshow(X_train_mnist[0], cmap='gray')
plt.title(f"MNIST Label: {y_train_mnist[0]}")
plt.show()

# Visualize CIFAR-10 sample
plt.imshow(X_train_cifar[0])
plt.title(f"CIFAR-10 Label: {y_train_cifar[0]}")
plt.show()