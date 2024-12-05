import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PageNotOpenedException(Exception):
    pass


class BasePage(object):
    url = 'https://ads.vk.com/'

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_all(self, locator, timeout=None) -> list[WebElement]:
        return self.wait(timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Search')
    def search(self, query):
        try:
            elem = self.find(self.locators.QUERY_LOCATOR_ID)
            elem.send_keys(query)
            go_button = self.find(self.locators.GO_BUTTON_LOCATOR)
            go_button.click()
        except TimeoutException as e:
            allure.attach(
                body=f"Element not found: {str(e)}",
                name="TimeoutException details",
                attachment_type=allure.attachment_type.TEXT
            )
            raise
        except AssertionError as e:
            allure.attach(
                body="Expected value did not match actual value",
                name="Assertion details",
                attachment_type=allure.attachment_type.TEXT
            )
            raise

    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        try:
            elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
            elem.click()
            return elem
        except TimeoutException as e:
            allure.attach(
                body=f"Could not click element: {str(e)}",
                name="TimeoutException details",
                attachment_type=allure.attachment_type.TEXT
            )
            raise

    def enter_text(self, locator, text, timeout=None):
        element = self.wait(timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_element_present(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_element_text(self, locator, timeout=None):
        element = self.wait(timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_element_value(self, locator, timeout=None):
        element = self.wait(timeout).until(EC.presence_of_element_located(locator))
        return element.get_attribute("value")

    def is_enabled(self, locator, timeout=None):
        element = self.wait(timeout).until(EC.presence_of_element_located(locator))
        if element.is_enabled():
            return True
        else:
            return False

    def click_action(self, button):
        action = ActionChains(self.driver)
        action.move_to_element(button).click(button).perform()

    def send_keys_tab(self, input, value):
        input.send_keys(value, Keys.TAB)

    def became_visible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def became_invisible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False