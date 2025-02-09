from selenium.webdriver.common.by import By


class BasePageLocators:
	USER_ICON = (By.CSS_SELECTOR, ".header-profile .user-profile")


class AuthPageLocators:
	LOGIN_FORM_USERNAME = (By.CSS_SELECTOR, "#loginform-username")
	LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#loginform-password")
	SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn")
	CARROTQUEST_SUPPORT_PALM = (By.CSS_SELECTOR, "#carrot-messenger-collapsed-frame")
	LOGIN_FORM_TOGGLE = (By.CSS_SELECTOR, ".login-form-toggle")
	LOGIN_FORM_REMEMBERME = (By.CSS_SELECTOR, ".field-loginform-rememberme")
	PASSWORD_RESET_REQUEST_FORM = (By.CSS_SELECTOR, "#passwordresetrequestform-username")
	PASSWORD_RESET_REQUEST_BUTTON = (By.CSS_SELECTOR, ".btn-lg")
	LOGIN_FORM_TOGGLE_COMEBACK = (By.XPATH, "//section[@id='passwordResetForm']//div[@class='form_row']")

class MainPageLocators:
	pass