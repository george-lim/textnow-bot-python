import os

from playwright.sync_api import sync_playwright
from textnow_bot import TextNowBot


def run(playwright):
    username = os.environ["SCHEDULE_TEXTNOW_USERNAME"]
    password = os.environ["SCHEDULE_TEXTNOW_PASSWORD"]
    recipient = os.environ["SCHEDULE_TEXTNOW_RECIPIENT"]
    message = "It's the weekend!"

    browser = None

    try:
        browser = playwright.firefox.launch()
        page = browser.new_page()

        bot = TextNowBot(page)

        bot.log_in(None, username, password)
        bot.send_text_message(recipient, message)

        browser.close()
    except Exception:
        if browser:
            browser.close()

        raise


with sync_playwright() as playwright:
    run(playwright)
