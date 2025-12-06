
import streamlit as st
from scraper.whatsapp import open_whatsapp

st.title("Proto WhatsApp Scraper")

if st.button("Open WhatsApp Web"):
    st.write("Launching WhatsApp...")
    open_whatsapp()
