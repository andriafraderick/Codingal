import os
import time
import sys

# Choose which API to use: "gemini" or "openai"
API_PROVIDER = "openai"  # Change to "gemini" if you want to use Google Gemini

# Load API keys from config.py
try:
    import config
except ImportError:
    print("❌ Could not find config.py. Create it with your API keys.")
    sys.exit(1)

# Import the appropriate client based on provider
if API_PROVIDER == "gemini":
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("❌ google-genai is not installed. Run: pip install google-genai")
        sys.exit(1)
elif API_PROVIDER == "openai":
    try:
        import openai
    except ImportError:
        print("❌ openai package not installed. Run: pip install openai")
        sys.exit(1)
else:
    print("❌ Invalid API_PROVIDER. Use 'gemini' or 'openai'.")
    sys.exit(1)


def generate_response(prompt, temperature=0.5):
    """Generate a response from the selected AI provider."""
    try:
        if API_PROVIDER == "gemini":
            client = genai.Client(api_key=config.GEMINI_API_KEY)
            contents = [types.Content(role="user", parts=[types.Part.from_text(prompt)])]
            config_gen = types.GenerateContentConfig(temperature=temperature, response_mime_type="text/plain")
            response = client.models.generate_content(model="gemini-2.0-flash", contents=contents, config=config_gen)
            return response.text
        else:  # OpenAI GPT
            openai.api_key = config.OPENAI_API_KEY
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature
            )
            return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error generating response: {e}"


def generate_streaming_response(prompt, temperature=0.5):
    """Stream responses without blocking the terminal."""
    try:
        print("\nStreaming response (press Ctrl+C to stop):")
        if API_PROVIDER == "gemini":
            client = genai.Client(api_key=config.GEMINI_API_KEY)
            contents = [types.Content(role="user", parts=[types.Part.from_text(prompt)])]
            config_gen = types.GenerateContentConfig(temperature=temperature, response_mime_type="text/plain")
            for chunk in client.models.generate_content_stream(model="gemini-2.0-flash", contents=contents, config=config_gen):
                print(chunk.text, end="", flush=True)
            print()
        else:  # OpenAI streaming
            openai.api_key = config.OPENAI_API_KEY
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                stream=True
            )
            for event in response:
                if "choices" in event:
                    delta = event["choices"][0]["delta"]
                    if "content" in delta:
                        print(delta["content"], end="", flush=True)
            print()
    except KeyboardInterrupt:
        print("\n⚡ Streaming stopped by user.")
    except Exception as e:
        print(f"\n❌ Error streaming response: {e}")


def temperature_prompt_activity():
    """Interactive activity to explore temperature and instruction-based prompts."""
    print("=" * 80)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")
    print("=" * 80)
    print("\nWe'll explore how temperature affects creativity and how instructions shape outputs.")

    # Temperature exploration
    base_prompt = input("\nEnter a creative prompt (e.g., 'Write a story about a robot learning to paint'): ")

    temps = [("LOW (0.1) - Deterministic", 0.1), ("MEDIUM (0.5) - Balanced", 0.5), ("HIGH (0.9) - Creative", 0.9)]
    for label, temp in temps:
        print(f"\n--- {label} ---")
        print(generate_response(base_prompt, temperature=temp))
        time.sleep(1)

    # Instruction-based prompts
    topic = input("\nChoose a topic for instruction-based prompts (e.g., 'space exploration'): ")
    instructions = [
        f"Summarize the key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I were a 10-year-old.",
        f"Write a pro/con list about {topic}.",
        f"Create a fictional news headline from the year 2050 about {topic}."
    ]

    for i, instr in enumerate(instructions, 1):
        print(f"\n--- INSTRUCTION {i}: {instr} ---")
        print(generate_response(instr, temperature=0.7))
        time.sleep(1)

    # Custom instruction + temperature
    custom_instr = input("\nEnter your own instruction-based prompt: ")
    try:
        custom_temp = float(input("Set temperature (0.1 to 1.0, default 0.7): ") or 0.7)
        if not 0.1 <= custom_temp <= 1.0:
            print("⚠ Invalid temperature. Using default 0.7.")
            custom_temp = 0.7
    except ValueError:
        custom_temp = 0.7

    print(f"\n--- YOUR CUSTOM PROMPT WITH TEMPERATURE {custom_temp} ---")
    print(generate_response(custom_instr, temperature=custom_temp))

    # Optional streaming
    choice = input("\nWould you like to see a streaming response? (y/n): ").lower().strip()
    if choice == 'y':
        stream_prompt = input("Enter a prompt for streaming response: ")
        generate_streaming_response(stream_prompt, temperature=0.7)


if __name__ == "__main__":
    temperature_prompt_activity()
