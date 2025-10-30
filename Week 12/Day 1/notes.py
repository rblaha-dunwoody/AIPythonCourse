# Introduction to Attention Mechanisms

# Understanding the Limitations of RNN's and the Need for Attention
#   Challenges of RNN's
#       - Sequential processing, making parallelization difficult
#       - Long-Term Dependency Problems, due to vanishing/exploding gradients
#       - Fixed Context Vector, encoder-decoder structrure can lead to attention bottlenecks as sequences get longer
#
#   Role of Attention Mechanisms
#       - Attention overcomes these limitations by allowing the model to focus on specific parts of the input sequence dynamically --
#       -- during each output generation step
#       - Instead of relying on a single context vector, attention provides a weighted combination of all input tokens relevant --
#       -- to the current output token


# Basics of the Attention Mechanism
#   Core Components:
#       - Queries (Q)
#           - Represents the current focus of the model (e.g., the current decoder state in Seq2Seq tasks)
#       - Keys (K)
#           - Encoded representations of the input sequence
#       - Values (V)
#           - Additional information associated with the keys
#
#   Attention Mechanism:
#       - The attention score is computed using the dot product of the query and keys, 
#       -- followed by a softmax function to normalize into a probability distribution
#       - The weighted sum of the values forms the context vector
#       - Attention(Q, K, V) = softmax(Q*K^T / sqrt(dk))V


# Types of Attention
#   Self-Attention
#       - The query, key, and value all come from the same input sequence
#       - Widely used in Transformer models for learning interdependencies within a sequence
#
#   Multi-Head Attention
#       - Extends self-attention by applying multiple attention mechanisms in parallel
#       - Captures different aspects of relationships in the sequence
#           - MultiHead(Q, K, V) = Concat(head1, head2, ... , headh)W^0
#           -- where each head computes attention with different learned projections of Q, K, and V