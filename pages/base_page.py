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
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4) -> bool:
        """
        Проверка, что элемент не появиться через определенное время
        """
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4) -> bool:
        """
        Проверка, что какой-то элемент исчезнет через определенное время
        """
        try:
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]).until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def should_be_user_icon(self) -> None:
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not visible on page!"

    def click_on_user_icon(self) -> None:
        link = self.browser.find_element(*BasePageLocators.USER_ICON)
        link.click()