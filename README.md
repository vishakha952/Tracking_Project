# 🎯 Multi-Object Detection and Tracking using YOLOv8

## 📌 Overview

This project implements a computer vision pipeline to detect and track multiple objects (players) in a sports video. Each detected subject is assigned a unique and persistent ID across frames.

The system is designed to handle real-world challenges such as occlusion, motion blur, camera movement, and multiple similar-looking subjects.

---

## 🎯 Objectives

* Detect all relevant subjects in the video
* Assign unique IDs to each subject
* Maintain consistent tracking across frames
* Generate an annotated output video

---

## 🛠️ Technologies Used

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* NumPy

---

## 📂 Project Structure

```
tracking_project/
│
├── input.mp4
├── output_video.mp4
├── main.py
├── README.md
├── report.pdf
└── screenshots/
```

---

## ⚙️ Installation

```
pip install ultralytics opencv-python numpy
```

---

## ▶️ How to Run

```
python main.py
```

If multiple Python versions are installed:

```
"C:\Users\My Lap\AppData\Local\Programs\Python\Python313\python.exe" main.py
```

---

## 🧠 Model and Approach

### Object Detection

* Model: YOLOv8 (yolov8n.pt)
* Reason: Fast and efficient for real-time detection

### Object Tracking

* Tracker: ByteTrack (integrated with YOLOv8)
* Maintains consistent IDs across frames
* Handles occlusion and motion effectively

---

## 🎥 Output Video

🔗 https://github.com/vishakha952/Tracking_Project/blob/main/output_video.mp4

📌 Download if preview is not visible.

---

## 📸 Sample Output

Below are sample frames showing detected players with unique IDs:

https://github.com/vishakha952/Tracking_Project/tree/main/screenshots

---

## ⚠️ Challenges Faced

* Occlusion between players
* Fast movement and motion blur
* Similar appearance of subjects
* Camera movement (pan/zoom)

---

## 🚀 Possible Improvements

* Implement DeepSORT for better tracking accuracy
* Add trajectory visualization
* Player counting system
* Heatmap generation for movement analysis
* Use larger YOLO models for higher accuracy

---

## 🔗 Video Source

🔗 https://github.com/vishakha952/Tracking_Project/blob/main/input.mp4

---

## 📌 Conclusion

This project demonstrates a practical implementation of multi-object detection and tracking using YOLOv8 and ByteTrack. The pipeline is efficient, scalable, and suitable for real-world applications such as sports analytics and surveillance systems.
