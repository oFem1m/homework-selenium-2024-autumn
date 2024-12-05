from hw.code.ui.locators.audience_page_locators import AudienceLocators
from hw.code.ui.pages.base_page import BasePage

class AudiencePage(BasePage):
    url = "https://ads.vk.com/hq/audience"
    locators = AudienceLocators

    def __init__(self, driver):
        self.driver = driver

    def open_audience_tab(self):
        self.click(self.locators.TAB_AUDIENCE, 10)

    def create_audience(self):
        self.click(self.locators.CREATE_AUDIENCE, 10)

    def checking_open_audience_creation_menu(self):
        assert self.is_element_present(self.locators.AUDIENCE_CREATION_ELEMENT, 10), "Audience creation menu is not displayed"

    def is_opened(self):
        # Реализуйте логику проверки, что вкладка открыта
        return self.is_element_present(self.locators.AUDIENCE_TAB_ACTIVE, 10)
