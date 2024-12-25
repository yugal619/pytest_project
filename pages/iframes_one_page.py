from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class IFrameOnePage(BasePage):

    # Locators
    BASIC_WEB_PAGE_EXAMPLE = (By.ID, 'basicpagetest')
    HEADER = (By.XPATH, '//h1')
    LIST = (By.XPATH, '//li')

    def __init__(self, driver):
        """
        Initializes the Page Object with the given WebDriver instance.

        Args:
            driver: The WebDriver instance to be used.
        """
        super().__init__(driver)
        driver.get('https://testpages.eviltester.com/styled/frames/frames-test.html')

    def get_text_from_left_frame(self):
        self.driver.switch_to.frame("left")
        return self.find_element(self.HEADER).text

    def get_list_from_left_frame(self):
        self.driver.switch_to.frame("left")
        return self.find_element(self.LIST).text

    def get_text_from_right_frame(self):
        self.driver.switch_to.frame("right")
        return self.find_element(self.HEADER).text

    def get_list_from_right_frame(self):
        self.driver.switch_to.frame("right")
        return self.find_element(self.LIST).text
