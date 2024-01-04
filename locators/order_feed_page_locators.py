from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_PAGE_HEADER = By.XPATH, ".//h1[text()='Лента заказов']"
    FIRST_ORDER = By.XPATH, ".//a[@class='OrderHistory_link__1iNby']"
    POPUP_WITH_ORDER_INFORMATION = By.XPATH, (".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X "
                                              "p-10']")
    NUMBER_OF_FIRST_ORDER = By.XPATH, ".//p[@class='text text_type_digits-default']"
    ORDERS_COUNT_FOR_ALL_TIME = By.XPATH, ".//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    ORDERS_COUNT_IN_A_DAY = By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]"
    ORDERS_IN_WORK = By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"
