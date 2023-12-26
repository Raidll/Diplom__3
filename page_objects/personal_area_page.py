import allure
from selenium.webdriver.common.by import By

from page_objects.home_page import BasePage


class PersonalAreaPage(BasePage):
    ORDERS_HISTORY_BUTTON = By.XPATH, ".//a[text()='История заказов']"
    EXIT_BUTTON = By.XPATH, ".//button[text()='Выход']"

    @allure.step('Ожидание видимости кнопки "История заказов"')
    def waiting_visibility_orders_history_button(self):
        self.waiting_visibility_by_xpath(self.ORDERS_HISTORY_BUTTON)

    @allure.step('Клик по кнопке "История заказов"')
    def click_orders_history_button(self):
        self.click_by_xpath(self.ORDERS_HISTORY_BUTTON)

    @allure.step('Ожидание видимости кнопки "Выход"')
    def waiting_visibility_exit_button(self):
        self.waiting_visibility_by_xpath(self.EXIT_BUTTON)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_button(self):
        self.click_by_xpath(self.EXIT_BUTTON)
