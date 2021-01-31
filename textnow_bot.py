import logging
import inspect
import asyncio

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
            raise Exception("authentication failed (did not reach textnow.com/messaging")

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


# Code for Async Below

class AsyncMeta(type):
    async def __call__(cls, *args, **kwargs):
        obb = object.__new__(cls)
        fn = obb.__init__(*args, **kwargs)
        if inspect.isawaitable(fn):
            await fn
        return obb

class AsyncTextNowBot(metaclass=AsyncMeta):
    async def __init__(self, page, cookies=None, username=None, password=None):
        self.page = page

        if cookies:
            logging.info("Async logging in with cookies...")
            await page.context.addCookies(cookies)
            await page.goto(f"{TEXTNOW_URL}/login", waitUntil="networkidle")
        elif username and password:
            logging.info("Async logging in with account info...")
            await page.context.clearCookies()

            await page.goto(f"{TEXTNOW_URL}/login")
            await page.type("#txt-username", username)
            await page.type("#txt-password", password)
            await page.click("#btn-login")
            await page.waitForNavigation()

            await page.context.addCookies([PERMISSION_COOKIE])
        else:
            raise Exception("missing authentication info")

        if "/messaging" not in page.url:
            # Added more information to error message
            raise Exception("authentication failed (did not reach textnow.com/messaging)")

    async def get_cookies(self):
        return await self.page.context.cookies(TEXTNOW_URL)

    async def send_message(self, recipient, message):
        logging.info("Async sending message...")

        await self.page.goto(f"{TEXTNOW_URL}/messaging")
        await self.page.click("#newText")

        await self.page.type(".newConversationTextField", recipient)
        await self.page.press(".newConversationTextField", "Enter")

        await self.page.type("#text-input", message)
        await self.page.press("#text-input", "Enter")
        await self.page.waitForTimeout(500)