import allure

from page_objects.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):

    @allure.step('Ожидание видимости инпута "Введите код из письма"')
    def waiting_visibility_input_code_from_email(self):
        self.waiting_visibility_by_xpath(ResetPasswordPageLocators.INPUT_CODE_FROM_EMAIL)

    @allure.step('Ожидание видимости поля ввода пароля')
    def waiting_visibility_input_password(self):
        self.waiting_visibility_by_xpath(ResetPasswordPageLocators.INPUT_PASSWORD)

    @allure.step('Ввести пароль')
    def fill_password_field(self, password):
        self.waiting_visibility_by_xpath(ResetPasswordPageLocators.INPUT_PASSWORD)
        self.fill_field_by_xpath(ResetPasswordPageLocators.INPUT_PASSWORD, password)

    @allure.step('Клик по переключателю видимости пароля')
    def click_display_password_button(self):
        self.waiting_visibility_by_xpath(ResetPasswordPageLocators.DISPLAY_PASSWORD_BUTTON)
        self.click_by_xpath(ResetPasswordPageLocators.DISPLAY_PASSWORD_BUTTON)

    @allure.step('Проверка видимости пароля')
    def display_password_is_active(self):
        self.waiting_visibility_by_xpath(ResetPasswordPageLocators.PASSWORD_INPUT_STATUS_ACTIVE)
        return self.is_active(ResetPasswordPageLocators.PASSWORD_INPUT_STATUS_ACTIVE)


