import allure

from page_objects.home_page import BasePage
from locators.personal_area_page_locators import PersonalAreaPageLocators


class PersonalAreaPage(BasePage):

    @allure.step('Ожидание видимости кнопки "История заказов"')
    def waiting_visibility_orders_history_button(self):
        self.waiting_visibility_by_xpath(PersonalAreaPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Клик по кнопке "История заказов"')
    def click_orders_history_button(self):
        self.waiting_visibility_by_xpath(PersonalAreaPageLocators.ORDERS_HISTORY_BUTTON)
        self.click_by_xpath(PersonalAreaPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Ожидание видимости кнопки "Выход"')
    def waiting_visibility_exit_button(self):
        self.waiting_visibility_by_xpath(PersonalAreaPageLocators.EXIT_BUTTON)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_button(self):
        self.waiting_visibility_by_xpath(PersonalAreaPageLocators.EXIT_BUTTON)
        self.click_by_xpath(PersonalAreaPageLocators.EXIT_BUTTON)
