import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def query_gemini(prompt: str) -> str:
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction="You are a helpful legal assistant."
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)

    return response.text
