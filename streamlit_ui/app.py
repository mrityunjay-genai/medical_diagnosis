import streamlit as st
import requests

st.title(" AI Medical Diagnostics Assistant")

symptom_input = st.text_area("Describe your Symptoms")

if st.button("Get Diagnosis"):
    state_input = {
        "input" : symptom_input,
        "symptom_area" : "",
        "diagnosis" : ""
    }

    try:
    # for local
        response = requests.post(
            "http://localhost:8000/diagnose/invoke",
            headers = {"Content-Type":"application/json"},
            json = {"input":state_input}
        )

        data = response.json()
        
        # st.write("DEBUG raw JSON:", data)

        st.subheader("Symptom Area Detected")
        st.write(data.get("symptom_area", data["output"]['symptom_area']))

        st.subheader("AI Diagnosis Sugestion")
        st.write(data.get("diagnosis", data["output"]['diagnosis']))


    except Exception as e:
        st.error(f"Failed to get diagnosis : {e}")


