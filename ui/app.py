import streamlit as st
import requests

st.title("Real-Time Financial News Monitoring")

news_text = st.text_area("Enter Financial News Text")
if st.button("Summarize"):
    response = requests.post("http://localhost:8000/summarize/", json={"text": news_text})
    if response.status_code == 200:
        result = response.json()
        st.subheader("Summary")
        st.write(result["summary"])
        st.subheader("Compliance Risks")
        st.write(", ".join(result["risks"]))
