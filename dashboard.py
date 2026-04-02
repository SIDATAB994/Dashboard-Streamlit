import streamlit as st
import requests
from datetime import date

st.set_page_config(page_title="Betting AI Pro", layout="wide")

st.title("🤖 Betting AI Pro")

BOT_URL = "https://bot-flask-e3848ed3063c719336b32e0b4861c7d9.up.railway.app"

selected_date = st.date_input("📅 Choisir une date", date.today())

if st.button("🚀 Générer combiné"):
    st.info("Analyse en cours...")

try:
    data = requests.get(f"{BOT_URL}/bets", params={"date": selected_date}, timeout=10).json()

    st.subheader("🎯 Pari Simple")

    simple = data.get("simple", {})
    st.metric("Match", simple.get("match", "-"))
    st.write(simple)

    st.subheader("🔥 Combiné optimisé")

    cols = st.columns(3)

    for i, bet in enumerate(data.get("combo", [])):
        with cols[i]:
            st.markdown(f"### {bet['match']}")
            st.write(f"Type: {bet['type']}")
            st.write(f"Choix: {bet['prediction']}")
            st.write(f"Cote: {bet['odd']}")
            st.write(f"Confiance: {bet['confidence']}%")

except:
    st.error("Erreur connexion bot")
