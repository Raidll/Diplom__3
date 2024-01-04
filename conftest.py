import allure
import requests
from selenium import webdriver
import pytest

from data import helpers
from data.urls import URLS
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage


@allure.step("Создание webDriver для прогона тестов в chrome и firefox")
@pytest.fixture(scope='function', params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    yield driver
    driver.quit()


@allure.step("Регистрация нового пользователя и удаление после теста. Возвращаемые значения - name, email, password")
@pytest.fixture
def register_new_user_return_user_data():
    user_data = {}
    email = f'{helpers.generate_random_string(10)}@mail.ru'
    password = helpers.generate_random_string(10)
    name = helpers.generate_random_string(10)
    user_data['email'] = email
    user_data['password'] = password
    user_data['name'] = name

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(URLS.API_URL_CREATE_NEW_USER, data=payload)
    user_token = response.json()['accessToken']
    user_data['token'] = user_token
    yield user_data
    requests.delete(URLS.API_URL_DELETE_USER, headers={'Authorization': user_token})
@pytest.fixture(scope='function', params=["chrome", "firefox"])
def register_new_user_and_authorization_return_driver(request):
    user_data = {}
    email = f'{helpers.generate_random_string(10)}@mail.ru'
    password = helpers.generate_random_string(10)
    name = helpers.generate_random_string(10)
    user_data['email'] = email
    user_data['password'] = password
    user_data['name'] = name

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(URLS.API_URL_CREATE_NEW_USER, data=payload)
    user_token = response.json()['accessToken']
    user_data['token'] = user_token

    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    driver.get(URLS.LOGIN_PAGE)

    login_page = LoginPage(driver)
    login_page.waiting_visibility_email_input()
    login_page.fill_email_field(email)
    login_page.fill_password_field(password)
    login_page.click_login_button()

    home_page = HomePage(driver)
    home_page.waiting_visibility_create_order_button()

    yield driver
    requests.delete(URLS.API_URL_DELETE_USER, headers={'Authorization': user_token})
    driver.quit()
