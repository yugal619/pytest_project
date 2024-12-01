from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    # Locators
    LIST_OF_EXAMPLES = (By.TAG_NAME, 'li')
    BASIC_WEB_PAGE_EXAMPLE = (By.ID, 'basicpagetest')

    def __init__(self, driver):
        """
        Initializes the Page Object with the given WebDriver instance.

        Args:
            driver: The WebDriver instance to be used.
        """
        super().__init__(driver)

    def count_examples(self):
        """
        Counts the number of examples in the list of examples.

        Returns:
            The number of examples.
        """
        examples = self.find_elements(*self.LIST_OF_EXAMPLES)
        return len(examples)

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
        self.find_element(*self.BASIC_WEB_PAGE_EXAMPLE).click()
        title = self.get_title()
        if title == 'Basic Web Page Title':
            return True
        else:
            return False
