import allure

from data import helpers
from data.urls import URLS
from page_objects.base_page import BasePage
from page_objects.home_page import HomePage
from page_objects.order_feed_page import OrderFeedPage


class TestMainFunctionality:
    @allure.title('Проверка кнопки "Конструктор"')
    @allure.description('Проверка перехода в конструктор')
    def test_constructor_button(self, register_new_user_and_authorization_return_driver):
        home_page = HomePage(register_new_user_and_authorization_return_driver)
        home_page.click_personal_area_button()
        home_page.click_constructor_button()

        assert home_page.get_text_from_create_order_button() == "Оформить заказ"
        assert home_page.get_current_url() == URLS.HOME_PAGE

    @allure.title('Проверка перехода в ленту заказов')
    @allure.description('Проверка перехода нас траницу ленты заказов')
    def test_go_to_order_feed_page(self, register_new_user_and_authorization_return_driver):
        home_page = HomePage(register_new_user_and_authorization_return_driver)
        home_page.waiting_visibility_personal_area_button()
        home_page.click_personal_area_button()
        home_page.waiting_visibility_order_feed_button()
        home_page.click_order_feed_button()

        order_feed_page = OrderFeedPage(register_new_user_and_authorization_return_driver)
        order_feed_page.waiting_visibility_order_feed_page_header()
        assert order_feed_page.get_text_from_order_feed_header() == "Лента заказов"
        assert order_feed_page.get_current_url() == URLS.ORDER_FEED_PAGE

    @allure.title('Проверка появления всплывающего окна')
    @allure.description('Всплывающее окно появляется при клике на ингредиент')
    def test_popup_will_appear_if_click_to_ingredient(self, register_new_user_and_authorization_return_driver):
        home_page = HomePage(register_new_user_and_authorization_return_driver)
        home_page.click_fluorescent_bun()
        home_page.waiting_visibility_ingredient_info_popup()

        assert home_page.get_text_from_header_ingredient_info_popup() == "Детали ингредиента"

    @allure.title('Проверка кликабельности крестика всплывающего окна')
    @allure.description('Всплывающее окно можно закрыть нажатием на крестик')
    def test_popup_with_ingredient_info_can_be_closed(self, register_new_user_and_authorization_return_driver):
        home_page = HomePage(register_new_user_and_authorization_return_driver)
        home_page.click_fluorescent_bun()
        home_page.click_to_close_popup_button()
        home_page.waiting_invisibility_popup_with_ingredient_info()

        assert home_page.get_text_from_header_ingredient_info_popup() == ""

    @allure.title('Проверка изменения счетчика ингредиента')
    @allure.description('Изменения счетчика ингредиента при переносе в корзину')
    def test_ingredient_count_in_basket(self, register_new_user_and_authorization_return_driver):
        home_page = HomePage(register_new_user_and_authorization_return_driver)
        home_page.move_bun_in_basket()

        assert int(home_page.get_count_buns_in_basket()) == 2

    @allure.title('Создание заказа')
    @allure.description('Проверка успешного создания заказа залогиненным пользователем')
    def test_create_order_by_authorized_user(self, register_new_user_and_authorization_return_driver):
        home_page = HomePage(register_new_user_and_authorization_return_driver)
        home_page.move_bun_in_basket()
        home_page.click_create_order_button()
        home_page.waiting_visibility_popup_with_order_identifier()

        assert home_page.get_text_from_popup_with_order_identifier() == 'идентификатор заказа'





