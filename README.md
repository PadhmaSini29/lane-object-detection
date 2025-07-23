# 🚗 Lane & Object Detection Pipeline

This project implements a robust **lane line detection** and **object detection** system using Python. It combines computer vision techniques for lane detection with a YOLOv5 deep learning model for real-time object recognition (vehicles, pedestrians, traffic signs, etc.).

## 📦 Features

- 🎯 Accurate lane line detection using color thresholding + perspective transforms
- 🔍 Multiple object detection with YOLOv5
- 📸 Supports images and video
- 🖥️ Streamlit frontend for easy use
- ⚡ FastAPI backend for model inference
- 📊 Logs and displays detection stats

## 🧠 Tech Stack

| Layer      | Tool / Framework         |
|------------|--------------------------|
| Language   | Python                   |
| Lane Lines | OpenCV + NumPy           |
| Object Detection | YOLOv5 (PyTorch Hub) |
| UI         | Streamlit + Bootstrap    |
| API        | FastAPI                  |
| Video      | moviepy                  |

## 🗂️ Folder Structure

```
Advanced-Lane-Lines/
│
├── CameraCalibration.py
├── LaneLines.py
├── Thresholding.py
├── PerspectiveTransformation.py
├── ObjectDetector.py
├── main.py                 # Main script (image/video)
├── backend/api.py          # FastAPI backend
├── frontend/app.py         # Streamlit frontend
├── logs/log.txt            # Detection logs
├── static/input.jpg        # Uploaded image
├── static/output.jpg       # Processed result
└── yolov5/ (optional)      # YOLOv5 source if cloned
```

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PadhmaSini29/lane-object-detection.git
cd lane-object-detection
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install torch torchvision opencv-python matplotlib moviepy docopt streamlit fastapi uvicorn
```

### 3️⃣ Run Main Script

- Process an image:
  ```bash
  python main.py test_images/test1.jpg output_images/output1.jpg
  ```

- Process a video:
  ```bash
  python main.py --video project_video.mp4 output_videos/output_video.mp4
  ```

## 🌐 Web App

### 🖥️ FastAPI Backend

```bash
uvicorn backend.api:app --reload
```

### 💻 Streamlit Frontend

```bash
streamlit run frontend/app.py
```

You can upload images and view results interactively.

## 📝 Logs & Stats

Detection logs are stored in `logs/log.txt`, showing object counts per image with timestamps.

