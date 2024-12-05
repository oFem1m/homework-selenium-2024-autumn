from selenium.webdriver.common.by import By

class LoginPageLocators:
    CABINET_BUTTON = (By.CLASS_NAME, "ButtonCabinet_primary__LCfol")
    MAIL_BUTTON = (By.CSS_SELECTOR, "[data-test-id='oAuthService_mail_ru']")
    USERNAME_INPUT = (By.NAME, "username")
    NEXT_BUTTON = (By.CSS_SELECTOR, "[data-test-id='next-button']")
    NO_VK_ID_BUTTON = (By.CSS_SELECTOR, "[data-test-id='bind-screen-vkid-change-restore-type-btn']")
    PASSWORD_INPUT = (By.NAME, "password")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='submit-button']")

