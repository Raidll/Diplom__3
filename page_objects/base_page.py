from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def is_active(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def waiting_visibility_by_xpath(self, xpath):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(xpath))

    def scroll_to_element_by_xpath(self, xpath):
        element = self.driver.find_element(*xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_by_xpath(self, xpath):
        self.driver.find_element(*xpath).click()

    def fill_field_by_xpath(self, xpath, message):
        self.driver.find_element(*xpath).send_keys(message)

    def get_element_text_by_xpath(self, xpath):
        return self.driver.find_element(*xpath).text

    def waiting_invisibility_by_xpath(self, xpath):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element_located(xpath))

    def move_from_to(self, locator_from, locator_to):
        element_from = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            locator_from))
        element_to = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            locator_to))

        actions = ActionChains(self.driver)
        actions.click_and_hold(element_from) \
            .move_to_element(element_to).release().perform()
