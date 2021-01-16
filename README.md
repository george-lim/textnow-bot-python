# TextNow Bot

[![pypi](https://img.shields.io/pypi/v/textnow-bot)](https://pypi.org/project/textnow-bot)
![pyversions](https://img.shields.io/pypi/pyversions/textnow-bot)
[![ci](https://github.com/george-lim/textnow-bot-python/workflows/CI/badge.svg)](https://github.com/george-lim/textnow-bot-python/actions)
[![license](https://img.shields.io/github/license/george-lim/textnow-bot-python)](https://github.com/george-lim/textnow-bot-python/blob/main/LICENSE)

## [Usage](#usage) | [Features](#features) | [Examples](#examples) | [CI/CD](#cicd)

TextNow Bot is a Python library to send text messages on TextNow with the [Playwright API](https://microsoft.github.io/playwright-python).

## Usage

```bash
python3 -m pip install textnow-bot
python3 -m playwright install
```

This installs TextNow Bot and its dependencies. Once installed, add `import textnow_bot` to a Python script to begin using TextNow Bot.

## Features

TextNow Bot accepts either account credentials or existing login cookies to authenticate the user. It allows users to send messages programmatically to various recipients.

## Examples

### Send a message

This snippet logs into TextNow and sends a message to a recipient.

```python
from playwright import sync_playwright
from textnow_bot import TextNowBot

username = "test@example.com"
password = "********"
recipient = "123-456-7890"
message = "Hello world!"

with sync_playwright() as api:
    browser = None

    try:
        browser = api.firefox.launch()
        page = browser.newPage()

        bot = TextNowBot(page, None, username, password)
        bot.send_message(recipient, message)

        browser.close()
    except Exception:
        if browser:
            browser.close()

        raise
```

### Login session persistence

This snippet shows how to persist and restore login sessions with cookies.

```python
cookies_path = pathlib.Path('/tmp/cookies.json')

# Persist `cookies` to `cookies_path`
bot = TextNowBot(page, None, username, password)
cookies = bot.get_cookies()
cookies_path.write_text(json.dumps(cookies))

# Restore `cookies` from `cookies_path`
cookies = json.loads(cookies_path.read_text())
bot = TextNowBot(page, cookies)
```

## CI/CD

### Secrets

```yaml
PYPI_USERNAME: '__token__'
PYPI_PASSWORD: '********'

TESTPYPI_USERNAME: '__token__'
TESTPYPI_PASSWORD: '********'
```

These secrets must exist in the repository for `CD` workflows to publish the PyPI package.
