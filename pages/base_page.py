from typing import Any


class BasePage:
    def __init__(self, browser, url, timeout=10) -> None:
        self.browser: Any = browser
        self.url: Any = url
        self.browser.implicitly_wait(timeout)