from pages.auth_page import AuthPage


class TestBasePageFromMainPage():
    def test_quest_can_auth(self, browser) -> None:
        link = "https://dude-yoga.fitbase.io/"
        page = AuthPage(browser, link)
        page.open()
        page.should_be_login_form()
        page.should_be_password_form()
        page.should_be_submit_button()
        page.auth_on_page()