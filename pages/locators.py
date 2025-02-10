from selenium.webdriver.common.by import By


class BasePageLocators:
	# Верхняя часть страницы
	USER_ICON = (By.CSS_SELECTOR, ".header-profile .user-profile")
	HEADER_KNOWLEAGE_BASE = (By.CSS_SELECTOR, ".header_knowleage_base .btn-primary")
	HEADER_IDEA = (By.CSS_SELECTOR, ".header_idea .btn-primary")
	BANNER_HEADER_LIMIT = (By.CSS_SELECTOR, ".banner_header-limit")
	# TODO Добавить css селекторы для всплывающего списка клиентов
	FAST_CLIENT_SEARCH = (By.CSS_SELECTOR, "#fast-client-card-input-main")
	FAST_CLIENT_BUTTON = (By.CSS_SELECTOR, ".btn-success")
	# TODO Добавить css селекторы для всплывающего табло клиентов в клубе
	OPEN_CLIENTS_RECEPTION = (By.CSS_SELECTOR, "#open_clients_reception")
	# TODO Добавить css селекторы для всплывающего списка
	CHANGE_CLUB_FORM = (By.CSS_SELECTOR, "#change-club-form")


class AuthPageLocators:
	# Страница авторизации
	LOGIN_FORM_USERNAME = (By.CSS_SELECTOR, "#loginform-username")
	LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#loginform-password")
	SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn")
	CARROTQUEST_SUPPORT_PALM = (By.CSS_SELECTOR, "#carrot-messenger-collapsed-frame")
	LOGIN_FORM_TOGGLE = (By.CSS_SELECTOR, ".login-form-toggle")
	LOGIN_FORM_REMEMBERME = (By.CSS_SELECTOR, ".field-loginform-rememberme")

	# Страница сброса пароля
	PASSWORD_RESET_REQUEST_FORM = (By.CSS_SELECTOR, "#passwordresetrequestform-username")
	PASSWORD_RESET_REQUEST_BUTTON = (By.CSS_SELECTOR, ".btn-lg")
	LOGIN_FORM_TOGGLE_COMEBACK = (By.XPATH, "//section[@id='passwordResetForm']//div[@class='form_row']")

class MainPageLocators:
	pass