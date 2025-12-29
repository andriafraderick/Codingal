# ai_master_suite.py

import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import io
import re
import config

# Initialize Gemini API client
client = genai.Client(api_key=config.GEMINI_API_KEY)

# -------- Common Gemini API calls --------
def generate_response(prompt, temperature=0.3):
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def generate_math_response(prompt, temperature=0.1):
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

# -------- AI Teaching Assistant --------
def run_ai_teaching_assistant():
    st.title("🧑‍🏫 AI Teaching Assistant")
    st.write("Ask me anything about various subjects, and I'll provide an insightful answer.")

    if "history_ata" not in st.session_state:
        st.session_state.history_ata = []

    col_clear, col_export = st.columns([1, 2])
    with col_clear:
        if st.button("🧹 Clear Conversation", key="clear_ata"):
            st.session_state.history_ata = []
            st.experimental_rerun()
    with col_export:
        if st.session_state.history_ata:
            export_text = ""
            for idx, qa in enumerate(st.session_state.history_ata, start=1):
                export_text += f"Q{idx}: {qa['question']}\nA{idx}: {qa['answer']}\n\n"
            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)
            st.download_button(
                label="💾 Export Chat History",
                data=bio,
                file_name="AI_Teaching_Assistant_Conversation.txt",
                mime="text/plain"
            )

    user_input = st.text_input("Enter your question here:", key="input_ata")
    if st.button("Ask", key="ask_ata"):
        if user_input.strip():
            with st.spinner("Generating AI response..."):
                # Detect math-related questions
                if any(word in user_input.lower() for word in ["solve", "calculate", "integral", "derivative", "equation", "algebra", "math", "geometry", "probability"]):
                    response = generate_math_response(user_input.strip())
                else:
                    response = generate_response(user_input.strip(), temperature=0.3)
            st.session_state.history_ata.append({"question": user_input.strip(), "answer": response})
            st.experimental_rerun()
        else:
            st.warning("⚠️ Please enter a question before clicking Ask.")

    st.markdown("### Conversation History")
    for idx, qa in enumerate(st.session_state.history_ata, start=1):
        st.markdown(f"**Q{idx}:** {qa['question']}")
        st.markdown(f"**A{idx}:** {qa['answer']}")

# -------- Math Mastermind --------
def run_math_mastermind():
    st.title("🧮 Math Mastermind")
    st.write("**Your Expert Mathematical Problem Solver** - From basic arithmetic to advanced calculus, I'll solve any math problem with step-by-step explanations!")

    if "history_mm" not in st.session_state:
        st.session_state.history_mm = []
    if "input_key_mm" not in st.session_state:
        st.session_state.input_key_mm = 0

    col_clear, col_export = st.columns([1, 2])
    with col_clear:
        if st.button("🧹 Clear Conversation", key="clear_mm"):
            st.session_state.history_mm = []
            st.experimental_rerun()
    with col_export:
        if st.session_state.history_mm:
            export_text = ""
            for idx, qa in enumerate(st.session_state.history_mm, start=1):
                export_text += f"Q{idx}: {qa['question']}\nA{idx}: {qa['answer']}\n\n"
            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)
            st.download_button(
                label="💾 Export Math Solutions",
                data=bio,
                file_name="Math_Mastermind_Solutions.txt",
                mime="text/plain"
            )

    with st.form(key="math_form", clear_on_submit=True):
        user_input = st.text_area(
            "📝 Enter your math problem here:",
            height=100,
            placeholder="Example: Solve x² + 5x + 6 = 0 or Find the integral of 2x + 3",
            key=f"user_input_{st.session_state.input_key_mm}"
        )
        col1, col2 = st.columns([3, 1])
        with col1:
            submitted = st.form_submit_button("🧮 Solve Problem", use_container_width=True)
        with col2:
            difficulty = st.selectbox("Level", ["Basic", "Intermediate", "Advanced"], index=1)

        if submitted and user_input.strip():
            enhanced_prompt = f"[{difficulty} Level] {user_input.strip()}"
            with st.spinner("🧮 Solving your math problem..."):
                response = generate_math_response(enhanced_prompt)
            st.session_state.history_mm.insert(0, {"question": user_input.strip(), "answer": response, "difficulty": difficulty})
            st.session_state.input_key_mm += 1
            st.experimental_rerun()
        elif submitted and not user_input.strip():
            st.warning("⚠️ Please enter a math problem before clicking Solve Problem.")

    if st.session_state.history_mm:
        st.markdown("### 🧮 Solution History (Latest First)")
        for idx, qa in enumerate(st.session_state.history_mm):
            question_num = len(st.session_state.history_mm) - idx
            difficulty_badge = f"[{qa.get('difficulty','N/A')}]"
            st.markdown(f"**Problem {question_num} {difficulty_badge}:** {qa['question']}")
            st.markdown(f"**Solution {question_num}:**\n{qa['answer']}")

# -------- Safe AI Image Generator --------
def run_safe_ai_image_generator():
    st.title("🖼️ Safe AI Image Generator")
    st.write("Enter a description to generate a safe and responsible AI image using Gemini 2.0 Flash.")

    def is_prompt_safe(prompt: str) -> bool:
        forbidden_keywords = [
            "violence", "weapon", "gun", "blood", "nude", "porn", "drugs", "hate", "racism", "sex",
            "terror", "bomb", "abuse", "kill", "death", "suicide", "self-harm", "hate speech"
        ]
        pattern = re.compile("|".join(forbidden_keywords), re.IGNORECASE)
        return not bool(pattern.search(prompt))

    def generate_image(prompt: str):
        if not is_prompt_safe(prompt):
            return None, "⚠️ Your prompt contains restricted or unsafe content. Please modify and try again."
        try:
            model = "gemini-2.0-flash-preview-image-generation"
            contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
            config_params = types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
                response_mime_type="text/plain"
            )
            for chunk in client.models.generate_content_stream(
                model=model,
                contents=contents,
                config=config_params,
            ):
                if (chunk.candidates is None or
                    chunk.candidates[0].content is None or
                    chunk.candidates[0].content.parts is None):
                    continue
                if (chunk.candidates[0].content.parts[0].inline_data and
                    chunk.candidates[0].content.parts[0].inline_data.data):
                    inline_data = chunk.candidates[0].content.parts[0].inline_data
                    data_buffer = inline_data.data
                    image = Image.open(BytesIO(data_buffer))
                    return image, None
                elif chunk.text:
                    continue
            return None, "No image was generated in the response."
        except Exception as e:
            return None, f"Error during image generation: {str(e)}"

    with st.form(key="image_gen_form"):
        prompt = st.text_area(
            "Image Description:",
            height=120,
            placeholder="Describe the image you want to generate... Be specific for better results!"
        )
        submit = st.form_submit_button("Generate Image")
        if submit:
            if not prompt.strip():
                st.warning("⚠️ Please enter an image description.")
            else:
                with st.spinner("Generating image... This may take a few moments."):
                    image, error = generate_image(prompt.strip())
                if error:
                    st.error(error)
                elif image:
                    st.image(image, caption="Generated Image", use_container_width=True)
                    st.session_state.generated_image = image
                else:
                    st.error("Failed to generate image. Please try again with a different prompt.")

    if "generated_image" in st.session_state and st.session_state.generated_image:
        buf = BytesIO()
        st.session_state.generated_image.save(buf, format='PNG')
        byte_im = buf.getvalue()
        st.download_button(
            label="💾 Download Generated Image",
            data=byte_im,
            file_name="ai_generated_image.png",
            mime="image/png",
            help="Click to download the generated image"
        )

# -------- Main App --------
def main():
    st.set_page_config(page_title="AI Master Suite", layout="centered")
    st.sidebar.title("Choose AI Feature")
    option = st.sidebar.selectbox("", [
        "AI Teaching Assistant",
        "Math Mastermind",
        "Safe AI Image Generator"
    ])

    if option == "AI Teaching Assistant":
        run_ai_teaching_assistant()
    elif option == "Math Mastermind":
        run_math_mastermind()
    elif option == "Safe AI Image Generator":
        run_safe_ai_image_generator()

if __name__ == "__main__":
    main()
