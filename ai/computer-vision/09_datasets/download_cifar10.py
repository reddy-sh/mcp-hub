import tensorflow as tf
from tensorflow.keras import datasets

def download_cifar10():
    """Downloads the CIFAR-10 dataset using TensorFlow/Keras."""
    (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
    print("CIFAR-10 dataset downloaded.")
    # You could add code here to save it to a specific directory if needed
    return (train_images, train_labels), (test_images, test_labels)

if __name__ == '__main__':
    download_cifar10()