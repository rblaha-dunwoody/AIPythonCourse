# Fine-Tuning Techniques in Computer Vision

# Choosing Layers to Fine-Tune and Understanding the Feature Extraction Process
#   Feature Extraction in Pre-Trained Models
#       - Early layers capture low-level features (e.g., edges, textures)
#       - Middle layers capture mid-level features (e.g., shpaes, parts of objects)
#       - Late layers capture high-level features (e.g., specific objects, task-specific patterns)
#
#   Choosing Layers to Fine-Tune
#       - Freeze Early Layers: Retain general features learned during pre-training
#       - Unfreeze Late Layers: Allow the model to adapt high-level features to the new task
#
#   Best Practices
#       - For small datasets: Fine-tune only the last few layers
#       - For large datasets: Unfreeze more layers and fine-tune with a smaller learning rate


# Data Augmentation for Improving Generalization
#   What is Data Augmentation?
#       - Artificially increase the diversity of training data by applying transformations like:
#           - Rotation | Horizontal/vertical flipping | Scaling/zooming | Cropping | Color jittering
#
#   Why Use Data Augmentation?
#       - Reduces overfitting by introducing variability
#       - Improves the model's ability to generalize to unseen data
#
#   Examples of Augmentation
#       - Rotation: Rotate images by random degrees
#       - Flip: Apply horizontal/vertical flips
#       - Zoom: Randomly zoom in/out on images


# Hyperparameter Tuning for Transfer Learning
#   Key Hyperparameters
#       - Learning Rate
#           - A smaller learning rate is recommended for fine-tuning pre-trained models
#           - Too large: Overshoots the optimal solution
#           - Too small: Slow convergence
#
#       - Batch Size
#           - Larger batches stabilize training but require more memory
#           - Smaller batches may lead to noisier updates but help with resource constraints
#
#       - Optimizer
#           - SGD: Works well with transfer learning when paired with momentum
#           - Adam: Faster convergence but may require fine-tuning for stability
#
#   Tuning Process
#       - Start with default settings (e.g., learning rate: 1e-4, batch size: 32)
#       - Experiment with one hyperparameter at a time to isolate its effect