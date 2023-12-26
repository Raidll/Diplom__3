import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ResetPasswordPage(BasePage):
    INPUT_CODE_FROM_EMAIL = By.XPATH, ".//label[text()='Введите код из письма']"
    INPUT_PASSWORD = By.XPATH, ".//input[@type='password']"
    DISPLAY_PASSWORD_BUTTON = By.XPATH, "//div[contains(@class, 'input__icon')]"
    PASSWORD_INPUT_STATUS_ACTIVE = By.XPATH, "//div[contains(@class, 'input_status_active')]"

    @allure.step('Ожидание видимости инпута "Введите код из письма"')
    def waiting_visibility_input_code_from_email(self):
        self.waiting_visibility_by_xpath(self.INPUT_CODE_FROM_EMAIL)

    @allure.step('Ожидание видимости поля ввода пароля')
    def waiting_visibility_input_password(self):
        self.waiting_visibility_by_xpath(self.INPUT_PASSWORD)

    @allure.step('Ввести пароль')
    def fill_password_field(self, password):
        self.fill_field_by_xpath(self.INPUT_PASSWORD, password)

    @allure.step('Клик по переключателю видимости пароля')
    def click_display_password_button(self):
        self.click_by_xpath(self.DISPLAY_PASSWORD_BUTTON)

    @allure.step('Проверка видимости пароля')
    def display_password_is_active(self):
        return self.is_active(self.PASSWORD_INPUT_STATUS_ACTIVE)


