class SystemState:
    def __init__(self):
        self.running = False
        self.voice_text = ""
        self.log = []
        self.camera_frame = ""
        self.camera_ok = False
        self.listening = False