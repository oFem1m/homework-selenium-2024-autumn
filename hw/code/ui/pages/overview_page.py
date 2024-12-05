from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.locators.overview_page_locators import OverviewPageLocators

class OverviewPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = OverviewPageLocators

    def is_opened(self):
        return self.driver.current_url.startswith(self.url)

    def open_audience_tab(self):
        self.click(self.locators.TAB_AUDIENCE, 10)

