// JavaScript for AI Touchless Control Dashboard

document.addEventListener('DOMContentLoaded', function() {
    const startBtn = document.getElementById('start-btn');
    const stopBtn = document.getElementById('stop-btn');
    const cameraFeed = document.getElementById('camera-feed');
    const voiceText = document.getElementById('voice-text');
    const activityLog = document.getElementById('activity-log');
    
    // Status indicators
    const cameraDot = document.getElementById('camera-dot');
    const gestureDot = document.getElementById('gesture-dot');
    const listeningDot = document.getElementById('listening-dot');
    
    // Event listeners for control buttons
    startBtn.addEventListener('click', function() {
        fetch('/start-system', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('System started:', data);
        })
        .catch(error => {
            console.error('Error starting system:', error);
        });
    });
    
    stopBtn.addEventListener('click', function() {
        fetch('/stop-system', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('System stopped:', data);
        })
        .catch(error => {
            console.error('Error stopping system:', error);
        });
    });
    
    // Function to update status indicators
    function updateStatus() {
        fetch('/status')
        .then(response => response.json())
        .then(data => {
            updateIndicator(cameraDot, data.camera);
            updateIndicator(gestureDot, data.gesture);
            updateIndicator(listeningDot, data.listening);
        })
        .catch(error => {
            console.error('Error fetching status:', error);
        });
    }
    
    // Function to update camera feed
    function updateCameraFeed() {
        fetch('/camera_feed')
        .then(response => response.json())
        .then(data => {
            if (data.frame && data.frame.length > 0) {
                cameraFeed.src = 'data:image/jpeg;base64,' + data.frame;
                cameraFeed.classList.remove('loading');
                cameraFeed.style.display = 'block';
            } else {
                cameraFeed.classList.add('loading');
                cameraFeed.style.display = 'none';
            }
        })
        .catch(error => {
            console.error('Error fetching camera feed:', error);
            cameraFeed.classList.add('loading');
            cameraFeed.style.display = 'none';
        });
    }
    
    // Function to update voice text
    function updateVoiceText() {
        fetch('/voice_text')
        .then(response => response.json())
        .then(data => {
            if (data.text !== voiceText.textContent) {
                voiceText.textContent = data.text || 'Listening for commands...';
                voiceText.classList.add('updating');
                setTimeout(() => {
                    voiceText.classList.remove('updating');
                }, 1000);
            }
        })
        .catch(error => {
            console.error('Error fetching voice text:', error);
        });
    }
    
    // Function to update activity log
    function updateActivityLog() {
        fetch('/log')
        .then(response => response.json())
        .then(data => {
            activityLog.innerHTML = '';
            data.log.forEach(entry => {
                const li = document.createElement('li');
                li.textContent = entry;
                activityLog.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error fetching activity log:', error);
        });
    }
    
    // Helper function to update status indicators
    function updateIndicator(dot, isActive) {
        if (isActive) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    }
    
    // Update all components every second
    function updateAll() {
        updateStatus();
        updateCameraFeed();
        updateVoiceText();
        updateActivityLog();
    }
    
    // Initial update
    updateAll();
    
    // Set up periodic updates
    setInterval(updateAll, 1000);
});