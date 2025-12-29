# ai_writing_assistant.py

import os
from google import genai
from google.genai import types
import config
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Initialize the Gemini API client safely
try:
    client = genai.Client(api_key=config.GEMINI_API_KEY)
except Exception as e:
    print(Fore.RED + f"❌ Error initializing Gemini client: {e}")
    exit(1)

def generate_response(prompt, temperature=0.3):
    """Generate a response from Gemini API with error handling."""
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params
        )
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

def get_essay_details():
    """Collect essay details from the user."""
    print(Fore.CYAN + "\n=== AI Writing Assistant ===\n")

    topic = input(Fore.YELLOW + "What is the topic of your essay? ").strip()
    essay_type = input(Fore.YELLOW + "Essay type (Argumentative, Expository, Descriptive, Persuasive, Analytical): ").strip()

    # Word count selection
    print(Fore.GREEN + "\nSelect the desired essay word count:")
    print(Fore.GREEN + "1. 300 words\n2. 900 words\n3. 1200 words\n4. 2000 words")
    word_count_choice = input(Fore.YELLOW + "Enter number (1-4): ").strip()
    word_count_dict = {"1": "300", "2": "900", "3": "1200", "4": "2000"}
    length = word_count_dict.get(word_count_choice, "300")

    target_audience = input(Fore.YELLOW + "Target audience (e.g., High school students, College professors): ").strip()
    specific_points = input(Fore.YELLOW + "Any specific points to include? ").strip()
    stance = input(Fore.YELLOW + "Your stance on the topic (For/Against/Neutral): ").strip()
    references = input(Fore.YELLOW + "Sources, quotes, or references (optional): ").strip()
    writing_style = input(Fore.YELLOW + "Preferred writing style (Formal, Conversational, Academic, Creative): ").strip()
    outline_needed = input(Fore.YELLOW + "Would you like the AI to suggest an outline first? (Yes/No): ").strip().lower()

    return {
        "topic": topic,
        "essay_type": essay_type,
        "length": length,
        "target_audience": target_audience,
        "specific_points": specific_points,
        "stance": stance,
        "references": references,
        "writing_style": writing_style,
        "outline_needed": outline_needed
    }

def generate_essay_content(details):
    """Generate essay content using AI."""
    # Temperature input with validation
    while True:
        try:
            temperature = float(input(Fore.YELLOW + "Enter AI creativity (0.1 - 1.0, e.g., 0.7): ").strip())
            if 0.1 <= temperature <= 1.0:
                break
            else:
                print(Fore.RED + "Please enter a value between 0.1 and 1.0.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a numeric value.")

    # Introduction
    intro_prompt = f"Write an introduction for a {details['essay_type']} essay about {details['topic']} with stance {details['stance']}."
    introduction = generate_response(intro_prompt, temperature)
    print(Fore.CYAN + "\n=== Generated Introduction ===")
    print(Fore.GREEN + introduction)

    # Body generation choice
    body_style = input(Fore.YELLOW + "Write the body step-by-step or full draft? (Step-by-step/Full draft): ").strip().lower()
    if body_style == "full draft":
        body_prompt = f"Write a detailed {details['essay_type']} essay on {details['topic']} with stance {details['stance']}."
        body = generate_response(body_prompt, temperature)
        print(Fore.CYAN + "\n=== Generated Full Body ===")
        print(Fore.GREEN + body)
    else:
        step_prompt = f"Write step-by-step arguments for the essay on {details['topic']} with stance {details['stance']} including evidence."
        body_step = generate_response(step_prompt, temperature)
        print(Fore.CYAN + "\n=== Generated Step-by-Step Body ===")
        print(Fore.GREEN + body_step)

    # Conclusion
    conclusion_prompt = f"Write a conclusion for a {details['essay_type']} essay about {details['topic']} with stance {details['stance']}."
    conclusion = generate_response(conclusion_prompt, temperature)
    print(Fore.CYAN + "\n=== Generated Conclusion ===")
    print(Fore.GREEN + conclusion)

def feedback_and_refinement():
    """Get user feedback and refinement."""
    satisfaction = input(Fore.YELLOW + "How satisfied are you with the generated content? (1-5 stars): ").strip()
    if satisfaction != "5":
        feedback = input(Fore.YELLOW + "Please provide feedback for improvement (tone, structure, etc.): ").strip()
        print(Fore.CYAN + f"\nThank you for your feedback! Essay will be refined based on: {feedback}")
    else:
        print(Fore.CYAN + "\nGreat! The essay looks good.")

def run_activity():
    """Main function to run the AI writing assistant."""
    print(Fore.CYAN + "\nWelcome to the AI Writing Assistant!\n")
    details = get_essay_details()
    generate_essay_content(details)
    feedback_and_refinement()

if __name__ == "__main__":
    run_activity()
