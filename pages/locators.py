from typing import Literal
from selenium.webdriver.common.by import By


class BasePageLocators:
	USER_ICON = (By.CSS_SELECTOR, ".header-profile .user-profile")


class AuthPageLocators:
	LOGIN_FORM_USERNAME = (By.CSS_SELECTOR, "#loginform-username")
	LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#loginform-password")
	SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn")


class MainPageLocators:
	pass