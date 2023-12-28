from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    RESTORE_BUTTON = By.XPATH, ".//button[text()='Восстановить']"
    INPUT_EMAIL = By.XPATH, ".//input[@name='name']"
