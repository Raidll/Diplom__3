import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание видимости кнопки "Восстановить пароль"')
    def waiting_visibility_forgot_password_button(self):
        self.waiting_visibility_by_xpath(LoginPageLocators.FORGOT_PASSWORD_BUTTON)

    @allure.step('Клик кнопке "Восстановить пароль"')
    def click_forgot_password_button(self):
        self.waiting_visibility_by_xpath(LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        self.click_by_xpath(LoginPageLocators.FORGOT_PASSWORD_BUTTON)

    @allure.step('Ожидание видимости поля ввода маила')
    def waiting_visibility_email_input(self):
        self.waiting_visibility_by_xpath(LoginPageLocators.INPUT_EMAIL)

    @allure.step('Заполнить поле "Email"')
    def fill_email_field(self, email):
        self.waiting_visibility_by_xpath(LoginPageLocators.INPUT_EMAIL)
        self.fill_field_by_xpath(LoginPageLocators.INPUT_EMAIL, email)

    @allure.step('Заполнить поле "Пароль"')
    def fill_password_field(self, password):
        self.waiting_visibility_by_xpath(LoginPageLocators.INPUT_PASSWORD)
        self.fill_field_by_xpath(LoginPageLocators.INPUT_PASSWORD, password)

    @allure.step('Клик кнопке "Войти"')
    def click_login_button(self):
        self.waiting_visibility_by_xpath(LoginPageLocators.LOGIN_BUTTON)
        self.click_by_xpath(LoginPageLocators.LOGIN_BUTTON)
