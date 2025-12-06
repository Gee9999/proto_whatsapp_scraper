import streamlit as st
from scraper.whatsapp import open_whatsapp

st.set_page_config(page_title="Proto WhatsApp Scraper (Selenium)", page_icon="📸", layout="centered")

st.title("📸 Proto WhatsApp Photo Scraper (Selenium)")

st.write("This tool opens WhatsApp Web using Selenium so you can scrape photos from a selected chat.")

st.markdown("""
### Before You Start:
1. Make sure Google Chrome is installed.
2. The app will open a new Chrome window.
3. Scan the QR code on WhatsApp Web.
4. Select the chat you want to scrape.
""")

if st.button("Open WhatsApp Web"):
    st.success("Launching WhatsApp Web...")
    open_whatsapp()
else:
    st.info("Click the button above to start.")
