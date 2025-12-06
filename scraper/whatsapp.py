
from playwright.sync_api import sync_playwright

def open_whatsapp():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://web.whatsapp.com")
        page.wait_for_timeout(30000)
        browser.close()
