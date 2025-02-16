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

	# Боковое меню
	NAV_TITLE_HOME_BUTTON = (By.CSS_SELECTOR, ".nav_title")
	CURRENT_PAGE_BUTTON = (By.CSS_SELECTOR, ".current-page")
	LEADS_BUTTON = (By.CSS_SELECTOR, "//a[@href='/leads/index']")
	CLIENTS_BUTTON = (By.CSS_SELECTOR, "//a[@href='/clients/index']")
	TASK_BUTTON = (By.CSS_SELECTOR, "//a[@href='/task/manage']")
	# TODO Добавить css селекторы для выпадающего списка
	SCHEDULE_DROPDOWN_BUTTON = (By.CSS_SELECTOR, ".schedule_dropdown")
	STAFF_BUTTON = (By.CSS_SELECTOR, "//a[@href='/staff']")
	STATISTICS_BUTTON = (By.CSS_SELECTOR, "//a[@href='/statistics']")
	PAYMASTER_BUTTON = (By.CSS_SELECTOR, "//a[@href='/paymaster']")
	RECEPTION_BUTTON = (By.CSS_SELECTOR, "//a[@href='/reception']")
	# TODO Добавить css селекторы для выпадающего списка
	SETTINGS_BUTTON = (By.CSS_SELECTOR, "//a[@href='/javascript:;']")
	# TODO Добавить css селекторы для выпадающего списка
	MOBILE_APP_BUTTON = (By.CSS_SELECTOR, ".fa-mobile")

	# Нижняя часть
	FOOTER_FIXED = (By.CSS_SELECTOR, ".footer_fixed")
	FOOTER_FIXED_LINK = (By.CSS_SELECTOR, "//a[@href='https://status.fitbase.io/']")


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
	ALERT_DANGER_ERROR = (By.CSS_SELECTOR, ".alert alert-danger")
	ALERT_DANGER_ERROR_LINK = (By.CSS_SELECTOR, ".alert-link")

	# Ряд фильтров
	DASHBOARD_SEARCH_PERIOD = (By.CSS_SELECTOR, ".dashboardsearch-dateperiod-container")
	DASHBOARD_CHOOSE_LEGAL_ENTITY = (By.CSS_SELECTOR, ".select2-selection--multiple")
	DASHBOARD_SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn-success")
	DASHBOARD_DEFAULT_BUTTON = (By.CSS_SELECTOR, ".btn-default")

	# Ряд статистики в числах
	# TODO Динамические ссылки, поменять css селекторы на них
	STATISTICS_TILL_BY_DAYS = (By.CSS_SELECTOR, "//a[@href='/statistics/till_by_days']")
	STATISTICS_COST = (By.CSS_SELECTOR, "//a[@href='/statistics/cost']")
	STATISTICS_NEW_REGISTRATION_CLIENTS = (By.CSS_SELECTOR, "//a[@href='/clients/index?registrationDate=01.02.2025+-+28.02.2025&registrationFrom=01.02.2025&registrationTo=28.02.2025&defaultClub%5B0%5D=1']")
	STATISTICS_OPEN_CLIENTS = (By.CSS_SELECTOR, "//a[@href='/clients/index?status=1&defaultClub%5B0%5D=1']")
	STATISTICS_DOWNLOAD_APPS = (By.CSS_SELECTOR, "//a[@href='/clients/index?appInstalled=3&defaultClub%5B0%5D=1']")
	STATISTICS_DATE_CONTRACT_END = (By.CSS_SELECTOR, "//a[@href='/clients/index?dateContractEnd=01.02.2025+-+28.02.2025&contractEndFrom=01.02.2025&contractEndTo=28.02.2025&defaultClub%5B0%5D=1']")
	STATISTICS_CLIENT_VISIT = (By.CSS_SELECTOR, "//a[@href='/statistic/client-visits/index?ClientVisitsSearch[date_range]=01.02.2025%20-%2028.02.2025']")
	# TODO Пропущено 3 статистики у которых нету кнопки, доделать
	STATISTICS_DEBT_PER_PERIOD = (By.CSS_SELECTOR, "//a[@href='/statistics/debt?DebtSearch[period]=01.02.2025%20-%2028.02.2025&DebtSearch[is_get_past]=1']")
	STATISTICS_ALL_DEBT = (By.CSS_SELECTOR, "//a[@href='/statistics/debt']")

	# Ряд графика в по дням
	REVENUE_STATISTICS = (By.CSS_SELECTOR, ".x_content")

	# Ряд графиков и диограм 
	TYPE_PAY_STATISTICS = (By.CSS_SELECTOR, "div.row:nth-child(3) > div:nth-child(1)")
	TOP_MANAGERS_STATISTICS = (By.CSS_SELECTOR, "div.row:nth-child(3) > div:nth-child(2)")
	REVENUE_SHARES_STATISTICS = (By.CSS_SELECTOR, "div.row:nth-child(3) > div:nth-child(3)")
	CUSTOMER_SEGMENTS_STATISTICS = (By.CSS_SELECTOR, "div.row:nth-child(3) > div:nth-child(4)")
