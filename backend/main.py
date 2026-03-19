from flask import Flask, render_template, jsonify, request
import threading
import os
from gesture_control import start_gesture
from voice_control import start_voice
from utils import SystemState

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

state = SystemState()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-system', methods=['POST'])
def start_system():
    # In cloud environment, only start voice control (no camera/gesture)
    if not state.running:
        state.running = True
        # Only start voice thread in cloud
        voice_thread = threading.Thread(target=start_voice, args=(state,))
        voice_thread.start()
        state.log.append("Voice control started (cloud mode)")
    return jsonify({'status': 'started', 'mode': 'voice_only'})

@app.route('/stop-system', methods=['POST'])
def stop_system():
    state.running = False
    # Wait for threads to finish with timeout
    return jsonify({'status': 'stopped'})

@app.route('/status')
def get_status():
    return jsonify({
        'running':False,  # Camera not available in cloud
        'gesture': False,  # Gesture control not available in cloud
        'listening': state.listening,
        'mode': 'cloud'
        'listening': state.listening
    })

@app.route('/camera_feed')
def camera_feed():
    try:
        # For cloud deployment, return placeholder since camera access is not available
        return jsonify({'frame': '', 'message': 'Camera not available in cloud environment'})
    except Exception as e:
        return jsonify({'frame': '', 'error': str(e)})

@app.route('/voice_text')
def voice_text():
    return jsonify({'text': state.voice_text})

@app.route('/log')
def get_log():
    return jsonify({'log': state.log[-20:]})  # Last 20 log entries

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))