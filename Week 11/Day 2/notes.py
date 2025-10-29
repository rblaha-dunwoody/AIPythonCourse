# Understanding RNN Architecture and Backpropagation Through Time (BPTT)

# Detailed Architecture of RNN's
#   Components of an RNN
#       - Input Layer
#           - Takes sequential data as input at each time step
#
#       - Hidden Layer
#           - Maintains a "memory" of past inputs through recurrent connections. The hidden state at time t(ht) is calculated as:
#               - ht = f(Wh * ht-1 + Wx * xt + bh)
#                   - Wh = Weight matrix for recurrent connections
#                   - Wx = Weight matrix for input connections
#                   - bh = Bias term
#                   - f = Non-linear activation function (e.g., tanh, ReLU)
#
#       - Output Layer
#           - Produces output yt based on the hidden state ht
#               - yt = g(Wy * ht + by)
#                   - g = Activation function (e.g., softmax for classification)


# Backpropagation Through Time (BPTT)
#   What is BPTT?
#       - Extension of standard backpropagation to handle sequential data in RNN's
#       - It calculates gradients for each time step and propagates them backward through the sequence
#       - Steps of BPTT:
#           - Unroll the RNN across the sequence for a fixed number of time steps
#           - Compute the loss for each time step
#           - Backpropagate the errors across all time steps to update weights
#       
#       - Challenges in BPTT:
#           - Vanishing Gradient Problem
#               - Gradients diminish exponentially as they are propagated back through time
#               - Leads to difficulty in learning long-term dependencies
#           - Exploding Gradient Problem
#               - Gradients grow exponentially, causing numerical instability during training
#
#       - Solutions:
#           - Use gradient clipping to handle exploding gradients
#           - Use architectures like Long Short-Term Memory (LSTM) or Gated Recurrent Units (GRU) to mitigate the vanishing gradient problem


# Limitations of Vanilla RNN's
#   Short-Term Memory
#       - Struggle to learn dependencies in long sequences due to vanishing gradients
#
#   Sequential Computation
#       - Cannot parallelize training across time steps, making them computationally expensive
#
#   Sensitive Initialization
#       - Performance depends heavily on proper weight initialization and learning rates