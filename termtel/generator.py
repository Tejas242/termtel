from json import load
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
API_KEY=os.environ.get("GENAI_API_KEY")


genai.configure(api_key=API_KEY)

def generate(query):
    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    prompt_parts = [
    "Give the proper terminal command to execute for the query.",
    "input: how to list all files with details",
    "output: ls -l",
    "input: change directory to Downloads",
    "output: cd Downloads",
    f"input: {query}",
    "output: ",
    ]

    response = model.generate_content(prompt_parts)
    return response.text