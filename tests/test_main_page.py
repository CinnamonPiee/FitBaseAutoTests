from pages.main_page import MainPage
from pages.auth_page import AuthPage


import pytest


class TestMainPage():
	@pytest.mark.xfail(strict=False, reason="Test crashed due to missing error warning")
	def test_check_visible_module_with_alert_danger_error(self, browser) -> None:
		# link = "https://dude-yoga.fitbase.io/"
		link = "https://d40228.fitbase.io/"
		auth_page = AuthPage(browser, link)
		auth_page.open()
		auth_page.auth_on_page()
		# Проверка отображения элемента предупреждения об ошибке
		page = MainPage(browser, browser.current_url)
		page.should_be_alert_danger_error()
		page.should_be_alert_danger_error_link()

	@pytest.mark.xfail(strict=False, reason="Test failed due to the presence of an error warning")
	def test_check_visible_module_with_alert_danger_error(self, browser) -> None:
		# link = "https://dude-yoga.fitbase.io/"
		link = "https://d40228.fitbase.io/"
		auth_page = AuthPage(browser, link)
		auth_page.open()
		auth_page.auth_on_page()
		# Проверка НЕ отображения элемента предупреждения об ошибке
		page = MainPage(browser, browser.current_url)
		page.should_be_not_alert_danger_error()

	def test_check_visible_modules_in_a_row_of_filters(self, browser) -> None:
		# link = "https://dude-yoga.fitbase.io/"
		link = "https://d40228.fitbase.io/"
		auth_page = AuthPage(browser, link)
		auth_page.open()
		auth_page.auth_on_page()
		# Проверка отображения элементов на странице в ряду фильтров
		page = MainPage(browser, browser.current_url)
		page.should_be_dashboard_search_period()
		page.should_be_dashboard_choose_legal_entity()
		page.should_be_dashboard_submit_button()
		page.should_be_dashboard_default_button()

	# TODO тесты могут падать из-за динамических css селекторов, исправить
	@pytest.mark.xfail(strict=False, reason="Test may fail due to dynamic css selectors")
	def test_check_visible_modules_in_a_series_of_statistics_in_numbers(self, browser) -> None:
		# link = "https://dude-yoga.fitbase.io/"
		link = "https://d40228.fitbase.io/"
		auth_page = AuthPage(browser, link)
		auth_page.open()
		auth_page.auth_on_page()
		# Проверка отображения элементов на странице в ряду статистики в числах
		page = MainPage(browser, browser.current_url)
		page.should_be_statistics_till_by_day()
		page.should_be_statistics_cost()
		page.should_be_statistics_new_registration_clients()
		page.should_be_statistics_open_clients()
		page.should_be_statistics_download_apps()
		page.should_be_statistics_date_contract_end()
		page.should_be_statistics_client_visit()
		page.should_be_statistics_debt_per_period()
		page.should_be_statistics_all_debt()

	def test_check_visible_modules_in_graphics_per_day(self, browser) -> None:
		# link = "https://dude-yoga.fitbase.io/"
		link = "https://d40228.fitbase.io/"
		auth_page = AuthPage(browser, link)
		auth_page.open()
		auth_page.auth_on_page()
		# Проверка отображения элементов на странице в ряду графика по дням
		page = MainPage(browser, browser.current_url)
		page.should_be_revenue_statistics()

	def test_check_visible_modules_in_graphics_and_diograms(self, browser) -> None:
		# link = "https://dude-yoga.fitbase.io/"
		link = "https://d40228.fitbase.io/"
		auth_page = AuthPage(browser, link)
		auth_page.open()
		auth_page.auth_on_page()
		# Проверка отображения элементов на странице в ряду графика и диограм
		page = MainPage(browser, browser.current_url)
		page.should_be_type_pay_statistics()
		page.should_be_top_managers_statistics()
		page.should_be_revenue_shares_statistics()
		page.should_be_custom_segments_statistics()
