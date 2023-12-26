import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class HomePage(BasePage):
    CREATE_ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"
    FLUORESCENT_BUN = By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']"
    INGREDIENT_DETAILS_POPUP = By.XPATH, ".//h2[text()='Детали ингредиента']"
    CLOSE_POPUP_BUTTON = By.XPATH, ".//button[@type='button']"
    BURGER_BASKET = By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]"
    COUNT_BUNS = By.XPATH, ".//p[@class='counter_counter__num__3nue1']"
    POPUP_WITH_ORDER_IDENTIFIER = By.XPATH, ".//p[text()='идентификатор заказа']"
    ORDER_NUMBER_FROM_POPUP = By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"

    @allure.step('Клик по кнопки "Оформить заказ"')
    def click_create_order_button(self):
        self.click_by_xpath(self.CREATE_ORDER_BUTTON)

    @allure.step('Ожидание видимости кнопки "Оформить заказ"')
    def waiting_visibility_create_order_button(self):
        self.waiting_visibility_by_xpath(self.CREATE_ORDER_BUTTON)

    @allure.step('Получить текст кнопки "Оформить заказ"')
    def get_text_from_create_order_button(self):
        return self.get_element_text_by_xpath(self.CREATE_ORDER_BUTTON)

    @allure.step('Ожидание видимости флуорисцентной булки в списке конструктора"')
    def waiting_visibility_fluorescent_bun(self):
        self.waiting_visibility_by_xpath(self.FLUORESCENT_BUN)

    @allure.step('Клик по флуорисцентной булке в списке конструктора"')
    def click_fluorescent_bun(self):
        self.click_by_xpath(self.FLUORESCENT_BUN)

    @allure.step('Ожидание видимости всплывающего окна с информацией о ингредиенте"')
    def waiting_visibility_ingredient_info_popup(self):
        self.waiting_visibility_by_xpath(self.INGREDIENT_DETAILS_POPUP)

    @allure.step('Получить текст из шапки в попапе с информацией о ингредиенте')
    def get_text_from_header_ingredient_info_popup(self):
        return self.get_element_text_by_xpath(self.INGREDIENT_DETAILS_POPUP)

    @allure.step('Ожидание видимости кнопки закрытия попапа')
    def waiting_visibility_close_popup_button(self):
        self.waiting_visibility_by_xpath(self.CLOSE_POPUP_BUTTON)

    @allure.step('Ожидание исчезновения попапа  синформацией о ингредиенте')
    def waiting_invisibility_popup_with_ingredient_info(self):
        self.waiting_invisibility_by_xpath(self.INGREDIENT_DETAILS_POPUP)

    @allure.step('Клик на кнопку закрытия попапа')
    def click_to_close_popup_button(self):
        self.click_by_xpath(self.CLOSE_POPUP_BUTTON)

    @allure.step('Перенести булку в корзину')
    def move_bun_in_basket(self):
        self.move_from_to(self.FLUORESCENT_BUN, self.BURGER_BASKET)

    @allure.step('Получить количество добавленных булок')
    def get_count_buns_in_basket(self):
        return self.get_element_text_by_xpath(self.COUNT_BUNS)

    @allure.step('Ожидание видимости попапа с идентификатором заказа')
    def waiting_visibility_popup_with_order_identifier(self):
        self.waiting_visibility_by_xpath(self.POPUP_WITH_ORDER_IDENTIFIER)

    @allure.step('Получить текст из попапа с информацией о созданном заказе')
    def get_text_from_popup_with_order_identifier(self):
        return self.get_element_text_by_xpath(self.POPUP_WITH_ORDER_IDENTIFIER)

    @allure.step('Получаем номер заявки')
    def get_order_number_from_home_page(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.ORDER_NUMBER_FROM_POPUP).text not in ("", "9999")
        )
        return self.driver.find_element(*self.ORDER_NUMBER_FROM_POPUP).text


