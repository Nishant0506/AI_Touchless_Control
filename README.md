# AI Touchless Computer Control System

This project allows controlling your computer using hand gestures and voice commands via a web dashboard.

## Setup

1. Run `python setup.py` to install dependencies.
2. Run `python backend/main.py` to start the server.
3. Open browser to http://localhost:5000

## Features

- **Gesture Control**: Move mouse with index finger, left click with thumb-index pinch.
- **Voice Commands**: "open chrome", "open vs code", "take screenshot", "scroll up", "scroll down", "stop system".
- **Web Dashboard**: Start/stop system, status indicators, live camera feed, voice text, activity log.

## Requirements

- Python 3.7+
- Webcam
- Microphone
- Windows OS (for app opening commands)

## Usage

- Start the system from the dashboard.
- Use hand gestures in front of webcam for mouse control.
- Speak commands clearly into microphone.
- View live feed and logs on the dashboard.