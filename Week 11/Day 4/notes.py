# Gated Recurrent Units (GRU's)

# Introduction to Gated Recurrent Units
#   What Are GRU's?
#       - Simplified variant of Long Short-Term Memory (LSTM) networks
#       - Designed to retain long-term dependencies while reducing computational complexity by having fewer parameters
#       - Key Features of GRU's:
#           - Simpler Architecture
#               - GRU's have two gates (update and reset) compared to LSTMs' three gates (input, forget, output)
#           - Efficiency
#               - Fewer parameters make GRU's computationally faster and less prone to overfitting on smaller datasets
#           - Retains Performance
#               - Comparable to LSTM's in terms of capturing sequential dependencies


# GRU Cell Structure: Update and Reset Gates
#   Update Gate
#       - Determines how much of the previous hidden state to retain and how much to update with the new information
#
#   Reset Gate
#       - Controls how much of the past information to forget when combining with new input
#
#   Hidden State Update
#       - Combines the new information and the past hidden state based on the reset and update gates


# When to Use GRU's vs. LSTM's
#   |-------------------|---------------------------------------|-----------------------------------|
#   | Feature           | LSTM                                  | GRU                               |
#   |-------------------|---------------------------------------|-----------------------------------|
#   | Gates             | Input, Forget, Output                 | Update, Reset                     |
#   | Parameters        | More                                  | Fewer                             |
#   | Performance       | Better for complex, longer sequences  | Comparable for shorter sequences  |
#   | Training Speed    | Slower due to complexity              | Faster due to simpler structure   |
#   | Use Cases         | NLP, speech recognition               | Time-series data, small datasets  |
#   |-------------------|---------------------------------------|-----------------------------------|