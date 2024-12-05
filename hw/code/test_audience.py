import pytest
import base
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.usefixtures("setup", "login_data")
class TestAudience(base.BaseCase):
    authorize = True

    def test_open(self, audience_page, login_data):
        assert audience_page.is_opened(), "The audience tab did not open as expected."

    def test_check_create_audience(self, audience_page, login_data):
        audience_page.checking_create_audience()

    def test_create_audience(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        audience_page.keywords_input("Тест")
        audience_page.keywords_button_save()
        audience_page.save_audience()
        audience_page.selected_audiece()
        audience_page.delete_audience()
        audience_page.delete_audience_click()

    def test_create_source(self, audience_page, login_data):
        audience_page.create_audience()
        audience_page.add_source()
        audience_page.keywords()
        audience_page.keywords_input("Тест")
        audience_page.keywords_button_save()
        audience_page.save_audience()
        audience_page.selected_audiece()
        audience_page.delete_audience()
        audience_page.delete_audience_click()

    



