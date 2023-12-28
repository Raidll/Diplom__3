import allure

from data import helpers
from page_objects.home_page import HomePage
from page_objects.base_page import BasePage
from page_objects.order_feed_page import OrderFeedPage
from data.urls import URLS


class TestOrderFeed:
    @allure.title('проверка всплывающего окна с информацией о заказе')
    def test_popup_with_order_info(self, register_new_user_and_authorization_return_driver):
        home_page = HomePage(register_new_user_and_authorization_return_driver)
        home_page.click_order_feed_button()

        order_feed_page = OrderFeedPage(register_new_user_and_authorization_return_driver)
        order_feed_page.click_first_order()
        order_feed_page.waiting_visibility_order_info()

        assert 'Cостав' in order_feed_page.get_text_from_popup_with_order_info()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_displayed_in_order_history_and_in_order_feed(self, register_new_user_and_authorization_return_driver):
        home_page = HomePage(register_new_user_and_authorization_return_driver)
        home_page.move_bun_in_basket()
        home_page.click_create_order_button()
        order_number_from_home_page = home_page.get_order_number_from_home_page()

        order_feed_page = OrderFeedPage(register_new_user_and_authorization_return_driver)
        register_new_user_and_authorization_return_driver.get(URLS.ORDER_FEED_PAGE)
        order_number_from_feed_page = order_feed_page.get_text_from_first_order()

        assert order_number_from_feed_page.replace('#', '').split('0')[1] == order_number_from_home_page

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_increase_order_count(self, register_new_user_and_authorization_return_driver):
        driver = register_new_user_and_authorization_return_driver
        driver.get(URLS.ORDER_FEED_PAGE)
        order_feed_page = OrderFeedPage(driver)
        orders_count_for_all_time_old = order_feed_page.get_orders_count_for_all_time()

        driver.get(URLS.HOME_PAGE)
        home_page = HomePage(driver)
        home_page.move_bun_in_basket()
        home_page.click_create_order_button()

        driver.get(URLS.ORDER_FEED_PAGE)
        orders_count_for_all_time_new = order_feed_page.get_orders_count_for_all_time()

        assert int(orders_count_for_all_time_old) + 1 == int(orders_count_for_all_time_new)

    @allure.title('При создании нового заказа счётчик Выполнено за день увеличивается')
    def test_increase_order_count(self, register_new_user_and_authorization_return_driver):
        driver = register_new_user_and_authorization_return_driver

        driver.get(URLS.ORDER_FEED_PAGE)
        order_feed_page = OrderFeedPage(driver)
        orders_count_in_a_day_old = order_feed_page.get_orders_count_in_a_day()

        driver.get(URLS.HOME_PAGE)
        home_page = HomePage(driver)
        home_page.move_bun_in_basket()
        home_page.click_create_order_button()

        driver.get(URLS.ORDER_FEED_PAGE)
        orders_count_in_a_day_new = order_feed_page.get_orders_count_in_a_day()

        assert int(orders_count_in_a_day_old) + 1 == int(orders_count_in_a_day_new)

    @allure.title('При создании нового заказа он появляется в разделе "В работе"')
    def test_numbers_of_orders_in_work(self, register_new_user_and_authorization_return_driver):
        driver = register_new_user_and_authorization_return_driver

        home_page = HomePage(driver)
        home_page.move_bun_in_basket()
        home_page.click_create_order_button()
        order_number_from_home_page = home_page.get_order_number_from_home_page()

        driver.get(URLS.ORDER_FEED_PAGE)
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.waiting_visibility_order_feed_page_header()

        assert order_number_from_home_page in order_feed_page.get_text_from_orders_in_work().split('0')[1]

