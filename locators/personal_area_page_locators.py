from selenium.webdriver.common.by import By


class PersonalAreaPageLocators:
    ORDERS_HISTORY_BUTTON = By.XPATH, ".//a[text()='История заказов']"
    EXIT_BUTTON = By.XPATH, ".//button[text()='Выход']"
