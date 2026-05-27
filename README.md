# -ParkLens
A real-time, edge-AI parking occupancy tracker using YOLOv8 and MQTT streaming.
# 🚘 ParkLens

> **ParkLens** is an end-to-end computer vision and data engineering pipeline that monitors parking lot occupancy in real time. By leveraging YOLOv8 for edge object detection and MQTT for lightweight data streaming, it transforms raw video feeds into actionable, live occupancy analytics.

---

## 🚀 Features

* **Real-Time Edge Detection:** Background processing of video frames using an optimized YOLOv8 model to identify vacant vs. occupied spots.
* **Lightweight Data Streaming:** Publishes live status updates, coordinates, and total counts via **MQTT protocol** to keep network overhead minimal.
* **Analytical Insights:** Automatically generates statistical graphs plotting peak usage hours, occupancy rates, and turnover times.
* **Modular Architecture:** Clean separation of data collection, computer vision inference, and streaming infrastructure.

---

## 🛠️ Tech Stack

* **Core Language:** Python 3.10+
* **Computer Vision:** OpenCV, Ultralytics YOLOv8
* **Data Streaming:** Paho-MQTT
* **Analysis & Visualization:** Matplotlib, Pandas, NumPy

---

## 📦 Project Structure

```text
parklens/
├── data/
│   ├── sample_video.mp4      # Test footage for inference
│   └── parking_map.json      # Pre-mapped ROI coordinates for parking slots
├── src/
│   ├── __init__.py
│   ├── config.py             # MQTT and model configurations
│   ├── detect.py             # YOLOv8 inference & spot processing logic
│   ├── stream.py             # MQTT client initialization and publishing
│   └── analytics.py          # Script to generate post-run occupancy graphs
├── requirements.txt
├── main.py                   # Central execution script
└── README.md
