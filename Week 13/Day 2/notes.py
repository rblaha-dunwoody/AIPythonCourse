# Transfer Learning in Computer Vision

# Popular Pre-Trained Models for Vision Tasks
#   VGG
#       - VGG16/VGG19: Deep networks with 16 or 19 layers
#       - Known for simplicity in architecture: stack of convolutional layers followed by fully connected layers
#       - Applications: General-purpose image classification and feature extraction
#
#   ResNet
#       - Residual Networks: Introduced residual connections (skip connections) to tackle vanishing gradients
#       - Popular variants: ResNet18, ResNet50, ResNet101
#       - Applications: Large-scale image classification tasks, object detection
#
#   Inception
#       - InceptionV3: Known for inception modules, which allow for multi-scale feature extraction in one layer
#       - Applications: Scene recognition, fine-grained image classification
#
#   EfficientNet
#       - Family of models that scales network depth, width, and resolution efficiently
#       - Provides better performance with fewer paramters
#       - Applications: Resource-constrained environments requiring high accuracy


# Freezing and Unfreezing Layers for Fine-Tuning
#   Why Freeze Layers?
#       - Early layers in pre-trained models capture general features
#       - Freezing these layers reduces training time and prevents overfitting on small datasets
#
#   Why Unfreeze layers?
#       - Later layers learn task-specific features
#       - Unfreezing layers allows the model to adapt to the new task
#
#   Approach
#       - Initial Training
#           - Freeze most layers and train the last few layers
#
#       - Fine-Tuning
#           - Gradually unfreeze layers and reduce the learning rate for fine-tuning


# Using Transfer Learning for Image Classification Task
#   Steps:
#       - Load a pre-trained model (e.g., ResNet, VGG)
#       - Replace the last layer with a task-specific classifier (e.g., softmax for multi-class classification)
#       - Fine-tune the model on the new dataset