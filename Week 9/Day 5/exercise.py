# Exercise: Build, train, evaluate and save a simple neural network to classify digits from the MNIST dataset
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize data
X_train = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
X_test = X_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

# One-hot encode labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

print(f"Training Data Shape: {X_train.shape}")
print(f"Test Data Shape: {X_test.shape}")

# Build the model
model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),     # Each filter is a 3x3 matrix, relu sets negative values to 0 to add non-linearity, we specify the shape of the input image as well
    MaxPooling2D(2, 2),     # Reduces each 2x2 block in the input to a single maximum value, which will reduce the spatial dimensions by half
    Flatten(),      # Converts the 2D feature map into a 1D vector
    Dense(128, activation="relu"),      # Adds a dense layer with 128 neurons and a relu activation function
    Dropout(0.5),       # Adds a dropout layer to randomly drop neurons during training to reduce overfitting
    Dense(10, activation="softmax")     # Adds a dense layer with 10 neurons and a softmax activation function
])

# Display model architecture
model.summary()     # Display summary information about the model, including how many params are trainable/non-trainable/etc

# Compile the model
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=['accuracy']
)

# Train the model
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2
)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy:.4f}")

# Save the model
model.save('mnist_classifier.h5')

# Load the model
from tensorflow.keras.models import load_model
loaded_model = load_model('mnist_classifier.h5')

# Verify loaded model's performance
loss, accuracy = loaded_model.evaluate(X_test, y_test)
print(f"Loaded Model Accuracy: {accuracy:.4f}")
