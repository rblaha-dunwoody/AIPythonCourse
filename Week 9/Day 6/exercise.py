# Exercise: Build, train, evaluate, and save a neural network for MNIST digit classification using PyTorch
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.nn.functional as F

# Define transformation
transform = transforms.Compose([            # Combines a list of transformations to be applied sequentially
    transforms.ToTensor(),      # Converts image data into PyTorch tensors, which scales pixel values to (0, 1)
    transforms.Normalize((0.5,), (0.5,))        # Normalizes tensor data to have a mean of 0.5 and a standard deviation of 0.5 for better training stability
])

# Load Datasets
train_dataset = datasets.MNIST(root="./data", train=True, transform=transform, download=True)
test_dataset = datasets.MNIST(root="./data", train=False, transform=transform, download=True)

# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=True)

print(f"Training Data Size: {len(train_dataset)}")
print(f"Test Data Size: {len(test_dataset)}")

# Define the model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()         # Flattens a 2D image into a 1D Vector
        self.fc1 = nn.Linear(28 * 28, 128)  # Reduces the input size of 28 * 28 to an output size of 128
        self.fc2 = nn.Linear(128, 64)       # Reduces the input size of 128 to an output size of 64
        self.fc3 = nn.Linear(64, 10)        # Reduce from 64 to 10
    
    def forward(self, x):
        x = self.flatten(x)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
model = NeuralNetwork()
print(model)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training Loop
def train_model(model, train_loader, criterion, optimizer, epochs=5):
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for images, labels in train_loader:
            # Zero gradients
            optimizer.zero_grad()
            
            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)
            
            # Backward pass and optimize
            loss.backward()     # Calculates the gradients for backpropagation
            optimizer.step()    # Update the model parameters
            
            running_loss += loss.item()
        print(f"Epoch {epoch+1}, Loss: {running_loss / len(train_loader):.4f}")

train_model(model, train_loader, criterion, optimizer)

# Evaluation loop
def evaluate_model(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print(f"Test Accuracy: {100 * correct / total:.2f}%")

evaluate_model(model, test_loader)

# Save the model
torch.save(model.state_dict(), 'mnist_model.pth')

# Reload the model
loaded_model = NeuralNetwork()
loaded_model.load_state_dict(torch.load('mnist_model.pth'))

# Verify loaded model performance
evaluate_model(loaded_model, test_loader)

# (Optional) How to play with the numbers and see the differences from the updates:
# Update optimizer with a new learning rate
""" optimizer - torch.optim.Adam(model.parameters(), lr=0.0001)
train_model(model, train_loader, criterion, optimizer)
evaluate_model(model, test_loader) """