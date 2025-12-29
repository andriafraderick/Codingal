# ai_teaching_assistant.py

import streamlit as st
from google import genai
from google.genai import types
import io
import config

# Initialize Gemini API client
client = genai.Client(api_key=config.GEMINI_API_KEY)

# -------- Common Gemini API Calls --------
def generate_response(prompt, temperature=0.3):
    """General AI response"""
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def generate_math_response(prompt, temperature=0.1):
    """Math-focused AI response with detailed steps"""
    system_prompt = """You are a Math Mastermind - an expert mathematics problem solver with exceptional abilities in:

- Algebra, Calculus, Geometry, Trigonometry
- Statistics, Probability, Linear Algebra
- Discrete Mathematics, Number Theory
- Mathematical Proofs and Logic
- Applied Mathematics and Word Problems

For every math problem:
1. Show clear step-by-step solutions
2. Explain the mathematical reasoning
3. Provide alternative solving methods when applicable
4. Verify your answer when possible
5. Use proper mathematical notation
6. Break down complex problems into manageable parts

Format your responses with:
- Clear problem identification
- Step-by-step solution process
- Final answer highlighted
- Brief explanation of concepts used

Always be precise, thorough, and educational in your mathematical explanations."""
    try:
        full_prompt = f"{system_prompt}\n\nMath Problem: {prompt}"
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=full_prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# -------- AI Teaching Assistant UI --------
def run_ai_teaching_assistant():
    st.title("🧑‍🏫 AI Teaching Assistant")
    st.write("Ask me anything about various subjects, and I'll provide an insightful answer.")

    # Initialize conversation history
    if "history_ata" not in st.session_state:
        st.session_state.history_ata = []

    # Buttons: Clear and Export
    col_clear, col_export = st.columns([1, 2])

    with col_clear:
        if st.button("🧹 Clear Conversation", key="clear_ata"):
            st.session_state.history_ata = []
            st.experimental_rerun()

    with col_export:
        if st.session_state.history_ata:
            export_text = ""
            for idx, qa in enumerate(st.session_state.history_ata, start=1):
                export_text += f"Q{idx}: {qa['question']}\n"
                export_text += f"A{idx}: {qa['answer']}\n\n"

            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)

            st.download_button(
                label="💾 Export Chat History",
                data=bio,
                file_name="AI_Teaching_Assistant_Conversation.txt",
                mime="text/plain",
            )

    # User input
    user_input = st.text_input("Enter your question here:", key="input_ata")
    if st.button("Ask", key="ask_ata"):
        if user_input.strip():
            with st.spinner("Generating AI response..."):
                # Check if user wants math-specific solution
                if any(word in user_input.lower() for word in ["solve", "calculate", "integral", "derivative", "equation", "algebra", "math", "geometry", "probability"]):
                    response = generate_math_response(user_input.strip())
                else:
                    response = generate_response(user_input.strip(), temperature=0.3)
            st.session_state.history_ata.append({"question": user_input.strip(), "answer": response})
            st.experimental_rerun()
        else:
            st.warning("⚠️ Please enter a question before clicking Ask.")

    # Display conversation history
    st.markdown("### Conversation History")
    for idx, qa in enumerate(st.session_state.history_ata, start=1):
        st.markdown(f"**Q{idx}:** {qa['question']}")
        st.markdown(f"**A{idx}:** {qa['answer']}")

# -------- Main --------
def main():
    st.set_page_config(page_title="🧑‍🏫 AI Teaching Assistant", layout="centered")
    run_ai_teaching_assistant()

if __name__ == "__main__":
    main()
