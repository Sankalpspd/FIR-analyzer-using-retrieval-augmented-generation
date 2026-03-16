import os
import google.generativeai as genai


# Set your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def query_gemini(prompt):
    response = genai.ChatCompletion.create(
        model="gemini-1.5",
        messages=[
            {"role": "system", "content": "You are a helpful legal assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["candidates"][0]["content"]
