# Exercise: Set up a transfer learning environment, load a pre-trained model, and explore its architecture and layers
import tensorflow as tf
from tensorflow.keras.applications import ResNet50

# Load a pre-trained ResNet50 model
model = ResNet50(weights="imagenet")

# Display the model's architecture
#model.summary()

# Access specific layers
""" for i, layer in enumerate(model.layers):
    print(f"Layer {i}: {layer.name}, Trainable {layer.trainable}") """

for layer in model.layers[:-10]:
    layer.trainable = False