import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image
image_path = 'image.jpg'  # Replace with a path to your image file
try:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Error: Image not found at {image_path}")
except FileNotFoundError as e:
    print(e)
    exit()

# Display the image using Matplotlib (remember to convert color order)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.show()

# Save the image
output_path = 'saved_image.png'
cv2.imwrite(output_path, image)
print(f"Image saved to {output_path}")

# Image information
print(f"Image shape: {image.shape}")  # (height, width, channels)
print(f"Image data type: {image.dtype}")
