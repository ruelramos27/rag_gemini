from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()  # Loads .env file

API_KEY = os.getenv("GOOGLE_API_KEY")  

if not API_KEY:
    raise ValueError("🚫 Missing GOOGLE_API_KEY. Did you load .env properly?")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")

def query_gemini(context, question):
    prompt = f"""Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""
    response = model.generate_content(prompt)
    return response.text