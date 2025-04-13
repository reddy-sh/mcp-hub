import cv2

# Read an image
image_path = 'image.jpg'  # Replace with your image
try:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Error: Image not found at {image_path}")
except FileNotFoundError as e:
    print(e)
    exit()

# Resizing
new_width = 300
new_height = 200
resized_image = cv2.resize(image, (new_width, new_height))
cv2.imshow('Resized Image', resized_image)

# Cropping
x_start, y_start = 50, 50
crop_width, crop_height = 100, 150
cropped_image = image[y_start:y_start + crop_height, x_start:x_start + crop_width]
cv2.imshow('Cropped Image', cropped_image)

# Color space conversion (BGR to Grayscale)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)

# Color space conversion (BGR to HSV)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
