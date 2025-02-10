from pages.base_page import BasePage
from pages.auth_page import AuthPage

import time
import pytest


class TestBasePageFromMainPage():
    def test_check_visible_on_page(self, browser) -> None:
        link = "https://dude-yoga.fitbase.io/"
        auth_page = AuthPage(browser, link)
        auth_page.open()
        auth_page.auth_on_page()
        # Проверка отображения элементов на странице
        page = BasePage(browser, browser.current_url)
        page.should_be_user_icon()
        page.should_be_header_idea()
        page.should_be_header_knowleage_base()
        page.should_be_fast_client_search()
        page.should_be_fast_client_button()
        page.should_be_open_clients_reception()

    @pytest.mark.xfail(strict=False, reason="The test may fail due to the lack of a limit banner on the page!")
    def test_check_visible_limit_banner_on_page(self, browser) -> None:
        link = "https://dude-yoga.fitbase.io/"
        auth_page = AuthPage(browser, link)
        auth_page.open()
        auth_page.auth_on_page()
        page = BasePage(browser, browser.current_url)
        # Проверка отображения баннера о превышении лимита
        page.should_be_banner_header_limit()

    @pytest.mark.xfail(strict=False, reason="The test may fail due to the lack of a club change on the page!")
    def test_check_visible_change_club_on_page(self, browser) -> None:
        link = "https://dude-yoga.fitbase.io/"
        auth_page = AuthPage(browser, link)
        auth_page.open()
        auth_page.auth_on_page()
        page = BasePage(browser, browser.current_url)
        # Проверка отображения смены филиала
        page.should_be_change_club()

    def test_user_can_click_on_username(self, browser) -> None:
        link = "https://dude-yoga.fitbase.io/"
        auth_page = AuthPage(browser, link)
        auth_page.open()
        auth_page.auth_on_page()
        page = BasePage(browser, browser.current_url)
        # Проверка нажатия на иконку пользователя
        page.click_on_user_icon()
        
