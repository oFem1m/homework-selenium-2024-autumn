from selenium.webdriver.common.by import By


class LeadformLocators:
    CREATE_LEADFORM_BUTTON = (By.XPATH, f"//*[@test-id='create-leadform-button']")

    DOWNLOAD_LOGO = (By.XPATH, f"//*[@data-testid='set-global-image']")

    CHOOSE_LOGO = (By.ID, "media-library-image")

    INPUT_NAME_LEAD_FORM = (By.XPATH, '//input[@placeholder="Название лид-формы"]')

    INPUT_NAME_COMPANY = (By.XPATH, '//input[@placeholder="Название компании"]')

    INPUT_TITLE = (By.XPATH, '//input[@placeholder="Текст заголовка"]')

    INPUT_DESCRIPTION = (By.XPATH, '//input[@placeholder="Краткое описание опроса"]')

    CONTINUE_BUTTON = (By.XPATH, f"//*[@data-testid='submit']")

    CANCEL_BUTTON = (By.XPATH, f"//button[@data-testid='cancel']")

    INPUT_LEGAL_NAME_COMPANY = (By.XPATH, '//input[@placeholder="Введите название"]')

    INPUT_LEGAL_ADRESS_COMPANY = (By.XPATH, '//input[@placeholder="Введите адрес"]')

    ADD_CONTACTS_BUTTON = (
    By.XPATH, f"//*[contains(@class, 'vkuiButton__content') and text()='Добавить контактные данные']")

    ADD_SITE_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiTypography') and text()='Добавить сайт']")

    @staticmethod
    def SELECT_FROM_LEADFORM_LIST(name: str):
        return By.XPATH, f"//*[contains(@class, 'vkuiLink') and text()='{name}']"

    SELECT_ACTIONS_BUTTON = (By.XPATH, f'//input[@placeholder="Действия"]')

    @staticmethod
    def DELETE_LEADFORM_BUTTON(name: str):
        return By.XPATH, f"//button[text()='{name}']/..//button[span/text()='Удалить'"

    @staticmethod
    def EDIT_LEADFORM_BUTTON(name: str):
        return By.XPATH, f"//button[text()='{name}']/..//button[span/text()='Редактировать'"

    INPUT_FIND_LEADFORM = (By.XPATH, '//input[@placeholder="Поиск"]')
