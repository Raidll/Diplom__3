import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):

    @allure.step('Клик по кнопки "Оформить заказ"')
    def click_create_order_button(self):
        self.waiting_visibility_by_xpath(HomePageLocators.CREATE_ORDER_BUTTON)
        self.click_by_xpath(HomePageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Ожидание видимости кнопки "Оформить заказ"')
    def waiting_visibility_create_order_button(self):
        self.waiting_visibility_by_xpath(HomePageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Получить текст кнопки "Оформить заказ"')
    def get_text_from_create_order_button(self):
        self.waiting_visibility_by_xpath(HomePageLocators.CREATE_ORDER_BUTTON)
        return self.get_element_text_by_xpath(HomePageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Ожидание видимости флуорисцентной булки в списке конструктора"')
    def waiting_visibility_fluorescent_bun(self):
        self.waiting_visibility_by_xpath(HomePageLocators.FLUORESCENT_BUN)

    @allure.step('Клик по флуорисцентной булке в списке конструктора"')
    def click_fluorescent_bun(self):
        self.waiting_visibility_by_xpath(HomePageLocators.FLUORESCENT_BUN)
        self.click_by_xpath(HomePageLocators.FLUORESCENT_BUN)

    @allure.step('Ожидание видимости всплывающего окна с информацией о ингредиенте"')
    def waiting_visibility_ingredient_info_popup(self):
        self.waiting_visibility_by_xpath(HomePageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Получить текст из шапки в попапе с информацией о ингредиенте')
    def get_text_from_header_ingredient_info_popup(self):
        return self.get_element_text_by_xpath(HomePageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Ожидание видимости кнопки закрытия попапа')
    def waiting_visibility_close_popup_button(self):
        self.waiting_visibility_by_xpath(HomePageLocators.CLOSE_POPUP_BUTTON)

    @allure.step('Ожидание исчезновения попапа  синформацией о ингредиенте')
    def waiting_invisibility_popup_with_ingredient_info(self):
        self.waiting_invisibility_by_xpath(HomePageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Клик на кнопку закрытия попапа')
    def click_to_close_popup_button(self):
        self.waiting_visibility_by_xpath(HomePageLocators.CLOSE_POPUP_BUTTON)
        self.click_by_xpath(HomePageLocators.CLOSE_POPUP_BUTTON)

    @allure.step('Перенести булку в корзину')
    def move_bun_in_basket(self):
        self.waiting_visibility_by_xpath(HomePageLocators.FLUORESCENT_BUN)
        self.waiting_visibility_by_xpath(HomePageLocators.BURGER_BASKET)
        self.move_from_to(HomePageLocators.FLUORESCENT_BUN, HomePageLocators.BURGER_BASKET)

    @allure.step('Получить количество добавленных булок')
    def get_count_buns_in_basket(self):
        self.waiting_visibility_by_xpath(HomePageLocators.COUNT_BUNS)
        return self.get_element_text_by_xpath(HomePageLocators.COUNT_BUNS)

    @allure.step('Ожидание видимости попапа с идентификатором заказа')
    def waiting_visibility_popup_with_order_identifier(self):
        self.waiting_visibility_by_xpath(HomePageLocators.POPUP_WITH_ORDER_IDENTIFIER)

    @allure.step('Получить текст из попапа с информацией о созданном заказе')
    def get_text_from_popup_with_order_identifier(self):
        return self.get_element_text_by_xpath(HomePageLocators.POPUP_WITH_ORDER_IDENTIFIER)

    @allure.step('Получаем номер заявки')
    def get_order_number_from_home_page(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*HomePageLocators.ORDER_NUMBER_FROM_POPUP).text not in ("", "9999")
        )
        return self.driver.find_element(*HomePageLocators.ORDER_NUMBER_FROM_POPUP).text

    @allure.step('Клик на "Личный кабинет"')
    def click_personal_area_button(self):
        self.click_by_xpath(HomePageLocators.PERSONAL_AREA_BUTTON)

    @allure.step('Клик на "Конструктор')
    def click_constructor_button(self):
        self.click_by_xpath(HomePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Ожидание видимости кнопки "Личный кабинет"')
    def waiting_visibility_personal_area_button(self):
        self.waiting_visibility_by_xpath(HomePageLocators.PERSONAL_AREA_BUTTON)

    @allure.step('Ожидание видимости кнопки "Конструктор"')
    def waiting_visibility_constructor_button(self):
        self.waiting_visibility_by_xpath(HomePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Ожидание видимости кнопки "Лента заказов"')
    def waiting_visibility_order_feed_button(self):
        self.waiting_visibility_by_xpath(HomePageLocators.ORDER_FEED_BUTTON)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_order_feed_button(self):
        self.click_by_xpath(HomePageLocators.ORDER_FEED_BUTTON)
