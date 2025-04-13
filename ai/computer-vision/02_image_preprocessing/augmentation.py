import cv2
import numpy as np
import random

# Read an image
image_path = 'image.jpg'  # Replace
try:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Error: Image not found at {image_path}")
except FileNotFoundError as e:
    print(e)
    exit()

# Function for augmentation
def augment_image(image, angle=0, flip=0):
    """
    Augments the image with rotation and flipping.

    Args:
        image: The input image.
        angle: Rotation angle in degrees.
        flip: 0 for no flip, 1 for horizontal, -1 for vertical.

    Returns:
        The augmented image.
    """
    augmented_image = image.copy() # Create a copy to avoid modifying the original
    if angle != 0:
        (h, w) = augmented_image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        augmented_image = cv2.warpAffine(augmented_image, M, (w, h))
    if flip != 0:
        augmented_image = cv2.flip(augmented_image, flip)
    return augmented_image

# Example usage
rotated_image = augment_image(image, angle=30)
flipped_image = augment_image(image, flip=1)
rotated_and_flipped_image = augment_image(image, angle=45, flip=-1)

# Display
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Flipped Image', flipped_image)
cv2.imshow('Rotated and Flipped', rotated_and_flipped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
