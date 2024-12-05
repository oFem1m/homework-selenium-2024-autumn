# test_registration.py

import pytest
from dotenv import load_dotenv

import base

load_dotenv()

@pytest.mark.usefixtures("setup", "login_data")
class TestRegistration(base.BaseCase):
    authorize = True

    def test_open_registration_page(self, registration_page, login_data):
        assert registration_page.is_opened(), "Страница регистрации не открылась как ожидалось."
