import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome


def pytest_addoption(parser) -> None:
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome")
    parser.addoption("--language", action="store", default="en",
                     help="Choose language what you want to open the site")
    

@pytest.fixture(scope="module")
def browser(request):
    
	browser_name = request.config.getoption("browser_name")
	user_language = request.config.getoption("language")
	browser = None

	options_chrome = OptionsChrome()
	options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})

	if browser_name == "chrome":
		print("\nstart chrome browser for test..")
		browser = webdriver.Chrome(options=options_chrome)
	else:
		raise pytest.UsageError("--browser_name should be chrome or firefox")

	yield browser

	print("\nquit browser..")
	browser.quit()