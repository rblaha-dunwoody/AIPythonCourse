# Convolutional Layers and Filters

# Convolutional Operations, Filters, and Feature Maps
#   What is a Convolutional Operation?
#       - Mathematical operation where a small matrix (kernel or filter) slides over the input image to extract features like edges, textures, or patterns
#       - Key Concepts
#           - Kernel (Filter)
#               - A small matrix (e.g., 3x3) used to extract features
#               - Each element of the kernel is a weight learned during training
#
#           - Feature Map
#               - The output of a convolution operation
#               - Highlights specific patterns detected by the filter
#
#           - Channels
#               - For RGB images, convolution processes each color channel separately and combines results


# Concepts of Kernel Size, Stride, and Padding
#   Kernel Size
#       - The dimensions of the filter (e.g., 3x3, 5x5)
#       - Smaller Kernels: Capture fine details
#       - Larger Kernels: Detect broader features
#
#   Stride
#       - Defines the step size of the filter as it slides across the input
#       - Larger Strides: Reduce the feature map size, improving computation efficiency
#       - Smaller Strides: Retain more detail but increase computation
#
#   Padding
#       - Adds extra pixels around the input to control the size of the output
#       - Valid Padding: No padding; the feature map shrinks
#       - Same Padding: Adds enough padding to keep the output size equal to the input size


# Visualizing How Convolution Extracts Features
#   Edge Detection
#       - Kernels like Sobel or Prewitt highlight edges in images
#
#   Feature Extraction
#       - Initial layers focus on edges; deeper layers capture abstract patterns