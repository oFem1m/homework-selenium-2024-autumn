from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    ACCOUNT_TYPE_ADVERTISER = (By.XPATH, "//input[@value='Рекламодатель']")
    ACCOUNT_TYPE_AGENCY = (By.XPATH, "//input[@value='Агентство']")
    COUNTRY_SELECT = (By.XPATH, "//select[@name='country']")
    CURRENCY_SELECT = (By.XPATH, "//select[@name='currency']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать')]")
