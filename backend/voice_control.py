import speech_recognition as sr
import pyautogui
import os
import subprocess

def start_voice(state):
    """
    Starts the voice control module.
    Continuously listens for voice commands and executes them.
    """
    r = sr.Recognizer()
    mic = sr.Microphone()
    
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
    except Exception as e:
        state.log.append(f"Error setting up microphone: {e}")
        return
    
    state.listening = True
    
    while state.running:
        try:
            with mic as source:
                audio = r.listen(source, timeout=1, phrase_time_limit=5)
            
            text = r.recognize_google(audio).lower()
            state.voice_text = text
            state.log.append(f"Recognized: {text}")
            
            # Execute commands
            if "open chrome" in text:
                try:
                    os.startfile("chrome.exe")  # Windows specific
                    state.log.append("Opened Google Chrome")
                except Exception as e:
                    state.log.append(f"Failed to open Chrome: {e}")
            elif "open vs code" in text:
                try:
                    subprocess.run(["code"])  # Assuming VS Code is in PATH
                    state.log.append("Opened VS Code")
                except Exception as e:
                    state.log.append(f"Failed to open VS Code: {e}")
            elif "take screenshot" in text:
                try:
                    screenshot = pyautogui.screenshot()
                    screenshot.save("screenshot.png")
                    state.log.append("Screenshot saved as screenshot.png")
                except Exception as e:
                    state.log.append(f"Failed to take screenshot: {e}")
            elif "scroll up" in text:
                pyautogui.scroll(100)
                state.log.append("Scrolled up")
            elif "scroll down" in text:
                pyautogui.scroll(-100)
                state.log.append("Scrolled down")
            elif "stop system" in text:
                state.running = False
                state.log.append("Stopping system via voice command")
                
        except sr.WaitTimeoutError:
            pass  # No speech detected, continue listening
        except sr.UnknownValueError:
            pass  # Speech not recognized, continue
        except Exception as e:
            state.log.append(f"Voice recognition error: {e}")
    
    state.listening = False