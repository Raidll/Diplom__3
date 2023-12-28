import allure
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step('Получить текст из шапки страницы')
    def get_text_from_order_feed_header(self):
        self.waiting_visibility_by_xpath(OrderFeedPageLocators.ORDER_FEED_PAGE_HEADER)
        return self.get_element_text_by_xpath(OrderFeedPageLocators.ORDER_FEED_PAGE_HEADER)

    @allure.step('Ожидание видимости шапки страницы')
    def waiting_visibility_order_feed_page_header(self):
        self.waiting_visibility_by_xpath(OrderFeedPageLocators.ORDER_FEED_PAGE_HEADER)

    @allure.step('Клик по первому заказу')
    def click_first_order(self):
        self.waiting_visibility_by_xpath(OrderFeedPageLocators.FIRST_ORDER)
        self.click_by_xpath(OrderFeedPageLocators.FIRST_ORDER)

    @allure.step('Ожидание видимости попапа с информацией о заказе')
    def waiting_visibility_order_info(self):
        self.waiting_visibility_by_xpath(OrderFeedPageLocators.POPUP_WITH_ORDER_INFORMATION)

    @allure.step('Получить текст из попапа с информацией о заказе')
    def get_text_from_popup_with_order_info(self):
        self.waiting_visibility_by_xpath(OrderFeedPageLocators.POPUP_WITH_ORDER_INFORMATION)
        return self.get_element_text_by_xpath(OrderFeedPageLocators.POPUP_WITH_ORDER_INFORMATION)

    @allure.step('Получить номер верхнего заказа')
    def get_text_from_first_order(self):
        self.waiting_visibility_by_xpath(OrderFeedPageLocators.NUMBER_OF_FIRST_ORDER)
        return self.get_element_text_by_xpath(OrderFeedPageLocators.NUMBER_OF_FIRST_ORDER)

    @allure.step('Получить количество заказов за все время')
    def get_orders_count_for_all_time(self):
        self.waiting_visibility_by_xpath(OrderFeedPageLocators.ORDERS_COUNT_FOR_ALL_TIME)
        return self.get_element_text_by_xpath(OrderFeedPageLocators.ORDERS_COUNT_FOR_ALL_TIME)

    @allure.step('Получить количество заказов за день')
    def get_orders_count_in_a_day(self):
        self.waiting_visibility_by_xpath(OrderFeedPageLocators.ORDERS_COUNT_IN_A_DAY)
        return self.get_element_text_by_xpath(OrderFeedPageLocators.ORDERS_COUNT_IN_A_DAY)

    @allure.step('Получаем номер заявки')
    def get_text_from_orders_in_work(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*OrderFeedPageLocators.ORDERS_IN_WORK).text not in ("", "Все текущие заказы готовы!")
        )
        return self.driver.find_element(*OrderFeedPageLocators.ORDERS_IN_WORK).text
