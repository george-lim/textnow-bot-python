import logging

TEXTNOW_URL = "https://www.textnow.com"
PERMISSION_COOKIE = {"name": "PermissionPriming", "value": "-1", "url": TEXTNOW_URL}


class TextNowBot:
    def __init__(self, page, cookies=None, username=None, password=None):
        self.page = page

        if cookies:
            logging.info("Logging in with cookies...")
            page.context.addCookies(cookies)
            page.goto(f"{TEXTNOW_URL}/login", waitUntil="networkidle")
        elif username and password:
            logging.info("Logging in with account info...")
            page.context.clearCookies()

            page.goto(f"{TEXTNOW_URL}/login")
            page.type("#txt-username", username)
            page.type("#txt-password", password)
            page.click("#btn-login")
            page.waitForNavigation()

            page.context.addCookies([PERMISSION_COOKIE])
        else:
            raise Exception("missing authentication info")

        if "/messaging" not in page.url:
            raise Exception("authentication failed")

    def get_cookies(self):
        return self.page.context.cookies(TEXTNOW_URL)

    def send_message(self, recipient, message):
        logging.info("Sending message...")

        self.page.goto(f"{TEXTNOW_URL}/messaging")
        self.page.click("#newText")

        self.page.type(".newConversationTextField", recipient)
        self.page.press(".newConversationTextField", "Enter")

        self.page.type("#text-input", message)
        self.page.press("#text-input", "Enter")
        self.page.waitForTimeout(500)
