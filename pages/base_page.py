from dotenv import load_dotenv
from selenium.common.exceptions import (
    NoSuchElementException, 
    TimeoutException,
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
    def __init__(self, browser, url, timeout=5) -> None:
        self.browser: Any = browser
        self.url: Any = url
        self.browser.implicitly_wait(timeout)
        self.login: str | None = os.getenv("LOGIN")
        self.password: str | None = os.getenv("PASSWORD")

    def open(self) -> None:
        self.browser.get(self.url)

    # Функции проверок
    def is_element_present(self, how, what) -> bool:
        """
        Проверка на наличие элемента на странице
        """
        try:
            self.browser.find_element(how, what)
            logger.info(f"✅ Элемент найден: {what}")
        except NoSuchElementException as ex:
            logger.warning(f"⚠️ Элемент НЕ найден: {what}, {ex}")
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4) -> bool:
        """
        Проверка, что элемент не появиться через определенное время
        """
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
            logger.info(f"✅ Элемент НЕ появился: {what}")
        except TimeoutException as ex:
            logger.warning(f"⚠️ Элемент появился: {what}, {ex}")
            return True
        return False

    def is_disappeared(self, how, what, timeout=4) -> bool:
        """
        Проверка, что какой-то элемент исчезнет через определенное время
        """
        try:
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]).until_not(ec.presence_of_element_located((how, what)))
            logger.info(f"✅ Элемент исчез: {what}")
        except TimeoutException as ex:
            logger.warning(f"⚠️ Элемент НЕ исчез: {what}, {ex}")
            return False
        return True
    
    def is_element_displayed(self, how, what) -> bool:
        """
        Проверка, что элемент отображается
        """
        try:
            element = self.browser.find_element(how, what)
            is_displayed = element.is_displayed()
            if is_displayed:
                logger.info(f"✅ Элемент отображается: {what}")
            else:
                logger.warning(f"⚠️ Элемент найден, но НЕ отображается: {what}")
            return is_displayed
        except NoSuchElementException as ex:
            logger.warning(f"⚠️ Элемент НЕ отображается: {what}, {ex}")
            return False

    def is_element_displayed_per_time(self, how, what, timeout=4) -> bool:
        """
        Проверка отображения элемента определенное время
        """
        try:
            WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located((how, what)))
            logger.info(f"✅ Элемент отображался в течение {timeout} секунд: {what}")
        except TimeoutException as ex:
            logger.warning(f"⚠️ Элемент НЕ отображался в течение {timeout} секунд: {what}, {ex}")
            return True
        return False

    def element_is_enabled(self, how, what) -> bool:
        """
        Проверка доступности элемента на странице
        """
        try:
            element = self.browser.find_element(how, what)
            is_enabled = element.is_enabled()
            if is_enabled:
                logger.info(f"✅ Элемент доступен: {what}")
            else:
                logger.warning(f"⚠️ Элемент найден, но НЕ доступен: {what}")
            return is_enabled
        except NoSuchElementException as ex:
            logger.warning(f"⚠️ Элемент НЕ найден: {what}, {ex}")
            return False

    def text_element_is_correct(self, how, what, text) -> bool:
        """
        Проверка корректности текста у элемента
        """
        try:
            element = self.browser.find_element(how, what)
            actual_text = element.text.strip()
            is_correct = actual_text == text
            if is_correct:
                logger.info(f"✅ Текст элемента корректен: {what} (\"{actual_text}\")")
            else:
                logger.warning(f"⚠️ Текст элемента НЕ совпадает: {what} (Ожидалось: \"{text}\", Получено: \"{actual_text}\")")
            return is_correct
        except NoSuchElementException as ex:
            logger.warning(f"⚠️ Элемент НЕ найден: {what}, {ex}")
            return False

    def is_element_attribute_correct(self, how, what, attribute, text) -> None:
        """
        Проверка атрибута элемента
        """
        try:
            element = self.browser.find_element(how, what)
            actual_value = element.get_attribute(attribute)
            is_correct = actual_value == text
            if is_correct:
                logger.info(f"✅ Атрибут '{attribute}' у элемента {what} имеет правильное значение: \"{actual_value}\"")
            else:
                logger.warning(f"⚠️ Атрибут '{attribute}' у элемента {what} НЕ совпадает. Ожидалось: \"{text}\", Получено: \"{actual_value}\"")
            return is_correct
        except NoSuchElementException as ex:
            logger.warning(f"⚠️ Элемент НЕ найден: {what}, {ex}")
            return False

    def is_redirect_correct(self, old_url, new_url, timeout=4) -> bool:
        """
        Проверка редиректа
        """
        try:
            WebDriverWait(self.browser, timeout).until(ec.url_changes(old_url))
            current_url = self.browser.current_url
            is_correct = current_url == new_url
            if is_correct:
                logger.info(f"✅ Успешный редирект: {old_url} → {new_url}")
            else:
                logger.warning(f"⚠️ Неверный редирект: Ожидалось {new_url}, но перешли на {current_url}")
            return is_correct
        except TimeoutException as ex:
            logger.warning(f"⚠️ Редирект НЕ произошёл. Остался URL: {self.browser.current_url}, {ex}")
            return False

    def is_element_to_be_clickable(self, how, what, timeout=4) -> bool:
        """
        Проверка кликабельности элемента
        """
        try:
            element: ec.WebElement = WebDriverWait(self.browser, timeout).until(ec.element_to_be_clickable((how, what)))
            logger.info(f"✅ Элемент кликабелен: {what}")
            return True
        except TimeoutException as ex:
            logger.warning(f"⚠️ Элемент НЕ кликабелен: {what}, {ex}")
            return False

    # Проверка отображения модулей верхнего меню
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

    # Проверка отображения модулей бокового меню
    def should_be_nav_title_home_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.NAV_TITLE_HOME_BUTTON), "Nav title home button is not visible on page!"

    def should_be_current_page_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.CURRENT_PAGE_BUTTON), "Current page button is not visible on page!"

    def should_be_leads_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.LEADS_BUTTON), "Leads button is not visible on page!"

    def should_be_clients_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.CLIENTS_BUTTON), "Clients button is not visible on page!"

    def should_be_task_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.TASK_BUTTON), "Task button is not visible on page!"

    def should_be_schedule_dropdown_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.SCHEDULE_DROPDOWN_BUTTON), "Schedule dropdown button is not visible on page!"

    def should_be_staff_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.STAFF_BUTTON), "Staff button is not visible on page!"

    def should_be_statistics_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.STATISTICS_BUTTON), "Statistics button is not visible on page!"

    def should_be_paymaster_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.PAYMASTER_BUTTON), "Paymaster button is not visible on page!"

    def should_be_reception_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.RECEPTION_BUTTON), "Reception button is not visible on page!"

    def should_be_settings_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.SETTINGS_BUTTON), "Settings button is not visible on page!"

    def should_be_mobile_app_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.MOBILE_APP_BUTTON), "Mobile app button is not visible on page!"

    def should_be_footer_fixed(self) -> None:
        assert self.is_element_present(*BasePageLocators.FOOTER_FIXED), "Footer fixed is not visible on page!"

    def should_be_footer_fixed_button(self) -> None:
        assert self.is_element_present(*BasePageLocators.FOOTER_FIXED_LINK), "Footer fixed link is not visible on page!"

    # Нажатия на кнопки
    def click_on_user_icon(self) -> None:
        link = self.browser.find_element(*BasePageLocators.USER_ICON)
        link.click()

    def click_on_footer_fixed_link(self) -> None:
        link = self.browser.find_element(*BasePageLocators.FOOTER_FIXED_LINK)
        link.click()

    