# Fine-Tuning Techniques in NLP

# Fine-Tuning Methods for NLP Tasks
#   Discriminative Fine-Tuning
#       - Different layers of a pre-trained model capture different types of information
#       - Approach:
#           - Use different learning rates for different layers of the model
#           - Lower learning rates for early layers (general features)
#           - Higher learning rates for later layers (task-specific features)
#
#   Slanted Triangular Learning Rates (STLR)
#       - Dynamically adjusts learning rates during training to balance exploration and convergence
#       - Phases:
#           - Warm-Up: Gradually increase the learning rate to promote exploration
#           - Decay: Slowly decrease the learning rate to ensure convergence
#
#   Use Case
#       - Effective for fine-tuning pre-trained models like BERT and GPT


# Regularization and Dropout for Preventing Overfitting in NLP Models
#   Regularization
#       - L1 Regularization: Encourages sparsity by penalizing absolute weights
#       - L2 Regularization (Ridge): Penalizes large weights to improve generalization
#
#   Dropout
#       - Randomly drops units (along with their connections) during training
#       - Prevents over-reliance on specific neurons
#       - Commonly used in Transformer-based models


# Evaluating Model Performance with NLP-Specific Metrics
#   Key Metrics:
#       - F1-Score
#           - Harmonic mean of precision and recall
#           - Suitable for classification tasks with imbalanced datasets
#
#       - BLEU Score
#           - Evaluates the quality of generated text against reference text
#           - Commonly used for translation and summarization tasks
#
#       - ROUGE Score
#           - Measures overlap between generated and reference text
#           - Used for summarization tasks