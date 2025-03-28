import google.generativeai as genai
from config import GEMINI_API_KEY

# Configuring Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def generate_response(email_text, tone="neutral"):
    """Generates an AI-crafted response to an email with a specified tone."""
    tone_mapping = {
        "formal": "Write a highly professional and polite response.",
        "neutral": "Write a clear and concise response.",
        "friendly": "Write a warm and approachable response."
    }

    # Ensuring a valid tone is selected
    tone_instruction = tone_mapping.get(tone, tone_mapping["neutral"])

    # Constructing the prompt
    prompt = f"{tone_instruction}\n\nEmail:\n{email_text}"

    try:
        # Generating AI response
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"Error: {str(e)}"
