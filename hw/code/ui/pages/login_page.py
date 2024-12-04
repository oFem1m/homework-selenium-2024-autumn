from hw.code.ui.locators.login_page_locators import LoginPageLocators
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.audience_page import AudiencePage


class LoginPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = LoginPageLocators

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


    def login_for_audience(self, username, password):
        self.driver.get(self.url)

        self.go_to_cabinet()
        self.click_mail()
        self.enter_username(username)
        self.click_next_button()
        self.click_no_vkid_button()
        self.enter_password(password)
        self.click_continue_mail()

        return AudiencePage(self.driver)
