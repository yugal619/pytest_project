from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """
    This class represents the Home Page on Test Pages.
    It provides methods to interact with various form elements and retrieve their values.

    Attributes:
        driver (WebDriver): The WebDriver instance used to interact with the page.
    """

    # Locators
    BASIC_WEB_PAGE_EXAMPLE = (By.ID, 'basicpagetest')

    def __init__(self, driver):
        """
        Initializes the Page Object with the given WebDriver instance.

        Args:
            driver: The WebDriver instance to be used.
        """
        super().__init__(driver)
        driver.get('https://testpages.eviltester.com/styled/index.html')

    def enter_password(self, password):
        """
        Enters the given password into the password field.

        Args:
            password: The password to be entered.
        """
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def open_basic_web_page(self):
        """
        Opens the basic web page and verifies the title.

        Returns:
            True if the page is opened successfully, False otherwise.
        """
        self.find_element(self.BASIC_WEB_PAGE_EXAMPLE).click()
        title = self.get_title()
        if title == 'Basic Web Page Title':
            return True
        else:
            return False
