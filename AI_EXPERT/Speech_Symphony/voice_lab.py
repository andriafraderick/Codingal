import random

# Try importing pyttsx3 for TTS
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("⚠️  Run: pip install pyttsx3")


def setup_tts():
    """Initialize text-to-speech engine and select a voice"""
    if not TTS_AVAILABLE:
        return None
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)     # Speech rate
        engine.setProperty("volume", 0.9)   # Volume (0.0 to 1.0)
        
        # Pick the first available voice (Windows default)
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)
        
        return engine
    except Exception as e:
        print(f"⚠️ TTS initialization failed: {e}")
        return None


def speak(engine, text):
    """Speak text or fallback to printing"""
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"🔇 [AUDIO FAIL]: {text} | Error: {e}")
    else:
        print(f"🔇 [AUDIO]: {text}")


def get_samples():
    """Return a list of sample phrases"""
    return [
        "Hello! I am your computer!",
        "Python is awesome!",
        "This is AI speaking!",
        "Welcome to the future!"
    ]


def main():
    print("🤖 AI VOICE LAB")
    print("===============")

    engine = setup_tts()

    if engine:
        print("✅ Voice ready! Try typing something...")
    else:
        print("⚠️  No audio, but you can still type and see output")

    speak(engine, "Hello! Type something for me to say!")

    while True:
        try:
            text = input("\n🎤 You: ").strip()
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            speak(engine, "Goodbye!")
            break

        if not text:
            print("💡 Type 'sample' for ideas or 'exit' to quit")
            continue

        if text.lower() == 'exit':
            speak(engine, "Goodbye!")
            break
        elif text.lower() == 'sample':
            phrase = random.choice(get_samples())
            print(f"🎲 {phrase}")
            speak(engine, phrase)
        else:
            speak(engine, text)


if __name__ == "__main__":
    main()
