import logging

TEXTNOW_URL = "https://www.textnow.com"
PERMISSION_COOKIE = {"name": "PermissionPriming", "value": "-1", "url": TEXTNOW_URL}


class TextNowBot:
    def __init__(self, page):
        self.page = page
        self._is_logged_in = False

    @property
    def is_logged_in(self):
        return self._is_logged_in

    @property
    def cookies(self):
        return self.page.context.cookies(TEXTNOW_URL)

    def log_in(self, cookies=None, username=None, password=None):
        if cookies:
            logging.info("Logging in with cookies...")
            self.page.context.add_cookies(cookies)
            self.page.goto(f"{TEXTNOW_URL}/login", wait_until="networkidle")
        elif username and password:
            logging.info("Logging in with account credentials...")
            self.page.context.clear_cookies()

            self.page.goto(f"{TEXTNOW_URL}/login")
            self.page.type("#txt-username", username)
            self.page.type("#txt-password", password)
            self.page.click("#btn-login")
            self.page.wait_for_load_state("networkidle")

            self.page.context.add_cookies([PERMISSION_COOKIE])
        else:
            raise Exception("missing account credentials")

        if "/messaging" not in self.page.url:
            raise Exception("authentication failed")

        self._is_logged_in = True

    def send_text_message(self, recipient, message):
        if not self.is_logged_in:
            raise Exception("authentication failed")

        logging.info("Sending text message...")

        self.page.goto(f"{TEXTNOW_URL}/messaging")
        self.page.click("#newText")

        self.page.type(".newConversationTextField", recipient)
        self.page.press(".newConversationTextField", "Enter")

        self.page.type("#text-input", message)
        self.page.press("#text-input", "Enter")
        self.page.wait_for_timeout(500)


class AsyncTextNowBot(TextNowBot):
    async def log_in(self, cookies=None, username=None, password=None):
        if cookies:
            logging.info("Logging in with cookies...")
            await self.page.context.add_cookies(cookies)
            await self.page.goto(f"{TEXTNOW_URL}/login", wait_until="networkidle")
        elif username and password:
            logging.info("Logging in with account credentials...")
            await self.page.context.clear_cookies()

            await self.page.goto(f"{TEXTNOW_URL}/login")
            await self.page.type("#txt-username", username)
            await self.page.type("#txt-password", password)
            await self.page.click("#btn-login")
            await self.page.wait_for_load_state("networkidle")

            await self.page.context.add_cookies([PERMISSION_COOKIE])
        else:
            raise Exception("missing account credentials")

        if "/messaging" not in self.page.url:
            raise Exception("authentication failed")

        self._is_logged_in = True

    async def send_text_message(self, recipient, message):
        if not self.is_logged_in:
            raise Exception("authentication failed")

        logging.info("Sending text message...")

        await self.page.goto(f"{TEXTNOW_URL}/messaging")
        await self.page.click("#newText")

        await self.page.type(".newConversationTextField", recipient)
        await self.page.press(".newConversationTextField", "Enter")

        await self.page.type("#text-input", message)
        await self.page.press("#text-input", "Enter")
        await self.page.wait_for_timeout(500)
