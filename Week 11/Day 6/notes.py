# Sequence-to-Sequence Models and Applications

# Sequence-to-Sequence (Seq2Seq) Models and Their Architecture
#   What are Seq2Seq Models?
#       - Map an input sequence to an output sequence of different lengths
#       - Widely used for tasks like language translation, text summarization, speech-to-text, and chatbots
#       - Architecture
#           - Encoder
#               - Processes the input sequence and encodes it into a fixed-length vector (context vector)
#           - Decoder
#               - Takes the context vector as input and generates the output sequence, step by step


# Encoder-Decoder Frameworks for Seq2Seq Tasks
#   How it Works
#       - Encoder
#           - Sequentially processes the input sequence using RNN, LSTM, or GRU
#           - Produces a context vector representing the entire input sequence
#
#       - Decoder
#           - Initializes its hidden state with the endcoder's context vector
#           - Generates the output sequence one token at a time
#           - Predicts the next token using the previously generated tokens


# Attention Mechanism Overview
#   Why Attention?
#       - Standard Seq2Seq models compress the entire input sequence into a fixed-length vector, which can lead to information loss for long sequences
#       - Attention Mechanism dynamically focuses on different parts of the input sequence when generating each output token
#
#   How Attention Works
#       - Calculates a weight (or score) for each input token based on its relevance to the current decoder state
#       - Outputs a weighted sum of the encoder outputs, creating a context vector for each decoder step