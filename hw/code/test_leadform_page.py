from datetime import datetime
from base import BaseCase
from selenium.webdriver.support.wait import WebDriverWait
from ui.fixtures import driver

LEADFORM_NAME = 'Лид-форма ' + str(datetime.now().second)
EDIT_LEADFORM_NAME = 'Новая Лид-форма ' + str(datetime.now().second)
COMPANY_NAME = 'AAA'
LEADFORM_TITLE = 'Заголовок 1'
LEADFORM_DESCRIPTION = 'Опрос 1'
COMPANY_LEGAL_NAME = ' AAA'
COMPANY_ADRESS = 'НН'


class TestLeadformPage(BaseCase):
    wait = WebDriverWait(driver, timeout=0)

    def test_create_leadform(self, leadform_page):
        leadform_page.click_create_leadform_button()
        assert leadform_page.is_leadform_page_opened()

        leadform_page.fill_leadform_name_field(LEADFORM_NAME)
        leadform_page.click_download_and_choose_logo_button()
        leadform_page.fill_company_name_field(COMPANY_NAME)
        leadform_page.fill_leadform_title_field(LEADFORM_TITLE)
        leadform_page.fill_leadform_description_field(LEADFORM_DESCRIPTION)
        leadform_page.click_save_button()

        assert leadform_page.is_question_leadform_page_opened()
        leadform_page.click_save_button()

        assert leadform_page.is_result_leadform_page_opened()
        leadform_page.click_save_button()

        assert leadform_page.is_settings_leadform_page_opened()
        leadform_page.fill_leadform_legal_name_field(COMPANY_LEGAL_NAME)
        leadform_page.fill_leadform_legal_adress_field(COMPANY_ADRESS)
        leadform_page.click_save_button()

        assert leadform_page.is_leadform_in_list_exists(LEADFORM_NAME)

    def test_find_leadform(self, leadform_page):
        leadform_page.fill_find_leadform_field(LEADFORM_NAME)
        assert leadform_page.is_leadform_in_list_exists(LEADFORM_NAME)

        unknown_leadform_name = 'Неизвестная лид-форма'
        leadform_page.fill_find_leadform_field(unknown_leadform_name)
        assert not leadform_page.is_leadform_in_list_exists(unknown_leadform_name)

    def test_editing_leadform(self, leadform_page):
        leadform_page.click_editing_leadform(LEADFORM_NAME)
        assert leadform_page.is_leadform_page_opened()

        leadform_name = leadform_page.get_leadform_name()
        assert leadform_name == LEADFORM_NAME
        leadform_page.fill_leadform_name_field(EDIT_LEADFORM_NAME)
        company_name = leadform_page.get_leadform_company_name()
        assert company_name == COMPANY_NAME
        leadform_title = leadform_page.get_leadform_title()
        assert leadform_title == LEADFORM_TITLE
        leadform_description = leadform_page.get_leadform_description()
        assert leadform_description == LEADFORM_DESCRIPTION

        leadform_page.click_save_button()
        leadform_page.click_save_button()

        leadform_legal_name = leadform_page.get_leadform_legal_name()
        assert leadform_legal_name == COMPANY_LEGAL_NAME
        leadform_legal_adress = leadform_page.get_leadform_legal_adress()
        assert leadform_legal_adress == COMPANY_ADRESS

        leadform_page.click_save_button()
        assert leadform_page.is_leadform_in_list_exists(EDIT_LEADFORM_NAME)

    def test_cancel_create_leadform(self, leadform_page):
        leadform_page.click_create_leadform_button()
        assert leadform_page.is_leadform_page_opened()

        leadform_page.click_cancel_button()
        assert not leadform_page.is_leadform_page_opened()

    def test_delete_leadform(self, leadform_page):
        leadform_page.click_delete_leadform_button(EDIT_LEADFORM_NAME)
        assert not leadform_page.is_leadform_in_list_exists(EDIT_LEADFORM_NAME)
