# Transfer Learning in NLP

# Popular Pre-Trained NLP Models
#   BERT (Bidirectional Encoder Representations from Transformers)
#       - Architecture: Transformer-based encoder model
#       - Training Tasks
#           - Masked Language Modeling (MLM)
#           - Next Sentence Prediction (NSP)
#       - Applications
#           - Text classification, sentiment analysis, question answering
#
#   GPT (Generative Pretrained Transformer)
#       - Architecture: Transformer-based decoder model
#       - Training Task
#           - Causal Language Modeling (predicting next word)
#       - Applications
#           - Text generation, summarization, dialogue systems
#
#   T5 (Text-to-Text Transfer Transformer)
#       - Treats all NLP tasks as text-to-text transformations
#       - Applications
#           - Summarization, translation, text classification
#
#   RoBERTa (Robustly Optimized BERT)
#       - Removes Next Sentence Prediction
#       - Pre-trained on a larger dataset with optimized training strategies
#       - Applications
#           - Similar to BERT but with better performance on downstream tasks


# Tokenization and Text Preprocessing for Fine-Tuning NLP Models
#   Tokenization
#       - Converts raw text into numerical representations
#       - Types
#           - WordPiece Tokenization: Used in BERT
#           - Byte-Pair Encoding (BPE): Used in GPT and RoBERTa
#
#   Text Preprocessing
#       - Cleaning
#           - Remove unnecessary characters (e.g., URL's, special symbols)
#           - Normalization
#               - Convert text to lowercase
#               - Remove stopwords if necessary
#           - Tokenization
#               - Break text into tokens compatible with the pre-trained model


# Adapting Pre-Trained Models for NLP Tasks
#   Common Tasks
#       - Text Classification
#           - Categorize text into predefined labels (e.g., positive/negative sentiment)
#       - Sentiment Analysis
#           - determine the sentiment polarity of text (e.g., positive, neutral, negative)
#       - Summarization
#           - Generate concise summaries from lengthy texts
#
#   Steps
#       - Load pre-trained model
#       - Add a task-specific head (e.g., classification layer)
#       - Fine-tune the model on task-specific data