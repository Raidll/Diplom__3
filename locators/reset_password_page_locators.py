from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    INPUT_CODE_FROM_EMAIL = By.XPATH, ".//label[text()='Введите код из письма']"
    INPUT_PASSWORD = By.XPATH, ".//input[@type='password']"
    DISPLAY_PASSWORD_BUTTON = By.XPATH, "//div[contains(@class, 'input__icon')]"
    PASSWORD_INPUT_STATUS_ACTIVE = By.XPATH, "//div[contains(@class, 'input_status_active')]"