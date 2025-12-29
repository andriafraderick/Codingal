def generate_response(prompt, level="vague"):
    """
    Simulated AI responses for offline demo
    """

    if level == "vague":
        return (
            "Technology refers to the use of scientific knowledge, tools, "
            "and machines to solve problems and make life easier."
        )

    elif level == "specific":
        return (
            "Artificial Intelligence helps self-driving cars by processing "
            "data from cameras and sensors to detect objects, recognize traffic signs, "
            "and make driving decisions."
        )

    elif level == "context":
        return (
            "In modern autonomous vehicles, Artificial Intelligence analyzes "
            "real-time data from sensors, cameras, and GPS systems to safely "
            "navigate roads, avoid obstacles, and follow traffic rules, "
            "reducing human error."
        )


def silly_prompt():
    print("Welcome to the AI Prompt Engineering Tutorial!")
    print("This activity demonstrates:")
    print("1. Clarity and Specificity")
    print("2. Contextual Information")

    # Step 1: Vague prompt
    vague = input("\nEnter a vague prompt (e.g., 'Tell me about technology'): ")
    print("\nAI response (Vague Prompt):")
    print(generate_response(vague, "vague"))

    # Step 2: Specific prompt
    specific = input("\nMake it more specific (e.g., 'Explain how AI helps self-driving cars'): ")
    print("\nAI response (Specific Prompt):")
    print(generate_response(specific, "specific"))

    # Step 3: Contextual prompt
    context = input("\nAdd context to the prompt: ")
    print("\nAI response (Contextual Prompt):")
    print(generate_response(context, "context"))

    # Reflection
    print("\n--- Reflection ---")
    print("1. How did the response change when the prompt became more specific?")
    print("2. How did adding context improve the response?")
    print("3. Which response was the most useful and why?")


if __name__ == "__main__":
    silly_prompt()
