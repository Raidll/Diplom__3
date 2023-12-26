import allure

from data import helpers
from page_objects.home_page import HomePage
from page_objects.base_page import BasePage
from page_objects.order_feed_page import OrderFeedPage
from data.urls import URLS


class TestOrderFeed:
    @allure.title('проверка всплывающего окна с информацией о заказе')
    def test_popup_with_order_info(self, driver, register_new_user_return_user_data):
        user_email = register_new_user_return_user_data.get('email')
        user_password = register_new_user_return_user_data.get('password')

        helpers.authorization_by_login_and_password(driver, user_email, user_password)
        base_page = BasePage(driver)
        base_page.waiting_visibility_order_feed_button()
        base_page.click_order_feed_button()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.waiting_visibility_order_feed_page_header()
        order_feed_page.click_first_order()
        order_feed_page.waiting_visibility_order_info()

        assert 'Cостав' in order_feed_page.get_text_from_popup_with_order_info()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_displayed_in_order_history_and_in_order_feed(self, driver, register_new_user_return_user_data):
        user_email = register_new_user_return_user_data.get('email')
        user_password = register_new_user_return_user_data.get('password')

        helpers.authorization_by_login_and_password(driver, user_email, user_password)
        home_page = HomePage(driver)
        home_page.waiting_visibility_fluorescent_bun()
        home_page.move_bun_in_basket()
        home_page.waiting_visibility_create_order_button()
        home_page.click_create_order_button()
        home_page.waiting_visibility_popup_with_order_identifier()
        order_number_from_home_page = home_page.get_order_number_from_home_page()

        order_feed_page = OrderFeedPage(driver)
        driver.get(URLS.ORDER_FEED_PAGE)
        order_feed_page.waiting_visibility_order_feed_page_header()
        order_number_from_feed_page = order_feed_page.get_text_from_first_order()

        assert order_number_from_feed_page.replace('#', '').split('0')[1] == order_number_from_home_page

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_increase_order_count(self, driver, register_new_user_return_user_data):
        user_email = register_new_user_return_user_data.get('email')
        user_password = register_new_user_return_user_data.get('password')

        helpers.authorization_by_login_and_password(driver, user_email, user_password)
        driver.get(URLS.ORDER_FEED_PAGE)
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.waiting_visibility_order_feed_page_header()
        orders_count_for_all_time_old = order_feed_page.get_orders_count_for_all_time()

        driver.get(URLS.HOME_PAGE)
        home_page = HomePage(driver)
        home_page.waiting_visibility_fluorescent_bun()
        home_page.move_bun_in_basket()
        home_page.waiting_visibility_create_order_button()
        home_page.click_create_order_button()
        home_page.waiting_visibility_popup_with_order_identifier()

        driver.get(URLS.ORDER_FEED_PAGE)
        order_feed_page.waiting_visibility_order_feed_page_header()
        orders_count_for_all_time_new = order_feed_page.get_orders_count_for_all_time()

        assert int(orders_count_for_all_time_old) + 1 == int(orders_count_for_all_time_new)

    @allure.title('При создании нового заказа счётчик Выполнено за день увеличивается')
    def test_increase_order_count(self, driver, register_new_user_return_user_data):
        user_email = register_new_user_return_user_data.get('email')
        user_password = register_new_user_return_user_data.get('password')

        helpers.authorization_by_login_and_password(driver, user_email, user_password)
        driver.get(URLS.ORDER_FEED_PAGE)
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.waiting_visibility_order_feed_page_header()
        orders_count_in_a_day_old = order_feed_page.get_orders_count_in_a_day()

        driver.get(URLS.HOME_PAGE)
        home_page = HomePage(driver)
        home_page.waiting_visibility_fluorescent_bun()
        home_page.move_bun_in_basket()
        home_page.waiting_visibility_create_order_button()
        home_page.click_create_order_button()
        home_page.waiting_visibility_popup_with_order_identifier()

        driver.get(URLS.ORDER_FEED_PAGE)
        order_feed_page.waiting_visibility_order_feed_page_header()
        orders_count_in_a_day_new = order_feed_page.get_orders_count_in_a_day()

        assert int(orders_count_in_a_day_old) + 1 == int(orders_count_in_a_day_new)

    @allure.title('При создании нового заказа он появляется в разделе "В работе"')
    def test_numbers_of_orders_in_work(self, driver, register_new_user_return_user_data):
        user_email = register_new_user_return_user_data.get('email')
        user_password = register_new_user_return_user_data.get('password')

        helpers.authorization_by_login_and_password(driver, user_email, user_password)
        home_page = HomePage(driver)
        home_page.waiting_visibility_fluorescent_bun()
        home_page.move_bun_in_basket()
        home_page.waiting_visibility_create_order_button()
        home_page.click_create_order_button()
        home_page.waiting_visibility_popup_with_order_identifier()
        order_number_from_home_page = home_page.get_order_number_from_home_page()

        driver.get(URLS.ORDER_FEED_PAGE)
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.waiting_visibility_order_feed_page_header()

        assert order_number_from_home_page in order_feed_page.get_text_from_orders_in_work().split('0')[1]

