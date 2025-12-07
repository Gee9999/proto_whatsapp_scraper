import streamlit as st
from scraper.engine import open_whatsapp
from scraper.engine import download_photos

st.set_page_config(page_title="Proto Photo Saver", layout="wide")

st.title("📸 Proto Photo Saver")
st.write("Open WhatsApp Web and select the chat you want to download photos from.")

# Start WhatsApp
if "driver" not in st.session_state:
    st.session_state.driver = open_whatsapp()

if st.button("📥 Download Photos From Chat"):
    count = download_photos(st.session_state.driver)
    st.success(f"Downloaded {count} photos!")
