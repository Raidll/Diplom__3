from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD_BUTTON = By.XPATH, ".//a[text()='Восстановить пароль']"
    INPUT_EMAIL = By.XPATH, ".//input[@name='name']"
    INPUT_PASSWORD = By.XPATH, ".//input[@name='Пароль']"
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти']"
