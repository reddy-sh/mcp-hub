import tensorflow as tf
from tensorflow.keras import layers, models, datasets
from tensorflow.keras.utils import to_categorical

# Load and preprocess the CIFAR-10 dataset
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
train_images = train_images.astype('float32') / 255.0  # Normalize to [0, 1]
test_images = test_images.astype('float32') / 255.0
train_labels = to_categorical(train_labels, num_classes=10)  # One-hot encode
test_labels = to_categorical(test_labels, num_classes=10)

# Create a CNN model (you can define a more complex one)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),  # Increased units
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',  # Use a better optimizer
              loss='categorical_crossentropy',  # Correct loss function for multi-class
              metrics=['accuracy'])

# Train the model
history = model.fit(train_images, train_labels, epochs=10, batch_size=64, validation_split=0.2)  # Added batch size and validation

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc:.2f}")

# Save the model
model.save('cifar10_classifier.h5')
