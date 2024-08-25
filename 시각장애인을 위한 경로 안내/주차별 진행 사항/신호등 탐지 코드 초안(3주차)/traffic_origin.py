import cv2
import torch
import yolov5

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5','custom',path='best.pt',force_reload=True)

# Set inference settings
model.conf = 0.25  # confidence threshold
model.iou = 0.45  # IoU threshold for NMS
model.max_det = 1000  # maximum number of detections per image

video_path = './IMG_4759.MOV'

# Create a video capture object
cap = cv2.VideoCapture(video_path)

frame_skip = 2
frame_count = 0

# Create a window for display
window_name = 'frame'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 600)

flag = -1  # Initialize flag

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue

    # Use the model to detect objects in the frame
    results = model(frame, size=640, augment=False)  # setting image size for inference

    # Process each detected object
    for _, row in results.pandas().xyxy[0].iterrows():
        # Bounding box coordinates
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        # Class name and confidence
        label = f"{row['name']} {row['confidence']:.2f}"
        print(label)
        
        # Traffic light logic
        if flag == -1:
            if row['name'] == 'red':
                flag = 0
            elif row['name'] == 'green':
                flag = 1
        elif flag == 0 and row['name'] == 'green':
            print('go')
            flag = 1
        elif flag == 1 and row['name'] == 'red':
            print('stop')
            flag = 0

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Draw class name and confidence
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
