import streamlit as st
from scraper.whatsapp import open_whatsapp

st.set_page_config(page_title="Proto WhatsApp Scraper", page_icon="💬")

st.title("💬 Proto WhatsApp Scraper (Sync Playwright Version)")

st.write("Click the button below to launch WhatsApp Web.")

if st.button("Open WhatsApp Web"):
    st.success("Launching WhatsApp…")
    open_whatsapp()
else:
    st.info("Waiting for user action…")
