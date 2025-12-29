# ai_teaching_assistant.py

import streamlit as st
from google import genai
from google.genai import types
import config

# Initialize the Gemini API client safely
try:
    client = genai.Client(api_key=config.GEMINI_API_KEY)
except Exception as e:
    st.error(f"❌ Error initializing Gemini client: {e}")
    st.stop()

def generate_response(prompt: str, temperature: float = 0.3) -> str:
    """
    Generate a response from Gemini API.
    Returns the text or error message.
    """
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config=config_params
        )
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

def setup_ui():
    """Streamlit UI setup."""
    st.set_page_config(page_title="AI Teaching Assistant", layout="wide")
    st.title("📚 AI Teaching Assistant")
    st.write("Ask me anything about various subjects, and I will provide an answer.")

    # Sidebar for temperature setting
    st.sidebar.header("Settings")
    temperature = st.sidebar.slider(
        "AI Creativity (Temperature)", 0.1, 1.0, 0.3, 0.1
    )

    # User input
    user_input = st.text_input("Enter your question here:")

    if st.button("Ask AI"):
        if not user_input.strip():
            st.warning("Please enter a question to ask the AI.")
        else:
            with st.spinner("Generating response..."):
                response = generate_response(user_input.strip(), temperature)
            st.markdown("**Your question:**")
            st.write(user_input)
            st.markdown("**AI's answer:**")
            st.write(response)

def main():
    setup_ui()

if __name__ == "__main__":
    main()
