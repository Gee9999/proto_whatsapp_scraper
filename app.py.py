import streamlit as st
from scraper.whatsapp import open_whatsapp

st.set_page_config(page_title="Proto WhatsApp Scraper", page_icon="💬", layout="centered")

st.title("💬 Proto WhatsApp Scraper")

st.write("Click the button below to launch WhatsApp Web using Playwright.")

if st.button("Open WhatsApp Web"):
    st.success("Launching WhatsApp…")
    open_whatsapp()
