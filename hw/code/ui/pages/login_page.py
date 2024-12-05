import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw.code.ui.locators.login_page_locators import LoginPageLocators
from hw.code.ui.pages.base_page import BasePage, PageNotOpenedException
from hw.code.ui.pages.overview_page import OverviewPage  # Создайте этот класс
from hw.code.ui.pages.commerce_page import CommercePage

class LoginPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = LoginPageLocators

    def login(self, username, password, redirect_url=None):
        self.driver.get(self.url)

        self.go_to_cabinet()
        self.click_mail()
        self.enter_username(username)
        self.click_next_button()
        self.click_no_vkid_button()
        self.enter_password(password)
        self.click_continue_mail()

        time.sleep(60)

        if redirect_url:
            self.driver.get(redirect_url)
            # Возвращаем соответствующий объект страницы
            if redirect_url == CommercePage.url:
                return CommercePage(self.driver)
            elif redirect_url == AudiencePage.url:
                return AudiencePage(self.driver)
            # Добавьте дополнительные проверки при необходимости
        else:
            # Если не указан redirect_url, возвращаем OverviewPage
            return OverviewPage(self.driver)

    def go_to_cabinet(self):
        self.click(self.locators.CABINET_BUTTON, 10)

    def click_mail(self):
        self.click(self.locators.MAIL_BUTTON, 15)

    def enter_username(self, username):
        self.enter_text(self.locators.USERNAME_INPUT, username, 10)

    def click_next_button(self):
        self.click(self.locators.NEXT_BUTTON, 10)

    def click_no_vkid_button(self):
        self.click(self.locators.NO_VK_ID_BUTTON, 10)

    def enter_password(self, password):
        self.enter_text(self.locators.PASSWORD_INPUT, password, 10)

    def click_continue_mail(self):
        self.click(self.locators.CONTINUE_BUTTON, 10)


    def wait_for_url_change(self, old_url, timeout=30):
        WebDriverWait(self.driver, timeout).until(EC.url_changes(old_url))
