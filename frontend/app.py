import streamlit as st
import requests

st.set_page_config(page_title="Diag-Raida", page_icon="🎯", layout="centered")

st.title("🎯 Diag-Raida")
st.subheader("Diagnostiquer, Comprendre, Réapprendre")

st.write("Bienvenue sur Diag-Raida — un outil intelligent pour diagnostiquer vos compétences en mathématiques.")

if st.button("Tester l'API Backend"):
    try:
        response = requests.get("http://localhost:5000/api/evaluation/")
        st.success(f"Backend says: {response.json()['message']}")
    except Exception as e:
        st.error(f"Could not reach backend: {e}")
