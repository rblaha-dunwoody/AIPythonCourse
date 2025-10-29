# Text Preprocessing and Word Embedding for RNN's

# Importance of Text Preprocessing
#   What is Text Preprocessing?
#       - Involves cleaning and preparing raw text data to make it suitable for machine learning models
#       - Critical step for achieving high performance in Natural Language Processing (NLP) tasks
#       - Key Steps
#           - Tokenization: Splits text into individual words (e.g., words, sentences)
#               - Example: "I love NLP" -> ["I", "Love", "NLP"]
#
#           - Stemming: Reduces words to their root form by removing suffixes
#               - Example: "running", "runner" -> "run"
#
#           - Lemmatization: Converts words to their base form using a vocabulary
#               - Example: "better" -> "good"
#
#   Why is Preprocessing Important?
#       - Reduces noise in the data
#       - Standardizes input for models
#       - Improves feature extraction and model accuracy


# Introduction to Word Embeddings
#   What are Word Embeddings?
#       - Dense vector representations of words that capture semantic meaning
#       - Represent words in a continuous vector space
#       - Popular Word Embedding Models
#           - Word2Vec:
#               - Models: Continuous Bag of Words (CBOW) and Skip-gram
#               - Captures word relationships based on context
#
#           - GloVe (Global Vectors for Word Representation)
#               - Uses word co-occurrence statistics to generate embeddings
#               - Represents global semantic relationships
#
#           - Pre-trained Embeddings in Frameworks
#               - Frameworks like TensorFlow and PyTorch offer pre-trained embeddings for quick integration
#
#       - Benefits of Word Embeddings
#           - Reduce dimensionality
#           - Capture semantic similarity
#           - Improve model generalization


# Using Pre-Trained Embeddings for NLP Tasks
#   Why Use Pre-Trained Embeddings
#       - Saves computational resources
#       - Leverages large, well-trained models
#       - Boosts performance for downstream tasks
#
#   Popular Pre-Trained Embeddings
#       - GloVe: Pre-trained on datasets like Wikipedia and Common Crawl
#       - FastText: Handles out-of-vocabulary (OOV) words through subword embeddings
#       - Embedding Layers in deep learning frameworks like TensorFlow and PyTorch