# ai_learning_activity.py

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

def reinforcement_learning_activity():
    """Reinforcement Learning Simulation Activity."""
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")
    prompt = input("Enter a prompt for the AI model (e.g., 'Describe the lion'): ").strip()
    
    if not prompt:
        print("❌ Prompt cannot be empty.")
        return

    initial_response = generate_response(prompt)
    print(f"\nInitial AI Response:\n{initial_response}\n")

    # Rating
    while True:
        try:
            rating = int(input("Rate the response from 1 (bad) to 5 (good): "))
            if 1 <= rating <= 5:
                break
            else:
                print("❌ Please enter a rating between 1 and 5.")
        except ValueError:
            print("❌ Please enter a valid number (1-5).")
    
    feedback = input("Provide feedback for improvement: ").strip()
    improved_response = f"{initial_response} (Improved with your feedback: {feedback})"
    print(f"\nImproved AI Response:\n{improved_response}")

    # Reflection
    print("\nReflection Questions:")
    print("1. How did the model's response improve with your feedback?")
    print("2. How does reinforcement learning help AI improve over time?\n")

def role_based_prompt_activity():
    """Role-Based Prompts Activity."""
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")
    
    category = input("Enter a category (e.g., science, history, math): ").strip()
    if not category:
        print("❌ Category cannot be empty.")
        return
    
    item = input(f"Enter a specific {category} topic (e.g., 'photosynthesis'): ").strip()
    if not item:
        print("❌ Topic cannot be empty.")
        return

    # Generate role-based prompts
    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."

    teacher_response = generate_response(teacher_prompt)
    expert_response = generate_response(expert_prompt)

    print(f"\n--- Teacher's Perspective ---\n{teacher_response}\n")
    print(f"--- Expert's Perspective ---\n{expert_response}\n")

    # Reflection
    print("Reflection Questions:")
    print("1. How did the AI's response differ between the teacher's and expert's perspectives?")
    print("2. How can role-based prompts help tailor AI responses for different contexts?\n")

def run_activity():
    """Main entry point."""
    print("\n=== AI Learning Activity ===")
    while True:
        choice = input("Which activity would you like to run? (1: Reinforcement Learning, 2: Role-Based Prompts, 3: Exit): ").strip()
        if choice == "1":
            reinforcement_learning_activity()
        elif choice == "2":
            role_based_prompt_activity()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    run_activity()
