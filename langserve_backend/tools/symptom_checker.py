from langchain.tools import tool

@tool
def check_symptom(symptom):
    """This langchain tool will analyze the input symptom text and return the relevent medical category"""
    symptom = symptom.lower()

    if "fever" in symptom or "body ache" in symptom or "chills" in symptom:
        return "infection"
    elif "throat" in symptom or "cough" in symptom:
        return "respiratory"
    elif "headache" in symptom or "dizzy" in symptom:
        return "neurological"
    elif "stomach" in symptom or "nausea" in symptom :
        return "gastrointestinal"
    else:
        return "general examination is required"
    
