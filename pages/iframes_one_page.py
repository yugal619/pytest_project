from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class IFrameOnePage(BasePage):
    """
    This class represents the IFrame One Page on Test Pages.
    It provides methods to interact with elements within the left and right frames.

    Attributes:
        driver (WebDriver): The WebDriver instance used to interact with the page.
    """

    # Locators
    BASIC_WEB_PAGE_EXAMPLE = (By.ID, 'basicpagetest')
    HEADER = (By.XPATH, '//h1')
    LIST = (By.XPATH, '//li')

    def __init__(self, driver):
        """
        Initializes the IFrameOnePage object with the given WebDriver instance.

        Args:
            driver (WebDriver): The WebDriver instance to use for interacting with the page.
        """
        super().__init__(driver)
        driver.get('https://testpages.eviltester.com/styled/frames/frames-test.html')

    def switch_to_left_frame(self):
        """
        Switches the WebDriver focus to the left frame.
        """
        self.driver.switch_to.frame("left")

    def switch_to_right_frame(self):
        """
        Switches the WebDriver focus to the right frame.
        """
        self.driver.switch_to.frame("right")

    def get_text_from_left_frame(self):
        """
        Gets the text from the header element within the left frame.

        Returns:
            str: The text content of the header element in the left frame.
        """
        self.switch_to_left_frame()
        return self.find_element(self.HEADER).text

    def get_list_from_left_frame(self):
        """
        Gets the text from the list element within the left frame.

        Returns:
            str: The text content of the list element in the left frame.
        """
        self.switch_to_left_frame()
        return self.find_element(self.LIST).text

    def get_text_from_right_frame(self):
        """
        Gets the text from the header element within the right frame.

        Returns:
            str: The text content of the header element in the right frame.
        """
        self.switch_to_right_frame()
        return self.find_element(self.HEADER).text

    def get_list_from_right_frame(self):
        """
        Gets the text from the list element within the right frame.

        Returns:
            str: The text content of the list element in the right frame.
        """
        self.switch_to_right_frame()
        return self.find_element(self.LIST).text