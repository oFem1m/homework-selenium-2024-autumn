import pytest
import base
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.usefixtures("setup", "login_data")
class TestAudience(base.BaseCase):
    authorize = True

    def test_open(self, audience_page, login_data):
        assert audience_page.is_opened(), "The audience tab did not open as expected."
