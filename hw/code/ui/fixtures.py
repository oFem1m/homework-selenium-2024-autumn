import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.login_page import LoginPage
from hw.code.ui.pages.commerce_page import CommercePage
from hw.code.ui.pages.registration_page import RegistrationPage


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()

    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_data():
    return {
        "username": os.getenv("username"),
        "password": os.getenv("password")
    }

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def login_page(driver):
    driver.get(LoginPage.url)
    return LoginPage(driver=driver)

@pytest.fixture
def audience_page(login_page, login_data):
    my_audience_page = login_page.login(login_data["username"], login_data["password"])
    my_audience_page.open_audience_tab()
    return my_audience_page


@pytest.fixture
def registration_page(driver, login_page, login_data):
    page = login_page.login(login_data["username"], login_data["password"])
    if isinstance(page, RegistrationPage):
        return page
    else:
        # Если после логина не была открыта RegistrationPage, выбрасываем исключение
        raise Exception("После логина не была открыта RegistrationPage")

@pytest.fixture
def commerce_page(login_page, login_data):
    # Выполняем логин и перенаправляем на страницу commerce
    return login_page.login(
        login_data["username"],
        login_data["password"],
        redirect_url=CommercePage.url
    )
