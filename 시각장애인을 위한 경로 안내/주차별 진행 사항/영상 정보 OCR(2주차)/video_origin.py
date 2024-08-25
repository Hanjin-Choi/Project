import cv2
import torch 
from ultralytics import YOLO
from util.imgocr import img_ocr
import sys
sys.stdout=open('out.txt','w')

model = YOLO('./yolov8_pretrained/yolov9s.pt')

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

cap = cv2.VideoCapture('3217waiting.MOV')

if not cap.isOpened():
    print('Error: Could not open camera.')
    exit()

frame_skip = 2
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue
    
    resized_frame = cv2.resize(frame,(640,640))

    frame_tensor = torch.from_numpy(resized_frame).permute(2,0,1).unsqueeze(0).float().div(255.0).to(device)

    results = model(frame_tensor)
    ocr_results ={}
    for result in results:
        print(result)
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            confidence = box.conf[0].item()
            class_id = box.cls[0].item()
            
            if model.names[int(class_id)] =='bus' and confidence >= 0.8:
                bus_roi = resized_frame[int(y1):int(y2), int(x1):int(x2)]
                ocr_result = img_ocr(bus_roi)
                if ocr_result:
                    label = f'{model.names[int(class_id)]}: {ocr_result}' 
                    print(label)
                else:
                    label = ''
                cv2.rectangle(resized_frame, (int(x1), int(y1)), (int(x2), int(y1)-(int(y1)-int(y2))//3), (0,255,0), 2)
                
                cv2.putText(resized_frame, label, (int(x1), int(y2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow('YOLOv8 Detection', resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    