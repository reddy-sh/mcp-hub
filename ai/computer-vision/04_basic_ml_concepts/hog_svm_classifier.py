import cv2
from skimage.feature import hog
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import os

def load_and_preprocess_images(folder_path, target_size=(64, 64)):
    """Loads images from a folder, resizes them, and extracts HOG features.

    Args:
        folder_path: Path to the folder containing images.
        target_size: The size to resize the images to.

    Returns:
        A tuple containing the feature matrix (X) and the labels (y).
    """
    images = []
    labels = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)
            if image is None:
                print(f"Warning: Could not read image {image_path}")
                continue
            image = cv2.resize(image, target_size)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # HOG on grayscale
            images.append(image)
            labels.append(os.path.basename(folder_path))  # Use folder name as label
    return images, labels

def extract_hog_features(images, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(3, 3)):
    """Extracts HOG features from a list of images.

        Args:
            images: List of images.
            orientations: HOG orientation
            pixels_per_cell: HOG cell size
            cells_per_block: HOG block size

        Returns:
            Numpy array of HOG features
    """
    hog_features = []
    for image in images:
        hog_feature = hog(image, orientations=orientations,
                          pixels_per_cell=pixels_per_cell,
                          cells_per_block=cells_per_block,
                          feature_vector=True)
        hog_features.append(hog_feature)
    return np.array(hog_features)



# Load images and extract HOG features
# Create two folders "cats" and "dogs" inside 04_basic_ml_concepts and put some cat and dog images.
cats_folder = 'cats'  # Replace with the path to your cats folder
dogs_folder = 'dogs'  # Replace with the path to your dogs folder
cats_images, cats_labels = load_and_preprocess_images(cats_folder)
dogs_images, dogs_labels = load_and_preprocess_images(dogs_folder)

all_images = cats_images + dogs_images
all_labels = ['cat'] * len(cats_images) + ['dog'] * len(dogs_images)


X = extract_hog_features(all_images)
y = all_labels

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train an SVM classifier
svm_classifier = SVC(kernel='linear', C=1.0)  # You can experiment with different kernels and C
svm_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm_classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
