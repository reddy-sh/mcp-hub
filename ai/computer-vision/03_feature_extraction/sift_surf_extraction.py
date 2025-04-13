import cv2

# Read image
image_path = 'image.jpg'  # Replace
try:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Error: Image not found at {image_path}")
except FileNotFoundError as e:
    print(e)
    exit()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# SIFT
sift = cv2.SIFT_create()
keypoints_sift, descriptors_sift = sift.detectAndCompute(gray_image, None)
image_with_sift_keypoints = cv2.drawKeypoints(gray_image, keypoints_sift, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SIFT Keypoints', image_with_sift_keypoints)

# SURF
surf = cv2.SURF_create()
keypoints_surf, descriptors_surf = surf.detectAndCompute(gray_image, None)
image_with_surf_keypoints = cv2.drawKeypoints(gray_image, keypoints_surf, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SURF Keypoints', image_with_surf_keypoints)

cv2.waitKey(0)
cv2.destroyAllWindows()
