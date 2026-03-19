from flask import Flask, render_template, jsonify, request
import threading
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
    if not state.running:
        state.running = True
        gesture_thread = threading.Thread(target=start_gesture, args=(state,))
        voice_thread = threading.Thread(target=start_voice, args=(state,))
        gesture_thread.start()
        voice_thread.start()
    return jsonify({'status': 'started'})

@app.route('/stop-system', methods=['POST'])
def stop_system():
    state.running = False
    # Wait for threads to finish with timeout
    return jsonify({'status': 'stopped'})

@app.route('/status')
def get_status():
    return jsonify({
        'running': state.running,
        'camera': state.camera_ok,
        'gesture': state.running,
        'listening': state.listening
    })

@app.route('/camera_feed')
def camera_feed():
    try:
        return jsonify({'frame': state.camera_frame or ''})
    except Exception as e:
        return jsonify({'frame': '', 'error': str(e)})

@app.route('/voice_text')
def voice_text():
    return jsonify({'text': state.voice_text})

@app.route('/log')
def get_log():
    return jsonify({'log': state.log[-20:]})  # Last 20 log entries

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)