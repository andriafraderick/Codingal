# ai_prompt_activity.py

import os
from google import genai
from google.genai import types
import config

# Initialize the Gemini API client
try:
    client = genai.Client(api_key=config.GEMINI_API_KEY)
except Exception as e:
    print(f"❌ Error initializing Gemini client: {e}")
    exit(1)

def generate_response(prompt, temperature=0.3):
    """Generate a response from Gemini API."""
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

def bias_mitigation_activity():
    """Bias Mitigation Activity."""
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    
    prompt = input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'): ").strip()
    if not prompt:
        print("❌ Prompt cannot be empty.")
        return

    initial_response = generate_response(prompt)
    print(f"\nInitial AI Response:\n{initial_response}\n")
    
    modified_prompt = input("Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a doctor'): ").strip()
    if not modified_prompt:
        print("❌ Modified prompt cannot be empty.")
        return

    modified_response = generate_response(modified_prompt)
    print(f"\nModified AI Response (Neutral):\n{modified_response}\n")

def token_limit_activity():
    """Token Limit Activity."""
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    
    long_prompt = input("Enter a long prompt (more than 300 words, e.g., a detailed story or description): ").strip()
    if not long_prompt:
        print("❌ Prompt cannot be empty.")
        return

    long_response = generate_response(long_prompt)
    print(f"\nResponse to Long Prompt:\n{long_response[:500]}... [truncated]\n")  # Limit output for demonstration

    short_prompt = input("Now, condense the prompt to be more concise: ").strip()
    if not short_prompt:
        print("❌ Condensed prompt cannot be empty.")
        return

    short_response = generate_response(short_prompt)
    print(f"\nResponse to Condensed Prompt:\n{short_response}\n")

def run_activity():
    """Runs the activity with user selection."""
    print("\n=== AI Learning Activity ===")
    
    while True:
        activity_choice = input("Which activity would you like to run? (1: Bias Mitigation, 2: Token Limits, 3: Exit): ").strip()
        
        if activity_choice == "1":
            bias_mitigation_activity()
        elif activity_choice == "2":
            token_limit_activity()
        elif activity_choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    run_activity()
