# AI Touchless Computer Control System

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/Nishant0506/AI_Touchless_Control)
[![Python](https://img.shields.io/badge/Python-3.7+-green)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-lightgrey)](https://flask.palletsprojects.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-red)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)

A complete production-ready system that allows users to control their computer using hand gestures and voice commands via a modern web dashboard.

## ✨ Features

### 🤖 Gesture Control
- **Real-time hand tracking** using OpenCV skin detection
- **Mouse cursor control** - move cursor with hand movement
- **Live camera feed** with visual feedback
- **Smooth cursor movement** with configurable smoothing

### 🎤 Voice Control
- **Continuous speech recognition** using SpeechRecognition
- **Pre-built commands**:
  - `"open chrome"` → Opens Google Chrome
  - `"open vs code"` → Opens VS Code
  - `"take screenshot"` → Saves screenshot to project folder
  - `"scroll up"` → Scrolls up
  - `"scroll down"` → Scrolls down
  - `"stop system"` → Safely stops all modules

### 🌐 Web Dashboard
- **Modern glassmorphism UI** with responsive design
- **Real-time status indicators** for Camera, Gesture, and Voice modules
- **Live camera feed** embedded in dashboard
- **Activity log panel** showing all system events
- **Voice command display** showing recognized speech
- **Start/Stop system controls**

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Webcam (built-in or external)
- Microphone (built-in or external)
- Windows OS (for app opening commands)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nishant0506/AI_Touchless_Control.git
   cd AI_Touchless_Control
   ```

2. **Install dependencies:**
   ```bash
   python setup.py
   ```
   Or manually:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python backend/main.py
   ```

4. **Open your browser:**
   Navigate to `http://localhost:5000`

## 🎯 Usage

1. **Start the System**: Click the green "Start System" button
2. **Gesture Control**: Place your hand in front of the webcam to control mouse cursor
3. **Voice Commands**: Speak clearly into your microphone
4. **Monitor**: Watch real-time updates in the dashboard

## 📁 Project Structure

```
AI_Touchless_Control/
├── backend/
│   ├── main.py           # Flask server and API endpoints
│   ├── gesture_control.py # Hand gesture detection module
│   ├── voice_control.py   # Voice recognition module
│   └── utils.py          # Shared state management
├── frontend/
│   ├── templates/
│   │   └── index.html    # Main dashboard HTML
│   └── static/
│       ├── style.css     # Glassmorphism styling
│       ├── script.js     # Frontend JavaScript
│       └── animations.css # UI animations
├── requirements.txt      # Python dependencies
├── setup.py             # Automated setup script
└── README.md            # This file
```

## 🛠️ Technical Details

### Backend Architecture
- **Flask Framework** for web server and REST APIs
- **Threading** for parallel gesture and voice processing
- **Base64 encoding** for real-time camera feed transmission
- **Error handling** and logging throughout

### Computer Vision
- **OpenCV** for camera access and image processing
- **Skin color detection** in HSV color space
- **Contour detection** for hand tracking
- **Real-time video processing** at camera frame rate

### Speech Recognition
- **SpeechRecognition library** with Google API
- **Continuous listening** with timeout handling
- **Command parsing** and execution
- **Error recovery** for recognition failures

## 🔧 Configuration

### Gesture Control Settings
- **Skin color range**: Adjustable HSV thresholds in `gesture_control.py`
- **Smoothing factor**: Configurable cursor smoothing (0.0-1.0)
- **Minimum hand area**: Threshold for hand detection

### Voice Recognition Settings
- **Recognition timeout**: Adjustable listening duration
- **Phrase time limit**: Maximum command length
- **Ambient noise adjustment**: Automatic calibration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV** for computer vision capabilities
- **SpeechRecognition** for voice processing
- **Flask** for the web framework
- **MediaPipe** (inspiration for gesture detection)

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/Nishant0506/AI_Touchless_Control/issues) page
2. Create a new issue with detailed information
3. Include your system specifications and error messages

---

**Made with ❤️ for touchless computing enthusiasts**