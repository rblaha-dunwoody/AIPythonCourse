# Positional Encoding and Feed-Forward Networks

# Understanding the Role of Positional Encoding in Transformers
#   Why Positional Encoding?
#       - Unlike RNN's, Transformers do not process sequences sequentially
#       - They process all tokens in parallel
#       - Transformers lack inherent knowledge of token positions, which is crucial for tasks like translation or sequnce modeling
#
#   What is Positional Encoding?
#       - Positional encoding itroduces information about the order of tokens in a sequence
#       - It allows the model to differentiate between identical tokens in different positions


# Mathematical Foundation and Implementation of Positional Encoding
#   Sinusoidal Positional Encoding
#       - Encodes positional information using sine and cosine functions
#       - Formula for positional encoding:
#           - PE(pos, 2i) = sin(pos / (10000)^(2i/d))
#           - PE(pos, 2i + 1) = cos(pos / (10000)&(2i/d))
#               - where 
#                   - pos is the position of the token in the sequence
#                   - i is the index of the embedding dimension
#                   - d is total number of embedding dimensions
#
#   Why Use Sinusoidal Functions?
#       - Provides unique encoding for each position
#       - Allows generalization to longer sequences not seen during training


# The Feed-Forward Network
#   What is a Feed-Forward Network (FFN)?
#       - FFN's a fully connected layers applied to each token independently and identically within a Transformer layer
#       - Adds non-linear transformation to the output of the attention mechanism
#
#   Role in Transformers
#       - Captures token-specific transformations
#       - Enhances representational capacity
#
#   Structure
#       - Linear transformation
#       - Non-linear activation (e.g., ReLU)
#       - Another linear transformation
#           FFN(x) = ReLU(xW1 + b1)W2 + b2