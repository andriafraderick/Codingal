import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import pyttsx3
from googletrans import Translator

# ------------------ Setup TTS ------------------
def setup_tts():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Default voice
    return engine

def speak(engine, text):
    engine.say(text)
    engine.runAndWait()

# ------------------ Translate ------------------
translator = Translator()

def translate_text(text, target_language="es"):
    try:
        translation = translator.translate(text, dest=target_language)
        print(f"🌍 Translated: {translation.text}")
        return translation.text
    except Exception as e:
        print(f"❌ Translation error: {e}")
        return text

# ------------------ Vosk Speech Recognition ------------------
def recognize_speech(model, duration=5, samplerate=16000):
    rec = KaldiRecognizer(model, samplerate)
    print(f"🎤 Speak now (listening for {duration} seconds)...")
    
    try:
        audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
        sd.wait()
        if rec.AcceptWaveform(audio_data):
            result = json.loads(rec.Result())
            text = result.get('text', "")
            if text:
                print(f"✅ You said: {text}")
                return text
    except Exception as e:
        print(f"❌ Error recording audio: {e}")
    print("❌ Could not recognize speech.")
    return ""

# ------------------ Language Options ------------------
def display_language_options():
    languages = {
        "1": "hi", "2": "ta", "3": "te", "4": "bn",
        "5": "mr", "6": "gu", "7": "ml", "8": "pa"
    }
    print("🌍 Available languages:")
    print("1. Hindi (hi)  2. Tamil (ta)  3. Telugu (te)  4. Bengali (bn)")
    print("5. Marathi (mr) 6. Gujarati (gu) 7. Malayalam (ml) 8. Punjabi (pa)")
    choice = input("Select target language number (1-8, default=es): ").strip()
    return languages.get(choice, "es")

# ------------------ Main Loop ------------------
def main():
    print("🤖 Speech Translation Lab (Vosk + pyttsx3)")
    tts_engine = setup_tts()
    
    print("Loading Vosk model...")
    model = Model("model")  # Put your downloaded vosk model folder here
    print("✅ Model loaded. You can start speaking now!")

    while True:
        target_lang = display_language_options()
        speech_text = recognize_speech(model)
        
        if speech_text.lower() in ["exit", "quit"]:
            speak(tts_engine, "Goodbye!")
            print("👋 Exiting...")
            break
        elif speech_text.lower() in ["sample", "example"]:
            sample_text = "Hello! This is a sample translation."
            print(f"🎲 Sample: {sample_text}")
            speak(tts_engine, translate_text(sample_text, target_lang))
        elif speech_text:
            translated = translate_text(speech_text, target_lang)
            speak(tts_engine, translated)
        else:
            print("💡 No input detected. Say 'sample' for example or 'exit' to quit.")

if __name__ == "__main__":
    main()
