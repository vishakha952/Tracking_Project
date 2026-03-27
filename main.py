from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")


cap = cv2.VideoCapture(r"C:\Users\My Lap\OneDrive\Desktop\tracking_project\input.mp4")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(frame, persist=True)

    for r in results:
        if r.boxes is None:
            continue

        for box in r.boxes:
            if box.id is None:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            id = int(box.id)

            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, f"ID {id}", (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow("video", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()