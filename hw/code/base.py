import pytest
import re
from _pytest.fixtures import FixtureRequest
from selenium.common import TimeoutException

from hw.code.ui.pages.login_page import LoginPage
from ui.pages.base_page import PageNotOpenedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseCase:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)

    def is_opened(self, url, timeout=None):
        if timeout is None:
            timeout = 10

        try:
            pattern = re.compile(url)
            WebDriverWait(self.driver, timeout).until(EC.url_matches(pattern))
            return True
        except TimeoutException:
            raise PageNotOpenedException(
                f"{url} did not open in {timeout} sec, current url {self.driver.current_url}"
            )