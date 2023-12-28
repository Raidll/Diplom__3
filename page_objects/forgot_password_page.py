import allure
from page_objects.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):

    @allure.step('Ожидание видимости кнопки "Восстановить"')
    def waiting_visibility_restore_button(self):
        self.waiting_visibility_by_xpath(ForgotPasswordPageLocators.RESTORE_BUTTON)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_restore_button(self):
        self.waiting_visibility_by_xpath(ForgotPasswordPageLocators.RESTORE_BUTTON)
        self.click_by_xpath(ForgotPasswordPageLocators.RESTORE_BUTTON)

    @allure.step('Ожидание видимости инпута "Email"')
    def waiting_visibility_email_input(self):
        self.waiting_visibility_by_xpath(ForgotPasswordPageLocators.INPUT_EMAIL)

    @allure.step('Заполнить поле "Email"')
    def fill_email_field(self, email):
        self.waiting_visibility_by_xpath(ForgotPasswordPageLocators.INPUT_EMAIL)
        self.fill_field_by_xpath(ForgotPasswordPageLocators.INPUT_EMAIL, email)
