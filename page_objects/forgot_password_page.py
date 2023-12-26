import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ForgotPasswordPage(BasePage):
    RESTORE_BUTTON = By.XPATH, ".//button[text()='Восстановить']"
    INPUT_EMAIL = By.XPATH, ".//input[@name='name']"

    @allure.step('Ожидание видимости кнопки "Восстановить"')
    def waiting_visibility_restore_button(self):
        self.waiting_visibility_by_xpath(self.RESTORE_BUTTON)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_restore_button(self):
        self.click_by_xpath(self.RESTORE_BUTTON)

    @allure.step('Ожидание видимости инпута "Email"')
    def waiting_visibility_email_input(self):
        self.waiting_visibility_by_xpath(self.INPUT_EMAIL)

    @allure.step('Заполнить поле "Email"')
    def fill_email_field(self, email):
        self.fill_field_by_xpath(self.INPUT_EMAIL, email)
