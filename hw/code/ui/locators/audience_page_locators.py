from selenium.webdriver.common.by import By

class AudienceLocators:
    TAB_AUDIENCE = (By.XPATH, "//*[@data-route='audience']")
    CREATE_AUDIENCE = (By.CSS_SELECTOR, "[data-testid='create-audience']")
    AUDIENCE_CREATION_ELEMENT = (By.CLASS_NAME, "vkuiTitle--level-2")
    AUDIENCE_NAME_INPUT = (By.CSS_SELECTOR, 'span.vkuiFormField > input')
    ADD_SOURCE = (By.CLASS_NAME, "vkuiButton--stretched")
    KEYWORDS = (By.XPATH, "//span[text()='Ключевые фразы']")
    KEYWORDS_INPUT_TEXTAREA = (By.CSS_SELECTOR, 'textarea[placeholder="Введите фразу и нажмите Enter"]')
    KEYWORDS_BUTTON_SAVE = (By.CSS_SELECTOR, '.ModalSidebarPage__footer.ModalSidebarPage_footer__xRUr-')
    KEYWORDS_DIV_BUTTON_SAVE = (By.CLASS_NAME, "vkuiButton--mode-primary")
    SAVE_AUDIENCE_BUTTON = (By.CSS_SELECTOR, ".ModalFooterSimple_container__rteom .vkuiButton--mode-primary")
    SHARING_AUDIENCE = (By.CSS_SELECTOR, "label.vkuiCheckbox > input.vkuiVisuallyHidden")
    SHARING_AUDIENCE_BUTTON = (By.CLASS_NAME, "sharingButton_button__K6Oqi")
    SHARING_AUDIENCE_HEAD = (By.CLASS_NAME, "vkuiPanelHeader__content-in")
    DELETE_AUDIENCE_BUTTON = (By.CLASS_NAME, 'RemoveItemsButton_button__6OoPq')
    DELETE_AUDIENCE_WINDOW = (By.CLASS_NAME, 'RemoveItemsModal_title__n8BNd')
    DELETE_AUDIENCE = (By.CSS_SELECTOR, 'input.vkuiCheckbox__input')
    DELETE_AUDIENCE_BUTTON_MENU = (By.CSS_SELECTOR, ".RemoveItemsModal_footer__pfEgN button:nth-child(2)")
    DELETE_AUDIENCE_BUTTON_IN_MENU = (By.CLASS_NAME, 'vkuiButton--mode-primary')