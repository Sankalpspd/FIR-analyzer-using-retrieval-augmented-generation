import os
import google.generativeai as genai


# Set your API key
genai.configure(api_key=GEMINI_API_KEY)

def query_gemini(prompt: str) -> str:
    # Use GenerativeModel for the latest API
    model = genai.GenerativeModel(
        model_name='gemini-2.5-flash', # Using flash for faster response, can be changed to pro
        system_instruction="You are a helpful legal assistant."
    )
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    return response.text
