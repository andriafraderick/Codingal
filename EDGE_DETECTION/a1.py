# --------------------------------------------------------------
# Import necessary libraries for:
# 1. Image processing (OpenCV)
# 2. Numerical operations (NumPy)
# 3. Displaying images (Matplotlib)
# --------------------------------------------------------------

# --------------------------------------------------------------
# Define a utility function to display images using Matplotlib.
# 1. Set up the figure size.
# 2. Check if image is grayscale or color.
# 3. Convert color images from BGR to RGB for correct rendering.
# 4. Set the plot title and hide the axis.
# 5. Display the image on the screen.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Define the main interactive function for edge detection.
# 1. Load an image from a specified path.
# 2. Convert it to grayscale.
# 3. Show the grayscale image to the user.
# 4. Present a menu of operations:
#    a) Sobel Edge Detection
#    b) Canny Edge Detection
#    c) Laplacian Edge Detection
#    d) Gaussian Smoothing
#    e) Median Filtering
#    f) Exit
# 5. Prompt the user to pick an option.
# 6. Perform the chosen operation and display the result.
# 7. Repeat until the user decides to exit.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Sobel Edge Detection:
# 1. Calculate Sobel filters along the x and y directions.
# 2. Convert both results to 8-bit images.
# 3. Combine them using bitwise OR.
# 4. Display the combined edge map.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Canny Edge Detection:
# 1. Ask for lower and upper thresholds.
# 2. Apply Canny edge detection, which:
#    - Smooths the image with a Gaussian filter.
#    - Finds intensity gradients.
#    - Applies non-maximum suppression.
#    - Uses double-thresholding and edge tracking.
# 3. Display the detected edges.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Laplacian Edge Detection:
# 1. Apply the Laplacian operator (second derivative).
# 2. Take the absolute value of the result to handle negative gradients.
# 3. Convert to 8-bit for display.
# 4. Show the resulting edges.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Gaussian Smoothing:
# 1. Prompt the user for a kernel size (odd number).
# 2. Apply GaussianBlur with the specified kernel.
# 3. Display the smoothed image, which helps reduce noise.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Median Filtering:
# 1. Prompt the user for a kernel size (odd number).
# 2. Apply medianBlur, which replaces each pixel with the median of neighbors.
# 3. This helps remove salt-and-pepper noise while preserving edges.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Exit:
# 1. Print a message confirming exit.
# 2. Break out of the interactive loop.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Make a call to the interactive function with the path to an image.
# e.g., interactive_edge_detection("example.jpg")
# This is where the program starts running and awaits user input.
# --------------------------------------------------------------
