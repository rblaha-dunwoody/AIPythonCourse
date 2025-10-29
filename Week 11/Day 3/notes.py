# Long Short-Term Memory (LSTM) Networks

# Introduction to LSTM's and How They Address RNN Limitations
#   What Are LSTM's?
#       - Type of Recurrent Neural Network (RNN) specifically designed to handle long-term dependencies
#       - LSTM's mitigate the vanishing gradient problem by using specialized gates to manage the flow of information
#       - Key Features of LSTM's
#           - Memory Cells
#               - Maintain a long-term memory state across sequences
#           - Gates Mechanism
#               - Regulates how much information to keep, update, or forget at each time step
#           - Effective for Long Sequences
#               - Handles sequential data with dependencies across many time steps
#
#   Advantages Over Vanilla RNN's
#       - Retains long-term dependencies
#       - Prevents gradient-related issues during training
#       - Outperforms RNN's on tasks like language modeling, speech recognition, and time-series forecasting


# LSTM Cell Structure: Input, Forget, and Output Gates
#   Forget Gate
#       - Decides what information to discard from the cell state
#           - ft = sig(Wf .dot[ht-1, xt] + bf)
#               - Wf: Weight matrix for the forget gate
#               - ft: Forget gate output
#               - xt: Input
#               - ht-1: Previous hidden state
#
#   Input Gate
#       - Decides what new information to add to the cell state
#           - it = sig(Wi * [ht-1, xt] + bi)
#               - sig: Sigmoid activation function
#               - Wi: Weight matrix for the input game
#               - ht-1: Hidden state from the previous time step
#               - xt: Current input
#               - bi: Bias for the current input gate
#
#   Cell State Update
#       - Combines the forget gate and input gate results to update the cell state
#           - Ct = ft .dot(Ct-1) + it .dot(Ct)
#
#   Output Gate
#       - Decide what information to output at each time step
#           - ot = sig(Wo * [ht-1, xt] + bo)
#               - Wo: Weight matrix for the output gate
#               - bo: Bias for the output gate


# Applications of LSTM's
#   Natural Language Processing (NLP)
#       -  Sentiment analysis, machine translation, text generation
#
#   Time-Series Forecasting
#       - Predicting stock prices, weather patters, or sales trends
#
#   Speech Recognition
#       - Converting spoken words into text
#
#   Anomaly Detection
#       - Identifying unusual patterns in sequential data