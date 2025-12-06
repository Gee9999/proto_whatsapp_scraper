import streamlit as st
import threading
import sys
import asyncio
from scraper.whatsapp import open_whatsapp

# Windows event-loop fix
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

st.set_page_config(page_title="Proto WhatsApp Scraper", page_icon="💬")

st.title("💬 Proto WhatsApp Scraper (Stable Version)")

def run_playwright():
    open_whatsapp()

if st.button("Open WhatsApp Web"):
    threading.Thread(target=run_playwright, daemon=True).start()
    st.success("Launching WhatsApp…")
else:
    st.info("Waiting for action…")
