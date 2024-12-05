import time

from selenium.webdriver.support.ui import Select
from hw.code.ui.locators.registration_page_locators import RegistrationPageLocators
from hw.code.ui.pages.base_page import PageNotOpenedException

class RegistrationPage:
    url = "https://ads.vk.com/hq/registration"

    locators = RegistrationPageLocators
    def __init__(self, driver):
        self.driver = driver


    def open_new_registration_tab(self):
        self.click(self.locators.TAB_AUDIENCE, 10)
    def select_account_type(self, account_type="Рекламодатель"):
        if account_type == "Рекламодатель":
            self.driver.find_element(*RegistrationPageLocators.ACCOUNT_TYPE_ADVERTISER).click()
        elif account_type == "Агентство":
            self.driver.find_element(*RegistrationPageLocators.ACCOUNT_TYPE_AGENCY).click()

    def select_country(self, country="Россия"):
        select = Select(self.driver.find_element(*RegistrationPageLocators.COUNTRY_SELECT))
        select.select_by_visible_text(country)

    def select_currency(self, currency="Российский рубль (RUB)"):
        select = Select(self.driver.find_element(*RegistrationPageLocators.CURRENCY_SELECT))
        select.select_by_visible_text(currency)

    def enter_email(self, email):
        self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)

    def submit_form(self):
        self.driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')
