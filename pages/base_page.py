from dotenv import load_dotenv
from selenium.common.exceptions import (
    NoSuchElementException, 
    TimeoutException, 
    NoAlertPresentException
)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from .locators import BasePageLocators

from typing import Any
import os
import logging


load_dotenv()

# Настройка логирования
BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR: str = os.path.dirname(BASE_DIR)
LOG_FILE: str = os.path.join(ROOT_DIR, "test_log.log")
logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOG_FILE, mode='a', encoding='utf-8')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class BasePage:
    def __init__(self, browser, url, timeout=10) -> None:
        self.browser: Any = browser
        self.url: Any = url
        self.browser.implicitly_wait(timeout)
        self.login: str | None = os.getenv("LOGIN")
        self.password: str | None = os.getenv("PASSWORD")

    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, how, what) -> bool:
        """
        Проверка на наличие элемента на странице
        """
        try:
            self.browser.find_element(how, what)
            logger.info(f"✅ Элемент найден: {what}")
        except NoSuchElementException:
            logger.warning(f"⚠️ Элемент НЕ найден: {what}")
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4) -> bool:
        """
        Проверка, что элемент не появиться через определенное время
        """
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
            logger.info(f"✅ Элемент появился: {what}")
        except TimeoutException:
            logger.info(f"⚠️ Элемент НЕ появился: {what}")
            return True
        return False

    def is_disappeared(self, how, what, timeout=4) -> bool:
        """
        Проверка, что какой-то элемент исчезнет через определенное время
        """
        try:
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]).until_not(ec.presence_of_element_located((how, what)))
            logger.info(f"✅ Элемент исчез: {what}")
        except TimeoutException:
            logger.warning(f"⚠️ Элемент НЕ исчез: {what}")
            return False
        return True
    
    def should_be_user_icon(self) -> None:
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not visible on page!"

    def should_be_change_club(self) -> None:
        assert self.is_element_present(*BasePageLocators.CHANGE_CLUB_FORM), "Change club button is not visible on page!"

    def should_be_header_idea(self) -> None:
        assert self.is_element_present(*BasePageLocators.HEADER_IDEA), "Header idea is not visible on page!"

    def should_be_header_knowleage_base(self) -> None:
        assert self.is_element_present(*BasePageLocators.HEADER_KNOWLEAGE_BASE), "Header knowleage base is not visible on page!"

    def should_be_banner_header_limit(self) -> None:
        assert self.is_element_present(*BasePageLocators.BANNER_HEADER_LIMIT), "Banner header limit is not visible on page!"

    def should_be_fast_client_search(self) -> None:
        assert self.is_element_present(*BasePageLocators.FAST_CLIENT_SEARCH), "Fast client search is not visible on page!"

    def should_be_fast_client_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.FAST_CLIENT_BUTTON), "Fast client button is not visible on page!"

    def should_be_open_clients_reception(self) -> None:
        assert self.is_element_present(*BasePageLocators.OPEN_CLIENTS_RECEPTION), "Open clients reception is not visible on page!"

    def click_on_user_icon(self) -> None:
        link = self.browser.find_element(*BasePageLocators.USER_ICON)
        link.click()