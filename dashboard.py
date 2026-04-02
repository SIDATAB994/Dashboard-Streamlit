import streamlit as st
import requests

st.set_page_config(page_title="📊 Betting Bot", layout="wide")
st.title("📊 Betting Bot Dashboard")

# URL publique de ton bot Flask (à remplacer par ton URL Railway)
BOT_URL = "https://TON-BOT-FLASK.up.railway.app"

# Bouton pour générer de nouveaux paris
if st.button("🔄 Générer les paris du jour"):
    requests.get(f"{BOT_URL}/run")
    st.success("Paris générés !")

try:
    data = requests.get(f"{BOT_URL}/bets").json()

    st.subheader(f"📅 Paris du {data.get('date', 'aujourd\'hui')}")

    st.markdown("### 🎯 Simple")
    st.write(data.get("simple", {}))

    st.markdown("### 🔗 Combo")
    for bet in data.get("combo", []):
        st.write(bet)

except:
    st.error("Bot non lancé ou URL BOT incorrect")
