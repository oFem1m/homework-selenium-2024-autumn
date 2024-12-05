from hw.code.ui.locators.audience_page_locators import AudienceLocators
from hw.code.ui.pages.base_page import BasePage

class AudiencePage(BasePage):
    url = "https://ads.vk.com/hq/audience"
    locators = AudienceLocators

    def __init__(self, driver):
        self.driver = driver

    def open_audience_tab(self):
        self.click(self.locators.TAB_AUDIENCE, 10)

    def checking_create_audience(self):
        assert self.is_element_present(self.locators.CREATE_AUDIENCE, 10), "The audience create button did not displayed"

    def create_audience(self):
        self.click(self.locators.CREATE_AUDIENCE, 10)

    def add_source(self):
        self.click(self.locators.ADD_SOURCE, 10)

    def keywords(self):
        self.click(self.locators.KEYWORDS, 10)

    def keywords_input(self, value):
        textarea = self.find(self.locators.KEYWORDS_INPUT_TEXTAREA)
        textarea.send_keys(value)

    def keywords_button_save(self):
        div_elements = self.driver.find_elements(self.locators.KEYWORDS_BUTTON_SAVE[0],
                                                 self.locators.KEYWORDS_BUTTON_SAVE[1])
        second_div = div_elements[1]
        button = second_div.find_element(self.locators.KEYWORDS_DIV_BUTTON_SAVE[0],
                                         self.locators.KEYWORDS_DIV_BUTTON_SAVE[1])
        button.click()

    def save_audience(self):
        button = self.driver.find_element(self.locators.SAVE_AUDIENCE_BUTTON[0], self.locators.SAVE_AUDIENCE_BUTTON[1])
        button.click()

    def selected_audiece(self):
        checkboxs = self.driver.find_elements(self.locators.SHARING_AUDIENCE[0], self.locators.SHARING_AUDIENCE[1])
        checkbox = checkboxs[-1]
        if not checkbox.is_selected():
            self.driver.execute_script("arguments[0].click();", checkbox)

    def delete_audience(self):
        button = self.driver.find_element(self.locators.DELETE_AUDIENCE_BUTTON[0],
                                          self.locators.DELETE_AUDIENCE_BUTTON[1])
        button.click()

    def delete_audience_click(self):
        second_button = self.driver.find_element(self.locators.DELETE_AUDIENCE_BUTTON_MENU[0],
                                                 self.locators.DELETE_AUDIENCE_BUTTON_MENU[1])
        second_button.click()

