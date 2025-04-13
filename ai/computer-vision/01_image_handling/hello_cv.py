# 01_image_handling/hello_cv.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Hello, Computer Vision!")
print(f"OpenCV Version: {cv2.__version__}")
print(f"NumPy Version: {np.__version__}")
print(f"Matplotlib Version: {plt.matplotlib.__version__}")

# Create a simple blue image
image = np.zeros((100, 200, 3), dtype=np.uint8)
image[:, :, 2] = 255  # Set blue channel to maximum

# OpenCV uses BGR by default, Matplotlib uses RGB, so we need to convert.
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Simple Blue Image")
plt.show()

cv2.imwrite("blue_image.png", image)
print("Blue image saved as blue_image.png")