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

# Convert to float for normalization
image = image.astype(np.float32)

# Min-Max normalization to [0, 1]
normalized_image = (image - np.min(image)) / (np.max(image) - np.min(image))

# Display original and normalized (scaled to 0-255 for display)
cv2.imshow('Original Image', image.astype(np.uint8))
cv2.imshow('Normalized Image', (normalized_image * 255).astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Standardization (Z-score normalization)
mean = np.mean(image)
std = np.std(image)
standardized_image = (image - mean) / std
print(f"Mean: {mean}, Std: {std}")
