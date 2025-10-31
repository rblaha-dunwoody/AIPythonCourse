# Introduction to Transformers Architecture

# Overview of Transformer Architecture
#   What is a Transformer?
#       - A Neural Network architecture introduced in the paper "Attention is All You Need"
#       - It relies entirely on the attention mechanism to process sequential data without using recurrence or convolution
#       - Transformative for NLP tasks like translation, summarization, and text generation
#
#   Components of the Transformer
#       - Encoder
#           - Processes the input sequence and generates a contextualized representation
#           - Consists of multiple identical layers, each with:
#               - Self-Attention Mechanism: Captures dependencies between all input tokens
#               - Feed-Forward Neural Network (FFNN): Processes the attention outputs
#
#       - Decoder
#           - Generates the output sequence one token at a time
#           - Consists of multiple identical layers, each with:
#               - Masked Self-Attention Mechanism: Prevents the decoder from attending to future tokens
#               - Encoder-Decoder Attention: Attends to encoder outputs
#               - Feed-Forward Neural Network
#
#       - Workflow: Input sequence -> Encoder -> Context vectors -> Decoder -> Output Sequence


# Detailed Breakdown of the Transformer Model Layers
#   Self-Attention Layer
#       - Captures relationships between all tokens in the input sequence
#       - Computes the importance of each token to all other tokens
#
#   Positional Encoding
#       - Since Transformers lack recurrence, positional encoding injects information about the token order into the model
#
#   Feed-Forward Neural Network
#       - Applies a position-wise FFNN to the outputs of the attention layer
#       - Non-linear transformation enhances the representation
#
#   Layer Normalization
#       - Stabilizes training by normalizing inputs within each layer
#
#   Multi-Head Attention
#       - Combines multiple self-attention mechanisms to learn various aspects of relationships within the sequence


# Key Differences Between Transformers and RNN's
#
#   |---------------------------|-----------------------------------------------|-----------------------------------------------|
#   | Aspect                    | Transformers                                  | RNN's                                         |
#   |---------------------------|-----------------------------------------------|-----------------------------------------------|
#   | Parallelization           | Fully parallelizable; faster training         | Sequential processing limits parallelization  |
#   | Long-Term Dependencies    | Handles long dependencies via attention       | Struggles with long dependencies              |
#   | Position Information      | Uses positional encodings                     | Implicitly encodes position                   |
#   | Architecture              | Built on attention mechanisms; no recurrence  | Sequential processing through hidden states   |
#   |---------------------------|-----------------------------------------------|-----------------------------------------------|