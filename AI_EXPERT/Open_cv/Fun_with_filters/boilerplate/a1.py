# BEGIN

# IMPORT OpenCV library as cv2
import cv2
# IMPORT NumPy as np

# DEFINE function apply_color_filter(image, filter_type):
#     """
#     Apply a specific color filter to the given image and return the result.
#     """

#     CREATE a copy of the input image called filtered_image

#     IF filter_type == "original":
#         RETURN the unmodified copy of the image

#     ELSE IF filter_type == "red_tint":
#         SET green channel to 0
#         SET blue channel to 0
#         (Leaves only the red channel visible)

#     ELSE IF filter_type == "blue_tint":
#         SET green channel to 0
#         SET red channel to 0
#         (Leaves only the blue channel visible)

#     ELSE IF filter_type == "green_tint":
#         SET blue channel to 0
#         SET red channel to 0
#         (Leaves only the green channel visible)

#     ELSE IF filter_type == "increase_red":
#         INCREASE the red channel intensity by +50 using cv2.add
#         (Ensures pixel values do not overflow beyond 255)

#     ELSE IF filter_type == "decrease_blue":
#         DECREASE the blue channel intensity by -50 using cv2.subtract
#         (Ensures pixel values do not go below 0)

#     RETURN filtered_image


# # MAIN SCRIPT EXECUTION

# SET image_path = "example.jpg"   # File path of input image
# LOAD the image using cv2.imread

# IF image could not be loaded:
#     PRINT error message "Image not found!"

# ELSE:
#     RESIZE the image to width=1200, height=800

#     INITIALIZE filter_type = "original"  # Default filter

#     PRINT key options for the user:
#         o - Original
#         r - Red Tint
#         b - Blue Tint
#         g - Green Tint
#         i - Increase Red Intensity
#         d - Decrease Blue Intensity
#         q - Quit

#     WHILE True (loop continuously until user exits):
#         CALL apply_color_filter(image, filter_type) → filtered_image
#         DISPLAY filtered_image in a window titled "Filtered Image"

#         WAIT for user key input

#         IF key == 'o':
#             SET filter_type = "original"
#         ELSE IF key == 'r':
#             SET filter_type = "red_tint"
#         ELSE IF key == 'b':
#             SET filter_type = "blue_tint"
#         ELSE IF key == 'g':
#             SET filter_type = "green_tint"
#         ELSE IF key == 'i':
#             SET filter_type = "increase_red"
#         ELSE IF key == 'd':
#             SET filter_type = "decrease_blue"
#         ELSE IF key == 'q':
#             PRINT "Exiting..."
#             BREAK the loop
#         ELSE:
#             PRINT "Invalid key! Please use 'o', 'r', 'b', 'g', 'i', 'd', or 'q'."

#     CLOSE all OpenCV windows

# END
