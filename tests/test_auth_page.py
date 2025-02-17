from pages.auth_page import AuthPage


class TestAuthPage():
    def test_check_visible_on_page(self, browser) -> None:
        link = "https://dude-yoga.fitbase.io/"
        page = AuthPage(browser, link)
        page.open()
        # Проверка отображения элементов на странице
        page.should_be_login_form()
        page.should_be_password_form()
        page.should_be_submit_button()
        page.should_be_carrotquest_support_palm()
        page.should_be_form_toggle()
        page.should_be_remember_me()

        # TODO не получается найти элемент кнопки возвращения на ввод данных для входа, либо неправильно вводятся данные из .env фала
        # Переход на восстановление пароля
        # page.go_to_toggle_on_reset_password()

        # Проверка отображения элементов на странице
        # page.should_be_password_reset_request_form()
        # page.should_be_password_reset_request_button()

        # Переход обратно
        # page.go_to_toggle_on_reset_password_comeback()

    def test_quest_can_auth(self, browser) -> None:
        link = "https://dude-yoga.fitbase.io/"
        page = AuthPage(browser, link)
        page.open()
        # Авторизация в форме
        page.auth_on_page()
