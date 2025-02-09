from .base_page import BasePage
from .locators import AuthPageLocators


class AuthPage(BasePage):
	def should_be_login_form(self) -> None:
		assert self.is_element_present(*AuthPageLocators.LOGIN_FORM_USERNAME), "Login username form is not visible on page!"

	def should_be_password_form(self) -> None:
		assert self.is_element_present(*AuthPageLocators.LOGIN_FORM_PASSWORD), "Password form is not visible on page!"

	def should_be_submit_button(self) -> None:
		assert self.is_element_present(*AuthPageLocators.SUBMIT_BUTTON), "Submit button is not visible on page!"

	def auth_on_page(self) -> None:
		self.browser.find_element(*AuthPageLocators.LOGIN_FORM_USERNAME).send_keys(self.login)
		self.browser.find_element(*AuthPageLocators.LOGIN_FORM_PASSWORD).send_keys(self.password)
		self.browser.find_element(*AuthPageLocators.SUBMIT_BUTTON).click()

	

