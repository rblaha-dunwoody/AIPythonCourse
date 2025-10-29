import torch    # Used for tensor operations
import torch.nn as nn       # Used for defining neural networks
import torch.optim as optim     # Contains optimizers for training NN's
from torch.utils.data import DataLoader, TensorDataset      # Utilities for working with datasets. DataLoader for batching, TensorDataset for packaging data
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

vocab_size = 10000  # Get only top 10000 most frequent words used
max_len = 200       # Each review will be padded or truncated to 200 words

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocab_size)

X_train = pad_sequences(X_train, maxlen=max_len, padding="post")
X_test = pad_sequences(X_test, maxlen=max_len, padding="post")

train_dataset = TensorDataset(torch.tensor(X_train), torch.tensor(y_train))
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# Define RNN model
class RNNModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(RNNModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)            # Embeds words into dense vectors
        self.rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True)      # Simple RNN layer
        self.fc = nn.Linear(hidden_dim, output_dim)                         # Fully connected layer mapping the RNN output to the final binary sentiment prediction
    
    def forward(self, x):
        embedded = self.embedding(x)                        # Embed input sequences
        output, hidden = self.rnn(embedded)                 # Pass the sequences to the RNN, hidden contains the RNN's last hidden state
        return torch.sigmoid(self.fc(hidden.squeeze(0)))    # Uses the sigmoid transformation to output the hidden probabilities

model = RNNModel(vocab_size=10000, embedding_dim=128, hidden_dim=128, output_dim=1)

criterion = nn.BCELoss()        # Binary Cross Entropy Loss function
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the Model
def train_rnn(model, train_loader, criterion, optimizer, epochs=5):
    model.train()       # Put model in training mode
    for epoch in range(epochs):
        epoch_loss = 0      # Initialize cumulative loss for this epoch
        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()       # Clears the previous gradients from previous loops
            predictions = model(X_batch).squeeze(1)     # Makes the predictions
            loss = criterion(predictions, y_batch.float())      # Calculates the loss
            loss.backward()         # Compute the gradients
            optimizer.step()        # Updates the model weights
            epoch_loss += loss.item()       # Add batch loss to cumulative epoch loss
        print(f"Epoch {epoch + 1}, loss: {epoch_loss / len(train_loader):.4f}")

train_rnn(model, train_loader, criterion, optimizer)

# Evaluate RNN
def evaluate_rnn(model, X_test, y_test):
    model.eval()        # Put the model in evaluation mode
    with torch.no_grad():   # Disables gradient computation for efficiency
        predictions = model(torch.tensor(X_test)).squeeze(1)
        loss = criterion(predictions, torch.tensor(y_test).float())
        accuracy = ((predictions > 0.5) == torch.tensor(y_test).float).float().mean().item()
    print(f"Test Loss: {loss.item():.4f}, Test Accuracy: {accuracy:.4f}")

evaluate_rnn(model, X_test, y_test)