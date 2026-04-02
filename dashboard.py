import streamlit as st
import requests
from datetime import date

st.set_page_config(page_title="📊 Betting Bot", layout="wide")
st.title("📊 Betting Bot Dashboard")

BOT_URL = "https://bot-flask-e3848ed3063c719336b32e0b4861c7d9.up.railway.app"  # Remplacer par ton URL Railway

# Sélection de la date
selected_date = st.date_input("Sélectionner une date pour le combiné", date.today())

if st.button("🔄 Générer les paris"):
    try:
        requests.get(f"{BOT_URL}/run", timeout=10)
        st.success("Paris générés !")
    except:
        st.error("Impossible de générer les paris. Vérifie le bot Flask.")

# Récupérer les paris pour la date sélectionnée
try:
    response = requests.get(f"{BOT_URL}/bets", params={"date": selected_date}, timeout=10)
    data = response.json()

    st.subheader(f"📅 Paris pour le {data.get('date', str(selected_date))}")

    st.markdown("### 🎯 Simple")
    st.write(data.get("simple", {}))

    st.markdown("### 🔗 Combo")
    for bet in data.get("combo", []):
        st.write(bet)

except:
    st.error("Impossible de récupérer les paris du bot Flask.")
