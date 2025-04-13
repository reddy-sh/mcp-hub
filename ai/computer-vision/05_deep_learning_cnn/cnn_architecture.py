import tensorflow as tf
from tensorflow.keras import layers, models

def create_cnn_model(input_shape=(28, 28, 1), num_classes=10):
    """
    Creates a simple CNN model for image classification.

    Args:
        input_shape: The shape of the input images (e.g., (28, 28, 1) for grayscale MNIST).
        num_classes: The number of classes to classify.

    Returns:
        A tf.keras.Model instance.
    """
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')  # Softmax for multi-class
    ])
    return model

if __name__ == '__main__':
    # Example usage:
    model = create_cnn_model()
    model.summary()

    # Example with different input shape and number of classes
    color_model = create_cnn_model(input_shape=(32, 32, 3), num_classes=100)
    color_model.summary()
