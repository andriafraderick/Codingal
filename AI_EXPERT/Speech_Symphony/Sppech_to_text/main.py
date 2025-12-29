import os

import time

from google import genai

from google.genai import types

import config

 

# To run this code, install the required dependency:

# pip install google-genai

 

def generate_response(prompt, temperature=0.5):

    """Generate a response from Gemini API with a specified temperature."""

    try:

        # Initialize the client with API key from config module

        client = genai.Client(api_key=config.GEMINI_API_KEY)

        

        # Create the content structure

        contents = [

            types.Content(

                role="user",

                parts=[

                    types.Part.from_text(text=prompt),

                ],

            ),

        ]

        

        # Configure generation parameters

        generate_content_config = types.GenerateContentConfig(

            temperature=temperature,

            response_mime_type="text/plain",

        )

        

        # Generate content (non-streaming version for simplicity)

        response = client.models.generate_content(

            model="gemini-2.0-flash",

            contents=contents,

            config=generate_content_config,

        )

        

        # Extract and return the response text

        return response.text

    except Exception as e:

        return f"Error generating response: {str(e)}"

 

def temperature_prompt_activity():

    """Interactive activity to explore temperature settings and instruction-based prompts."""

    print("=" * 80)

    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")

    print("=" * 80)

    print("\nIn this activity, we'll explore:")

    print("1. How temperature affects AI creativity and randomness")

    print("2. How instruction-based prompts can control AI outputs")

    

    # Part 1: Temperature Exploration

    print("\n" + "-" * 40)

    print("PART 1: TEMPERATURE EXPLORATION")

    print("-" * 40)

    

    base_prompt = input("\nEnter a creative prompt (e.g., 'Write a short story about a robot learning to paint'): ")

    

    print("\nGenerating responses with different temperature settings...")

    print("\n--- LOW TEMPERATURE (0.1) - More Deterministic ---")

    low_temp_response = generate_response(base_prompt, temperature=0.1)

    print(low_temp_response)

    

    # Add a small delay between API calls to avoid rate limiting

    time.sleep(1) 

    

    print("\n--- MEDIUM TEMPERATURE (0.5) - Balanced ---")

    medium_temp_response = generate_response(base_prompt, temperature=0.5)

    print(medium_temp_response)

    

    # Add a small delay between API calls to avoid rate limiting

    time.sleep(1)

    

    print("\n--- HIGH TEMPERATURE (0.9) - More Random/Creative ---")

    high_temp_response = generate_response(base_prompt, temperature=0.9)

    print(high_temp_response)

    

    # Part 2: Instruction-Based Prompts

    print("\n" + "-" * 40)

    print("PART 2: INSTRUCTION-BASED PROMPTS")

    print("-" * 40)

    

    print("\nNow, let's explore how specific instructions change the AI's output.")

    

    topic = input("\nChoose a topic (e.g., 'climate change', 'space exploration'): ")

    

    # Different instruction-based prompts

    instructions = [

        f"Summarize the key facts about {topic} in 3-4 sentences.",

        f"Explain {topic} as if I'm a 10-year-old child.",

        f"Write a pro/con list about {topic}.",

        f"Create a fictional news headline from the year 2050 about {topic}."

    ]

    

    # Display different instruction-based outputs

    for i, instruction in enumerate(instructions, 1):

        print(f"\n--- INSTRUCTION {i}: {instruction} ---")

        response = generate_response(instruction, temperature=0.7)

        print(response)

        # Add a small delay between API calls to avoid rate limiting

        time.sleep(1)

    

    # Part 3: Combining Instructions and Temperature

    print("\n" + "-" * 40)

    print("PART 3: CREATING YOUR OWN INSTRUCTION-BASED PROMPTS")

    print("-" * 40)

    

    print("\nNow it's your turn! Create an instruction-based prompt and test it with different temperatures.")

    

    custom_instruction = input("\nEnter your instruction-based prompt: ")

    

    # Let the user choose a temperature

    try:

        custom_temp = float(input("\nSet a temperature (0.1 to 1.0): "))

        if custom_temp < 0.1 or custom_temp > 1.0:

            print("Invalid temperature. Using default 0.7.")

            custom_temp = 0.7

    except ValueError:

        print("Invalid input. Using default temperature 0.7.")

        custom_temp = 0.7

    

    print(f"\n--- YOUR CUSTOM PROMPT WITH TEMPERATURE {custom_temp} ---")

    custom_response = generate_response(custom_instruction, temperature=custom_temp)

    print(custom_response)

    

    # Reflection Questions

    print("\n" + "-" * 40)

    print("REFLECTION QUESTIONS")

    print("-" * 40)

    print("1. How did changing the temperature affect the creativity and variety in the AI's responses?")

    print("2. Which instruction-based prompt produced the most useful or interesting result? Why?")

    print("3. How might you combine specific instructions and temperature settings in real applications?")

    print("4. What patterns did you notice in how the AI responds to different types of instructions?")

    

    # Challenge Activity

    print("\n" + "-" * 40)

    print("CHALLENGE ACTIVITY")

    print("-" * 40)

    print("Try creating a 'chain' of prompts where:")

    print("1. First, ask the AI to generate content about a topic")

    print("2. Then, use an instruction-based prompt to modify or build upon that content")

    print("3. Experiment with different temperature settings at each step")

    print("\nFor example: Generate a story → Instruct AI to rewrite it in a specific style → Ask AI to create a sequel")

 

# For demonstrating streaming responses (optional part)

def generate_streaming_response(prompt, temperature=0.5):

    """Generate a streaming response from Gemini API with a specified temperature."""

    try:

        # Initialize the client with API key from config module

        client = genai.Client(api_key=config.GEMINI_API_KEY)

        

        # Create the content structure

        contents = [

            types.Content(

                role="user",

                parts=[

                    types.Part.from_text(text=prompt),

                ],

            ),

        ]

        

        # Configure generation parameters

        generate_content_config = types.GenerateContentConfig(

            temperature=temperature,

            response_mime_type="text/plain",

        )

        

        # Generate content with streaming

        print("\nStreaming response (press Ctrl+C to stop):")

        for chunk in client.models.generate_content_stream(

            model="gemini-2.0-flash",

            contents=contents,

            config=generate_content_config,

        ):

            print(chunk.text, end="")

        print("\n")  # Add a newline at the end

        

    except Exception as e:

        print(f"\nError generating streaming response: {str(e)}")


def generate_response(prompt, temperature=0.5):
    try:
        client = genai.Client(api_key=config.GEMINI_API_KEY)

        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]

        config_data = types.GenerateContentConfig(
            temperature=temperature,
            response_mime_type="text/plain",
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config=config_data,
        )

        return response.text

    except Exception:
        # OFFLINE DEMO RESPONSE
        return (
            f"[OFFLINE DEMO MODE]\n"
            f"Prompt: {prompt}\n"
            f"Temperature: {temperature}\n\n"
            f"This is a simulated AI response demonstrating how temperature "
            f"affects creativity in real applications."
        )



 

# Run the activity

if __name__ == "__main__":

    temperature_prompt_activity()

    

    # Optional: Demonstrate streaming responses

    print("\n" + "-" * 40)

    print("BONUS: STREAMING RESPONSES")

    print("-" * 40)

    print("Would you like to see a streaming response? (y/n)")

    choice = input("> ").lower().strip()

    if choice == 'y':

        prompt = input("\nEnter a prompt for streaming response: ")

        generate_streaming_response(prompt, temperature=0.7)