import streamlit as st
import asyncio
from scraper.whatsapp import open_whatsapp_async

st.set_page_config(page_title="WhatsApp Scraper", page_icon="💬", layout="centered")
st.title("💬 Proto WhatsApp Scraper")

st.write("Click the button to launch WhatsApp.")

if st.button("Open WhatsApp Web"):
    st.success("Launching WhatsApp…")
    asyncio.run(open_whatsapp_async())
else:
    st.info("Waiting for user action…")
