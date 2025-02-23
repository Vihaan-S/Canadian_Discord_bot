from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def gemini_api(input_text):

    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents={
            input_text,
            "given this message from the user, respond in a and in a nice and very steriotypical Canadian way"
        }   
    )
    
    return response.text
