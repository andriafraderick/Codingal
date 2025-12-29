import sounddevice as sd
import vosk
import pyttsx3
import queue
import json

q = queue.Queue()

# Load Vosk model
model = vosk.Model("path_to_vosk_model")  # e.g., "D:/vosk-model-small-en-us-0.15"

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def main():
    speak("Voice assistant activated. Speak now!")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                command = result.get("text", "")
                if command:
                    print("✅ You said:", command)
                    if "exit" in command or "stop" in command:
                        speak("Goodbye!")
                        break
                    elif "hello" in command:
                        speak("Hi there! How can I help you today?")
                    elif "time" in command:
                        from datetime import datetime
                        now = datetime.now().strftime("%H:%M")
                        speak(f"The time is {now}")
                    else:
                        speak("I'm not sure how to help with that.")

if __name__ == "__main__":
    main()
