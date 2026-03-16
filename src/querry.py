import os
import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

def query_gemini(prompt):
    response = genai.chat.create(
        model="gemini-1.5",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    # Extract the text from response
    return response.last.content
