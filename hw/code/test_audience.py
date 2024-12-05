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

    def test_create_uniq_audience(self, audience_page, login_data):
        audience_page.create_audience()
        audience_name = 'A1'
        audience_page.set_audience_name(audience_name)
        audience_page.add_source()
        audience_page.keywords()
        audience_page.keywords_input("Тест")
        audience_page.keywords_button_save()
        audience_page.save_audience()
        audience_page.selected_audiece()
        audience_page.delete_audience()
        audience_page.delete_audience_click()

    def test_create_non_uniq_audience(self, audience_page, login_data):
        audience_page.create_audience()
        audience_name = 'A1'
        audience_page.set_audience_name(audience_name)
        audience_page.add_source()
        audience_page.keywords()
        audience_page.keywords_input("Тест")
        audience_page.keywords_button_save()
        audience_page.save_audience()

        audience_page.create_audience()
        audience_page.set_audience_name(audience_name)
        audience_page.add_source()
        audience_page.keywords()
        audience_page.keywords_input("Тест")
        audience_page.keywords_button_save()
        audience_page.save_audience()

        audience_page.selected_audiece()
        audience_page.delete_audience()
        audience_page.delete_audience_click()

    def test_long_name_audience(self, audience_page, login_data):
        audience_page.create_audience()
        audience_name = 'A' * 266
        assert audience_page.set_audience_name(audience_name), "Too long name"

    def test_empty_name_audience(self, audience_page, login_data):
        audience_page.create_audience()
        audience_name = ''
        assert audience_page.set_audience_name(audience_name), "Empty name is forbidden"

    def test_len_1_name_audience(self, audience_page, login_data):
        audience_page.create_audience()
        audience_name = '1'
        audience_page.set_audience_name(audience_name)

    def test_create_source(self, audience_page, login_data):
        audience_page.create_audience()
        audience_name = 'A1'
        audience_page.set_audience_name(audience_name)
        audience_page.add_source()
        audience_page.keywords()
        audience_page.keywords_input("Тест")
        audience_page.keywords_button_save()
        audience_page.save_audience()
        audience_page.selected_audiece()
        audience_page.delete_audience()
        audience_page.delete_audience_click()

    def test_create_empty_source(self, audience_page, login_data):
        audience_page.create_audience()
        audience_name = 'A1'
        audience_page.set_audience_name(audience_name)
        audience_page.add_source()
        audience_page.keywords()
        audience_page.keywords_input("")
        assert audience_page.keywords_button_save(), "you need to enter keywords"


