# Project: Build, train, and optimize RNN, LSTM, or GRU models for Sentiment Analysis
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense, LSTM, GRU

# Load dataset
vocab_size = 10000
max_len = 100
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocab_size)

X_train = pad_sequences(X_train, maxlen=max_len, padding="post")
X_test = pad_sequences(X_test, maxlen=max_len, padding="post")

print(f"Training data shape: {X_train.shape}, {y_train.shape}")
print(f"Test data shape: {X_test.shape}, {y_test.shape}")

# Define the RNN model
rnn_model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=128),
    SimpleRNN(128, activation='tanh'),
    Dense(1, activation='sigmoid')
])

# Compile the model
rnn_model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Display the model summary
rnn_model.summary()

# Define the LSTM model
lstm_model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=128),
    LSTM(128, activation='tanh'),
    Dense(1, activation='sigmoid')
])

# Compile the model
lstm_model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Display the model summary
lstm_model.summary()

# Define the GRU model
gru_model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=128),
    GRU(128, activation='tanh'),
    Dense(1, activation='sigmoid')
])

# Compile the model
gru_model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Display the model summary
gru_model.summary()

# Train RNN Model
history_rnn = rnn_model.fit(X_train, y_train, validation_split=0.2, epochs=5, batch_size=64, verbose=1)

# Train LSTM Model
history_lstm = lstm_model.fit(X_train, y_train, validation_split=0.2, epochs=5, batch_size=64, verbose=1)
                            
# Train GRU Model
history_gru = gru_model.fit(X_train, y_train, validation_split=0.2, epochs=5, batch_size=64, verbose=1)

# Evaluate models
loss_rnn, accuracy_rnn = rnn_model.evaluate(X_test, y_test, verbose=0)
loss_lstm, accuracy_lstm = lstm_model.evaluate(X_test, y_test, verbose=0)
loss_gru, accuracy_gru = gru_model.evaluate(X_test, y_test, verbose=0)

print(f"RNN Accuracy: {accuracy_rnn:.4f}")
print(f"LSTM Accuracy: {accuracy_lstm:.4f}")
print(f"GRU Accuracy: {accuracy_gru:.4f}")

import matplotlib.pyplot as plt

# Plot training accuracy
plt.plot(history_rnn.history['accuracy'], label="RNN Training Accuracy")
plt.plot(history_lstm.history['accuracy'], label="LSTM Training Accuracy")
plt.plot(history_gru.history['accuracy'], label="GRU Training Accuracy")
plt.title("Training Accuracy Comparison")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()