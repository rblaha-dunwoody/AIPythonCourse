# Self-Attention and Multi-Head Attention in Transformers

# What is Self-Attention?
#   - Allows a model to dynamically focus on different parts of an input sequence when encoding a token
#   - It captures dependencies across all tokens in a sequence, enabling context-aware representations
#   - Steps in Self-Attention:
#       - Compute Attention Scores:
#           - Calculate dot products between the query (Q) and key (K) vectors for all tokens
#           - Scale by the square root of the key dimension (dk) to stabilize gradients
#           - Apply the softmax function to convert scores into probabilities
#
#       - Weight Values
#           - Use the attention scores to compute a weighted sum of value (V) vectors
#
#       - Attention(Q, K, V) = softmax(Q*K^T/sqrt(dk))*V


# Multi-Head Attention
#   What is Multi-Head Attention?
#       - Applies several attention mechanisms in parallel
#       - Each attention "head" focuses on different aspects of the sequence
#
#   Steps:
#       - Linear Projections
#           - Project Q, K, and V into multiple subspaces using learned weight matrices
#       - Apply Self-Attention
#           - Perform self-attention for each head independently
#       - Concatenate Outputs
#           - Combine outputs from all heads
#       - Final Linear Projection
#           - Project concatenated outputs back into the origianl dimension
#               - MultiHead(Q, K, V) = Concat(head1, head2, ... , headh) * W0


# Applications of Multi-Head Attention in NLP
#   Machine Translation
#       - Captures dependencies across languages for better translations
#
#   Text Summarization
#       - Identifies key phrases to generate concise summaries
#
#   Named Entity Recognition
#       - Focuses on contextual clues to detect entities in text