import cv2
import numpy as np

# Read an image
image_path = 'image.jpg'  # Replace
try:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Error: Image not found at {image_path}")
except FileNotFoundError as e:
    print(e)
    exit()
height, width = image.shape[:2]


# 1. Color-based segmentation (Example: Segmenting a blue object)
# Convert to HSV color space (more robust to lighting changes)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range of blue color in HSV
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

# Create a mask
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Apply the mask to the original image
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Display
cv2.imshow('Original Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Segmented Image', segmented_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
