import pyttsx3
import sounddevice as sd
import vosk
import json
from googletrans import Translator
import queue

q = queue.Queue()

# -------------------------
# Text-to-Speech
# -------------------------
def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    
    if language == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
    
    engine.say(text)
    engine.runAndWait()

# -------------------------
# Vosk Callback for microphone
# -------------------------
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

# -------------------------
# Recognize speech using Vosk
# -------------------------
def speech_to_text(model):
    print("🎤 Speak now...")
    rec = vosk.KaldiRecognizer(model, 16000)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "")
            if text:
                print(f"✅ You said: {text}")
                return text

# -------------------------
# Translate text
# -------------------------
def translate_text(text, target_language="es"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"🌍 Translated text: {translation.text}")
    return translation.text

# -------------------------
# Choose target language
# -------------------------
def display_language_options():
    print("🌍 Available translation languages: ")
    options = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa"
    }
    for num, lang in options.items():
        print(f"{num}. {lang}")
    
    choice = input("Please select the target language number (1-8): ")
    return options.get(choice, "es")  # default Spanish

# -------------------------
# Main function
# -------------------------
def main():
    # Load Vosk model
    print("🤖 Loading Vosk model...")
    model = vosk.Model("model")  # <- Put your downloaded Vosk model folder path here

    target_language = display_language_options()

    # Start microphone stream
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while True:
            original_text = speech_to_text(model)
            if original_text.lower() in ["exit", "stop"]:
                speak("Goodbye!")
                break

            translated_text = translate_text(original_text, target_language=target_language)
            speak(translated_text)

if __name__ == "__main__":
    main()
