🚗🚶 Vehicle and Pedestrian Detection & Tracking System

A real-time computer vision project built with OpenCV that detects and tracks cars and pedestrians in a video feed using Haar cascade classifiers and CSRT trackers.

📌 Features
Detects pedestrians using a full-body Haar cascade
Detects cars using a car Haar cascade
Tracks detected objects across frames using CSRT trackers
Displays live pedestrian count and car count
Draws bounding boxes around tracked objects
Processes video input from a file
🧠 How It Works

The program reads frames from a video and converts each frame to grayscale for object detection. It uses Haar cascade classifiers to detect pedestrians and cars, then creates CSRT trackers to follow them across frames and maintain a running count of each object type.

🛠️ Tech Stack
Python
OpenCV
📂 Required Files

Make sure these files are in the same folder as your Python script:

Cars2.mp4
haarcascade_fullbody.xml
haarcascade_cars.xml
⚙️ Installation

Install OpenCV:

pip install opencv-python opencv-contrib-python
▶️ Usage

Run the script:

python main.py
Controls
Press ESC to quit the program
📷 Output

The program displays:

Green rectangles for pedestrians
Red rectangles for cars
Live pedestrian count
Live car count
🔧 How Tracking Works
Detect pedestrians and cars in each frame
Compare new detections with existing tracked objects
If an object is new, create a new CSRT tracker
If an object is already tracked, continue following it
Remove trackers when objects leave the frame

⚠️ Limitations
Haar cascades are less accurate than modern deep learning models
Counts may reset if objects are temporarily missed
Fast movement or occlusion can reduce tracking accuracy
Performance depends on video quality and cascade quality

🔮 Future Improvements
Replace Haar cascades with YOLO for better detection accuracy
Add unique object IDs
Improve counting logic to avoid duplicate counts
Support live webcam or traffic camera input
Export counts and detections to a log file

👤 Author
Built as a computer vision project exploring object detection, tracking, and counting with OpenCV.
