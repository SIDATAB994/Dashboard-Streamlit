import streamlit as st
import requests

st.set_page_config(page_title="📊 Betting Bot", layout="wide")
st.title("📊 Betting Bot Dashboard")

# Remplacer par ton URL publique Railway du bot Flask
BOT_URL = "https://TON-BOT-FLASK.up.railway.app"

if st.button("🔄 Générer les paris du jour"):
    try:
        requests.get(f"{BOT_URL}/run", timeout=5)
        st.success("Paris générés !")
    except:
        st.error("Impossible de générer les paris. Vérifie le bot Flask.")

try:
    response = requests.get(f"{BOT_URL}/bets", timeout=5)
    data = response.json()
    st.subheader(f"📅 Paris du {data.get('date','aujourd\'hui')}")

    st.markdown("### 🎯 Simple")
    st.write(data.get("simple",{}))

    st.markdown("### 🔗 Combo")
    for bet in data.get("combo",[]):
        st.write(bet)

except:
    st.error("Impossible de récupérer les paris du bot Flask.")
