import cv2
import matplotlib.pyplot as plt

def load_image(image_path):
    """Loads an image using OpenCV.

    Args:
        image_path: Path to the image file.

    Returns:
        The image as a NumPy array, or None if the image cannot be loaded.
    """
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Error: Image not found at {image_path}")
        return image
    except FileNotFoundError as e:
        print(e)
        return None  # Explicitly return None for error handling

def display_image(image, title='Image', convert_to_rgb=True):
    """Displays an image using Matplotlib.

    Args:
        image: The image to display (NumPy array).
        title: The title of the plot.
        convert_to_rgb: Whether to convert from BGR (OpenCV) to RGB (Matplotlib).
    """
    if image is not None: #check if the image is loaded
        if convert_to_rgb:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
        plt.title(title)
        plt.show()

def save_image(image, output_path):
    """Saves an image using OpenCV.

    Args:
        image: The image to save (NumPy array).
        output_path: Path to save the image file.
    """
    cv2.imwrite(output_path, image)
    print(f"Image saved to {output_path}")
