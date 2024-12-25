from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import logging
from selenium.common.exceptions import TimeoutException

# Create a logger for this module
logger = logging.getLogger(__name__)


class HtmlPage(BasePage):

    # Locators
    LIST_OF_EXAMPLES = (By.TAG_NAME, 'li')
    CHECKBOX = (By.XPATH, '//*[@value="{value}"]')
    BASIC_WEB_PAGE_EXAMPLE = (By.ID, 'basicpagetest')
    USERNAME = (By.XPATH, '//*[@name="username"]')
    PASSWORD = (By.XPATH, '//*[@name="password"]')
    COMMENT = (By.XPATH, '//*[@name="comments"]')
    RADIOBUTTON = (By.XPATH, '//*[@value="rd3"]')
    MULTIPLE_SELECT = (By.XPATH, '//*[@name="multipleselect[]"]')
    DROPDOWN = (By.XPATH, '//*[@name="dropdown"]')
    CHOOSE_FILE = (By.XPATH, '//input[@type="file"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@value="submit"]')

    def __init__(self, driver):
        """
        Initializes the Page Object with the given WebDriver instance.

        Args:
            driver: The WebDriver instance to be used.
        """
        super().__init__(driver)
        driver.get('https://testpages.eviltester.com/styled/basic-html-form-test.html')

    @classmethod
    def update_locator(cls, locator, value):
        """
        Generates a dynamic locator by formatting the pattern with the given value.

        Args:
            locator: A tuple containing the locator type and pattern.
            value: The value to be formatted into the pattern.

        Returns:
            A tuple containing the updated locator type and pattern.
        """
        return (locator[0], locator[1].format(value=value))

    def upload_file(self, file_path):
        """
        Uploads a file to the specified file input field.

        Args:
            file_path: The path to the file to be uploaded.
        """
        file_input = self.find_element((By.XPATH, '//input[@type="file"]'))
        file_input.send_keys(os.path.abspath(file_path))

    def enter_username(self, username):
        """
                Enters the given username into the username field.

                Args:
                    username: The username to be entered.

                Returns:
                    HomePage: Current page object for method chaining
                """
        try:
            # Use the base class method for finding and interacting with element
            username_element = self._wait_and_find_element(self.USERNAME)

            # Clear existing text (if any)
            username_element.clear()

            # Enter username
            username_element.send_keys(username)

            # Log the action
            # logger.info("Enter Username", f"Entered username: {username}")
        except TimeoutException:
            logger.error(f"Failed to find username field: {self.USERNAME}")
            raise
        except Exception as e:
            logger.error(f"Error entering username: {str(e)}")
            raise

        """
        Enters the given username into the username field.

        Args:
            username: The username to be entered.
        """
        # self.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        """
        Enters the given password into the password field.

        Args:
            password: The password to be entered.
        """
        self.find_element(self.PASSWORD).send_keys(password)

    def enter_comment(self, comment):
        """
        Clears the comment field and enters the given comment.

        Args:
            comment: The comment to be entered.
        """
        self.find_element(self.COMMENT).clear()
        self.find_element(self.COMMENT).send_keys(comment)

    def select_checkbox(self, value):
        """
        Selects the checkbox with the given value.

        Args:
            value: The value of the checkbox to be selected.
        """
        dynamic_locator = self.update_locator(self.CHECKBOX, value)
        self.find_element(dynamic_locator).click()

    def select_radiobutton(self):
        """
        Selects the specified radio button.
        """
        self.find_element(self.RADIOBUTTON).click()

    def select_multiple_select_option(self, text):
        """
        Selects the given option from the multiple select element.

        Args:
            text: The visible text of the option to be selected.
        """
        select_element = self.find_element(self.MULTIPLE_SELECT)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def select_from_dropdown(self, option):
        """
        Selects the given option from the dropdown.

        Args:
            option: The value of the option to be selected.
        """
        select_element = self.find_element(self.DROPDOWN)
        select = Select(select_element)
        select.select_by_value(option)

    def click_submit(self):
        """
        Clicks the submit button.
        """
        self.find_element(self.SUBMIT_BUTTON).click()

    def open_basic_web_page(self):
        """
        Opens the basic web page and verifies the title.
        """
        self.find_element(self.BASIC_WEB_PAGE_EXAMPLE).click()
        title = self.get_title()
        if title == 'Basic Web Page Title':
            print('Basic Web Page is opened')
        else:
            print('Basic Web Page is not opened')