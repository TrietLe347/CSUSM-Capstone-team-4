# 🕺 PoseMirror – Interactive Science Demo

This project is an **interactive demo** where a cartoon or animated character mirrors a user’s body posture and movements in **real time** using AI pose estimation.  
It is built to showcase the capabilities of **Snapdragon X Elite-powered devices** for on-device AI and graphics.

---

## 🚀 Project Overview

- **Real-Time Pose Tracking** – Capture movements from the webcam and extract skeleton landmarks.  
- **Animated Character Mirroring** – (Planned) A cartoon/3D character will mimic the user’s movements.  
- **Split-Screen UI** – Webcam + pose overlay on one side, animated character on the other.  
- **On-Device Execution** – Runs locally on Snapdragon X Elite hardware with Qualcomm AI SDKs.  

Current state: ✅ baseline pose tracking with **MediaPipe BlazePose**.  
Next steps: 🔄 integrate ONNX/Qualcomm AI Hub models and build the animation pipeline.

---

## 🛠️ Tech Stack

- **AI Models:** BlazePose (via MediaPipe), later MoveNet / Qualcomm AI Hub ONNX models  
- **Frameworks:** OpenCV, MediaPipe, ONNX Runtime  
- **Programming Language:** Python 3.10+  
- **Animation Engine (Planned):** Unity (C#) or WebGL (Three.js/Babylon.js)  
- **Tools & SDKs:** QAIRT, QNN, LiteRT, Qualcomm AI Hub (for Snapdragon optimization)  

---

🧩 Features in Progress
 Baseline pose detection with BlazePose (MediaPipe)

 Build ONNX backend for MoveNet/BlazePose

 Integrate Qualcomm QNN/QAIRT for Snapdragon acceleration

 WebSocket bridge to Unity/WebGL

 Animated stick figure / character mirroring

🤝 Collaboration
Weekly mentor check-ins (Thursday 2:30).

Communication via Discord/Microsoft Teams.

All code contributions should be made via pull requests.

📖 Learning Outcomes
Real-time computer vision & AI inference

Working with Qualcomm AI SDKs and on-device acceleration

Integrating AI pipelines with animation engines

Team collaboration using GitHub + SCRUM/Agile

📌 Notes
For now, we’re using MediaPipe BlazePose as a fast baseline.

Qualcomm’s AI Hub models will replace this once Snapdragon hardware is available.

Keep .venv/, .idea/, and other local files out of Git (see .gitignore).

