import openai
import config  # Make sure config.py has OPENAI_API_KEY = "your_api_key_here"

# Initialize OpenAI client
openai.api_key = config.OPENAI_API_KEY

# Function to generate AI responses
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can also use "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7
    )
    return response.choices[0].message['content']

# Interactive tutorial
def silly_prompt():
    print("Welcome to the AI Prompt Engineering Tutorial!")
    print("We will learn about **Clarity and Specificity** and **Contextual Information** in crafting prompts for AI.\n")
    
    # Step 1: Vague Prompt
    vague_prompt = input("Step 1: Enter a vague prompt (e.g., 'Tell me about technology'): ")
    print(f"\nYour vague prompt: {vague_prompt}")
    print("AI's response to the vague prompt:\n")
    print(generate_response(vague_prompt))
    
    # Step 2: Specific Prompt
    specific_prompt = input("\nStep 2: Make the prompt more specific (e.g., 'Explain how AI works in self-driving cars'): ")
    print(f"\nYour specific prompt: {specific_prompt}")
    print("AI's response to the specific prompt:\n")
    print(generate_response(specific_prompt))
    
    # Step 3: Add Context
    contextual_prompt = input("\nStep 3: Add context to your specific prompt (e.g., 'Given advancements in autonomous vehicles, explain how AI is used in self-driving cars'): ")
    print(f"\nYour contextual prompt: {contextual_prompt}")
    print("AI's response to the contextual prompt:\n")
    print(generate_response(contextual_prompt))
    
    # Reflection
    print("\n--- Reflection Questions ---")
    print("1. How did the AI's response change when the prompt was made more specific?")
    print("2. How did the AI's response improve with the added context?")
    print("3. Which prompt produced the most relevant and tailored response? Why?")

# Run the tutorial
if __name__ == "__main__":
    silly_prompt()
