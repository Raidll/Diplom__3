import allure
import requests
from selenium import webdriver
import pytest

from data import helpers
from data.urls import URLS


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Создание webDriver")
@allure.description("Создание webDriver для прогона тестов в chrome и firefox")
@pytest.fixture(scope='function', params=["chrome", "firefox"])
def driver1(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    yield driver
    driver.quit()


@allure.title("Регистрация нового пользователя и удаление после теста. Возвращаемые значения - name, email, password")
@allure.description(
    "Регистрация пользователя, возврат response и удаление пользователя после теста. Возвращаемые значения - name, email, password")
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
