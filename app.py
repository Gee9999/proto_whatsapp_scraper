import streamlit as st
from scraper.whatsapp import open_whatsapp

st.set_page_config(page_title="Proto WhatsApp Scraper", page_icon="💬", layout="centered")

st.title("💬 Proto WhatsApp Scraper")

st.write("Click the button below to launch WhatsApp Web using Playwright.")

# IMPORTANT: Do NOT run Playwright at import time!
# Only trigger WhatsApp when button is clicked.

if st.button("Open WhatsApp Web"):
    st.success("Launching WhatsApp…")
    open_whatsapp()
else:
    st.info("Waiting for user action…")
