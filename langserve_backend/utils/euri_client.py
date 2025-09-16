import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

def euri_chat_completion(messages, model="gpt-4.1-nano", temprature = 0.7,max_tokens=100):
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization" : f"Bearer {API_KEY}",
        "Content-Type" : "application/json"
    }
    payload = {
        "model" : model,
        "messages" : messages,
        "temprature" : temprature,
        "max_tokens" : max_tokens
    }

    response = requests.post(url,headers=headers,json=payload)
    return response.json()["choices"][0]["message"]["content"]


