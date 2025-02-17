from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
	# Проверка отображения модулей оповещения об ошибках
	def should_be_alert_danger_error(self) -> None:
		assert self.is_element_present(*MainPageLocators.ALERT_DANGER_ERROR), "Alert danger error is not visible on page!"

	def should_be_not_alert_danger_error(self) -> None:
		assert self.is_not_element_present(*MainPageLocators.ALERT_DANGER_ERROR), "Alert danger error is present on page!"

	def should_be_alert_danger_error_link(self) -> None:
		assert self.is_element_present(*MainPageLocators.ALERT_DANGER_ERROR_LINK), "Alert danger error ling is not visible on page!"
	
	# Проверка отображения модулей в ряду фильтров
	def should_be_dashboard_search_period(self) -> None:
		assert self.is_element_present(*MainPageLocators.DASHBOARD_SEARCH_PERIOD), "Dashboard search period is not present on page!"
	
	def should_be_dashboard_choose_legal_entity(self) -> None:
		assert self.is_element_present(*MainPageLocators.DASHBOARD_CHOOSE_LEGAL_ENTITY), "Dashboard choose legal entity is not visible on page!"

	def should_be_dashboard_submit_button(self) -> None:
		assert self.is_element_present(*MainPageLocators.DASHBOARD_SUBMIT_BUTTON), "Dashboard submit button is not visible on page!"

	def should_be_dashboard_default_button(self) -> None:
		assert self.is_element_present(*MainPageLocators.DASHBOARD_DEFAULT_BUTTON), "Dashboard default button is not visible on page!"

	# Проверка отображения модулей в ряду статистики в числах
	def should_be_statistics_till_by_day(self) -> None:
		assert self.is_element_present(*MainPageLocators.STATISTICS_TILL_BY_DAYS), "Statistics till by day is not visible on page!"

	def should_be_statistics_cost(self) -> None:
		assert self.is_element_present(*MainPageLocators.STATISTICS_COST), "Statistics cost is not visible on page!"

	def should_be_statistics_new_registration_clients(self) -> None:
		assert self.is_element_present(*MainPageLocators.STATISTICS_NEW_REGISTRATION_CLIENTS), "Statistics new registration clients is not visible on page!"

	def should_be_statistics_open_clients(self) -> None:
		assert self.is_element_present(*MainPageLocators.STATISTICS_OPEN_CLIENTS), "Statistics open clients is not visible on page!"

	def should_be_statistics_download_apps(self) -> None:
		assert self.is_element_present(*MainPageLocators.STATISTICS_DOWNLOAD_APPS), "Statistics download apps is not visible on page!"

	def should_be_statistics_date_contract_end(self) -> None:
		assert self.is_element_present(*MainPageLocators.STATISTICS_DATE_CONTRACT_END), "Statistics date contract end is not visible on page!"

	def should_be_statistics_client_visit(self) -> None:
		assert self.is_element_present(*MainPageLocators.STATISTICS_CLIENT_VISIT), "Statistics client visit is not visible on page!"

	def should_be_statistics_debt_per_period(self) -> None:
		assert self.is_element_present(*MainPageLocators.STATISTICS_DEBT_PER_PERIOD), "Statistics debt per period is not visible on page!"

	def should_be_statistics_all_debt(self) -> None:
		assert self.is_element_present(*MainPageLocators.STATISTICS_ALL_DEBT), "Statistics all debt is not visible on page!"

	# Проверка отображения графика по дням
	def should_be_revenue_statistics(self) -> None:
		assert self.is_element_present(*MainPageLocators.REVENUE_STATISTICS), "Revenue statistics is not visible on page!"

	# Проверка отображения графиков и диограм
	def should_be_type_pay_statistics(self) -> None:
		assert self.is_element_present(*MainPageLocators.TYPE_PAY_STATISTICS), "Type pay statistics is not visible on page!"

	def should_be_top_managers_statistics(self) -> None:
		assert self.is_element_present(*MainPageLocators.TOP_MANAGERS_STATISTICS), "Top managers statistics is not visible on page!"

	def should_be_revenue_shares_statistics(self) -> None:
		assert self.is_element_present(*MainPageLocators.REVENUE_SHARES_STATISTICS), "Revenue shares statistics is not visible on page!"

	def should_be_custom_segments_statistics(self) -> None:
		assert self.is_element_present(*MainPageLocators.CUSTOMER_SEGMENTS_STATISTICS), "Customer segments statistics is not visible on page!"
