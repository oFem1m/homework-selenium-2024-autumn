from selenium.webdriver.common.by import By

class OverviewPageLocators:
    TAB_AUDIENCE = (By.XPATH, "//*[@data-route='audience']")
    CREATE_AUDIENCE = (By.XPATH, "//*[@data-testid='create-audience']")
    AUDIENCE_CREATION_ELEMENT = (By.CLASS_NAME, "vkuiTitle--level-2")
    SAVE_AUDIENCE = (By.CLASS_NAME, "ModalFooterSimple_container__rteom")
    SAVE_AUDIENCE_BUTTON = (By.CSS_SELECTOR, ".ModalFooterSimple_container__rteom .vkuiButton--mode-primary")