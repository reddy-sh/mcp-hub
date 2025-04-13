import cv2

# Load a pre-trained YOLO model (you'll need the weights and config file)
# Download these from a source like: https://github.com/pjreddie/darknet
weights_path = 'yolov3.weights'  # Replace with your weights file
config_path = 'yolov3.cfg'    # Replace with your config file
net = cv2.dnn.readNet(weights_path, config_path)

# Load class names
with open('coco.names', 'r') as f:  # COCO dataset class names
    classes = [line.strip() for line in f]

# Load an image
image_path = 'image.jpg'  # Replace
try:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Error: Image not found at {image_path}")
except FileNotFoundError as e:
    print(e)
    exit()
height, width = image.shape[:2]

# Create a blob from the image
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)  # Common size is 416

# Pass the blob through the network
net.setInput(blob)
output_layers_names = net.getUnconnectedOutLayersNames()
outputs = net.forward(output_layers_names)

# Process the outputs
boxes = []
confidences = []
class_ids = []
for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:  # Confidence threshold
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Apply non-maximum suppression to eliminate redundant boxes
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)  # Confidence and NMS thresholds

# Draw bounding boxes
if len(indices) > 0:
    for i in indices.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = confidences[i]
        color = (0, 255, 0)  # Green
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        cv2.putText(image, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Display the result
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
