import streamlit as st
from ai_handler import generate_response

# Streamlit UI
st.set_page_config(page_title="Smart Email Responder", layout="centered")

st.title("📩 Smart Email Responder")
st.markdown("Generate professional email responses instantly with AI.")

# User Input
email_input = st.text_area("✉️ Paste your email here", height=200)

# Tone Selection
tone = st.radio("Select Response Tone:", ["Formal", "Neutral", "Friendly"], horizontal=True)

# Generate Button
if st.button("✨ Generate Response"):
    if email_input.strip():
        with st.spinner("Generating response..."):
            response = generate_response(email_input, tone.lower())
        st.subheader("🤖 AI Generated Response:")
        st.code(response, language="markdown")
    else:
        st.warning("⚠️ Please enter an email text before generating a response.")
