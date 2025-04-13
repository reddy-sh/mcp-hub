import cv2
import numpy as np

# Read an image
image_path = 'image.jpg'  # Replace with your image path
try:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Error: Image not found at {image_path}")
except FileNotFoundError as e:
    print(e)
    exit()

# Accessing pixel values
height, width, channels = image.shape
print(f"Image dimensions: {height} x {width} x {channels}")

# Get the pixel value at (y, x) = (100, 50)
y, x = 100, 50
pixel_value = image[y, x]
print(f"Pixel value at (y={y}, x={x}): {pixel_value}")  # Returns BGR

# Iterate through all pixels (slow, for demonstration only)
# for y in range(height):
#     for x in range(width):
#         pixel = image[y, x]
#         # Do something with the pixel value

# Accessing color channels
blue_channel = image[:, :, 0]  # All rows, all columns, blue channel
green_channel = image[:, :, 1]
red_channel = image[:, :, 2]

# Displaying individual channels
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()
