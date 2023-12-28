import allure
from data import helpers
from page_objects.home_page import HomePage
from page_objects.personal_area_page import PersonalAreaPage
from page_objects.login_page import LoginPage
from data.urls import URLS


class TestPersonalArea:
    @allure.title('Проверка кнопки "Личный кабинет"')
    @allure.description('Проверка перехода в личный кабинет авторизованного пользователя')
    def test_click_personal_area_button(self, register_new_user_and_authorization_return_driver):
        driver = register_new_user_and_authorization_return_driver

        home_page = HomePage(driver)
        home_page.waiting_visibility_personal_area_button()
        home_page.click_personal_area_button()

        personal_area_page = PersonalAreaPage(driver)
        personal_area_page.waiting_visibility_orders_history_button()
        assert home_page.get_current_url() == URLS.PROFILE_PAGE

    @allure.title('Проверка кнопки "История заказов"')
    @allure.description('Проверка перехода в историю заказов авторизованного пользователя')
    def test_go_to_orders_history(self, register_new_user_and_authorization_return_driver):
        driver = register_new_user_and_authorization_return_driver

        home_page = HomePage(driver)
        home_page.waiting_visibility_personal_area_button()
        home_page.click_personal_area_button()

        personal_area_page = PersonalAreaPage(driver)
        personal_area_page.click_orders_history_button()

        assert personal_area_page.get_current_url() == URLS.ORDERS_HISTORY_PAGE

    @allure.title('Проверка кнопки "Выход"')
    @allure.description('Проверка выхода пользователя из личного кабинета')
    def test_logout_user_success(self, register_new_user_and_authorization_return_driver):
        driver = register_new_user_and_authorization_return_driver

        home_page = HomePage(driver)
        home_page.click_personal_area_button()

        personal_area_page = PersonalAreaPage(driver)
        personal_area_page.click_exit_button()

        login_page = LoginPage(driver)
        login_page.waiting_visibility_forgot_password_button()

        assert login_page.get_current_url() == URLS.LOGIN_PAGE

