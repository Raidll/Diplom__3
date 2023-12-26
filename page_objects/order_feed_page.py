import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class OrderFeedPage(BasePage):
    ORDER_FEED_PAGE_HEADER = By.XPATH, ".//h1[text()='Лента заказов']"
    FIRST_ORDER = By.XPATH, ".//a[@class='OrderHistory_link__1iNby']"
    POPUP_WITH_ORDER_INFORMATION = By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"
    NUMBER_OF_FIRST_ORDER = By.XPATH, ".//p[@class='text text_type_digits-default']"
    ORDERS_COUNT_FOR_ALL_TIME = By.XPATH, ".//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    ORDERS_COUNT_IN_A_DAY = By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]"
    ORDERS_IN_WORK = By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"

    @allure.step('Получить текст из шапки страницы')
    def get_text_from_order_feed_header(self):
        return self.get_element_text_by_xpath(self.ORDER_FEED_PAGE_HEADER)

    @allure.step('Ожидание видимости шапки страницы')
    def waiting_visibility_order_feed_page_header(self):
        self.waiting_visibility_by_xpath(self.ORDER_FEED_PAGE_HEADER)

    @allure.step('Клик по первому заказу')
    def click_first_order(self):
        self.click_by_xpath(self.FIRST_ORDER)

    @allure.step('Ожидание видимости попапа с информацией о заказе')
    def waiting_visibility_order_info(self):
        self.waiting_visibility_by_xpath(self.POPUP_WITH_ORDER_INFORMATION)

    @allure.step('Получить текст из попапа с информацией о заказе')
    def get_text_from_popup_with_order_info(self):
        return self.get_element_text_by_xpath(self.POPUP_WITH_ORDER_INFORMATION)

    @allure.step('Получить номер верхнего заказа')
    def get_text_from_first_order(self):
        return self.get_element_text_by_xpath(self.NUMBER_OF_FIRST_ORDER)

    @allure.step('Получить количество заказов за все время')
    def get_orders_count_for_all_time(self):
        return self.get_element_text_by_xpath(self.ORDERS_COUNT_FOR_ALL_TIME)

    @allure.step('Получить количество заказов за день')
    def get_orders_count_in_a_day(self):
        return self.get_element_text_by_xpath(self.ORDERS_COUNT_IN_A_DAY)


    @allure.step('Получаем номер заявки')
    def get_text_from_orders_in_work(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.ORDERS_IN_WORK).text not in ("", "Все текущие заказы готовы!")
        )
        return self.driver.find_element(*self.ORDERS_IN_WORK).text



