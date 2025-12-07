import streamlit as st
from scraper.engine import open_whatsapp

st.title("WhatsApp Photo Saver - FAST MODE")

if st.button("Launch WhatsApp Web"):
    open_whatsapp()
    st.success("WhatsApp window opened. Scan QR in Chrome.")
