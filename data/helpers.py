import string
import random
from data.urls import URLS
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def authorization_by_login_and_password(driver, email, password):
    driver.get(URLS.LOGIN_PAGE)

    login_page = LoginPage(driver)
    login_page.waiting_visibility_email_input()
    login_page.fill_email_field(email)
    login_page.fill_password_field(password)
    login_page.click_login_button()

    home_page = HomePage(driver)
    home_page.waiting_visibility_create_order_button()

