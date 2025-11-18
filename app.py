import streamlit as st
import openai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Support Assistant",
    page_icon="💼",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
        body {
            background-color: #f4f6fa;
        }

        .main-container {
            background: white;
            padding: 35px;
            border-radius: 18px;
            box-shadow: 0 4px 25px rgba(0, 0, 0, 0.08);
            margin-top: 25px;
        }

        h1 {
            text-align: center;
            font-size: 34px !important;
            font-weight: 700 !important;
            margin-bottom: 0px;
        }

        .sub {
            text-align: center;
            font-size: 16px;
            color: #6c757d;
            margin-bottom: 30px;
        }

        textarea {
            border-radius: 15px !important;
        }

        .result-box {
            background: #f8f9fc;
            padding: 20px;
            border-radius: 15px;
            border-left: 5px solid #4a90e2;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("<h1>💼 AI Email Support Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub'>Analyze support emails or screenshots → Detect issue → Generate reply automatically</p>", unsafe_allow_html=True)

# ---------- INPUT ----------
email_input = st.text_area("📩 Paste user email here:", height=200)

uploaded_img = st.file_uploader("📷 Upload screenshot (optional)", type=["png", "jpg", "jpeg"])

generate = st.button("⚡ Generate AI Response", use_container_width=True)


# ---------- LOGIC ----------
if generate:

    # Extract text from screenshot (if uploaded)
    extracted_text = ""
    if uploaded_img:
        st.info("🔍 Extracting text from screenshot...")

        img_bytes = uploaded_img.read()

        # Vision prompt
        vision_prompt = """
        Extract all visible text from this screenshot.
        Return ONLY the text, no explanation.
        """

        try:
            vision_response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": vision_prompt},
                    {"role": "user", "content": [{"image": img_bytes, "mime_type": "image/png"}]}
                ]
            )

            extracted_text = vision_response.choices[0].message.content
            st.success("📄 Text extracted from screenshot!")

        except Exception as e:
            st.error(f"Image extraction error: {e}")

    # Combine email + extracted text
    final_input = email_input + "\n" + extracted_text

    if final_input.strip() == "":
        st.warning("Please paste an email or upload an image.")
    else:
        with st.spinner("Thinking..."):

            prompt = f"""
            You are an IT Support Assistant.
            Analyze the following content and provide:

            1. Issue Type  
            2. Severity (Low/Medium/High)  
            3. Step-by-step troubleshooting  
            4. A professional auto-reply  

            User Content:
            {final_input}
            """

            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            output = response.choices[0].message.content

        st.markdown("<h3>🧠 AI-Generated Response</h3>", unsafe_allow_html=True)
        st.markdown(f"<div class='result-box'>{output}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<br><hr><p style='text-align: center; color: #6c757d;'>Developed by Krishna Murthi</p>", unsafe_allow_html=True)