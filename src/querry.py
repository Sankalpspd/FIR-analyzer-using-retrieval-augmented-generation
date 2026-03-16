import os
import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

def query_gemini(prompt):
    genai.ChatCompletion.create(
    model="gemini-1.5",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize this FIR."}
    ],)
    # Extract the text from response
    return response.last_message.content
