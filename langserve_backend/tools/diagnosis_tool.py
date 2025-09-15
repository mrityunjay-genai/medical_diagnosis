from langchain.tools import tools
from utils.euri_client import euri_chat_completion

@tools
def ai_diagnosis(symptom_description : str) ->str:
    """Use EURI AI to diagnose based on symptoms"""
    messages = [
        {"role": "user", "content" : f"A patient reports: {symptom_description}. What are possible diagnose and steps to take"}
    ]
    return euri_chat_completion(messages)