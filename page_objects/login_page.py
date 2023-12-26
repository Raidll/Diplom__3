import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    FORGOT_PASSWORD_BUTTON = By.XPATH, ".//a[text()='Восстановить пароль']"
    INPUT_EMAIL = By.XPATH, ".//input[@name='name']"
    INPUT_PASSWORD = By.XPATH, ".//input[@name='Пароль']"
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти']"

    @allure.step('Ожидание видимости кнопки "Восстановить пароль"')
    def waiting_visibility_forgot_password_button(self):
        self.waiting_visibility_by_xpath(self.FORGOT_PASSWORD_BUTTON)

    @allure.step('Клик кнопке "Восстановить пароль"')
    def click_forgot_password_button(self):
        self.click_by_xpath(self.FORGOT_PASSWORD_BUTTON)

    @allure.step('Ожидание видимости поля ввода маила')
    def waiting_visibility_email_input(self):
        self.waiting_visibility_by_xpath(self.INPUT_EMAIL)

    @allure.step('Заполнить поле "Email"')
    def fill_email_field(self, email):
        self.fill_field_by_xpath(self.INPUT_EMAIL, email)

    @allure.step('Заполнить поле "Пароль"')
    def fill_password_field(self, password):
        self.fill_field_by_xpath(self.INPUT_PASSWORD, password)

    @allure.step('Клик кнопке "Войти"')
    def click_login_button(self):
        self.click_by_xpath(self.LOGIN_BUTTON)


