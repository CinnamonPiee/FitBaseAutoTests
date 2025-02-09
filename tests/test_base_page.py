from pages.base_page import BasePage
from pages.auth_page import AuthPage

import time


class TestBasePageFromMainPage():
    def test_user_can_click_on_username(self, browser) -> None:
        link = "https://dude-yoga.fitbase.io/"
        auth_page = AuthPage(browser, link)
        auth_page.open()
        auth_page.auth_on_page()
        page = BasePage(browser, browser.current_url)
        page.should_be_user_icon()
        page.click_on_user_icon()
        
