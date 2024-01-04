from selenium.webdriver.common.by import By


class HomePageLocators:
    CREATE_ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"
    FLUORESCENT_BUN = By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']"
    INGREDIENT_DETAILS_POPUP = By.XPATH, ".//h2[text()='Детали ингредиента']"
    CLOSE_POPUP_BUTTON = By.XPATH, ".//button[@type='button']"
    BURGER_BASKET = By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]"
    COUNT_BUNS = By.XPATH, ".//p[@class='counter_counter__num__3nue1']"
    POPUP_WITH_ORDER_IDENTIFIER = By.XPATH, ".//p[text()='идентификатор заказа']"
    ORDER_NUMBER_FROM_POPUP = By.XPATH, (".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m "
                                         "text text_type_digits-large mb-8']")
    PERSONAL_AREA_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']"
    ORDER_FEED_BUTTON = By.XPATH, ".//p[text()='Лента Заказов']"
