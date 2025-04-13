import cv2
from skimage.feature import hog
import matplotlib.pyplot as plt

# Read image
image_path = 'image.jpg' #replace
try:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Error: Image not found at {image_path}")
except FileNotFoundError as e:
    print(e)
    exit()
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # HOG works on grayscale

# HOG parameters
orientations = 9
pixels_per_cell = (8, 8)
cells_per_block = (3, 3)

# Compute HOG features
hog_features, hog_image = hog(image, orientations=orientations,
                              pixels_per_cell=pixels_per_cell,
                              cells_per_block=cells_per_block,
                              visualize=True,
                              feature_vector=True)  # Return flattened feature vector

# Display
plt.imshow(hog_image, cmap=plt.cm.gray)
plt.title('HOG Image')
plt.show()

print(f"HOG feature shape: {hog_features.shape}")