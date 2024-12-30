from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FormProcessorPage(BasePage):
    """
    This class represents the Form Processor Page on Test Pages.
    It provides methods to interact with various form elements and retrieve their values.

    Attributes:
        driver (WebDriver): The WebDriver instance used to interact with the page.
    """

    # Locators
    USERNAME = (By.ID, '_valueusername')
    PASSWORD = (By.ID, '_valuepassword')
    COMMENT = (By.ID, '_valuecomments')
    FILE_NAME = (By.ID, '_valuefilename')
    CHECKBOX = (By.ID, '_valuecheckboxes0')
    RADIOBUTTON = (By.ID, '_valueradioval')
    MULTIPLE_SELECT = (By.ID, '_valuemultipleselect0')
    DROPDOWN = (By.ID, '_valuedropdown')

    def __init__(self, driver):
        """
        Initializes the FormProcessorPage object with the given WebDriver instance.

        Args:
            driver (WebDriver): The WebDriver instance to use for interacting with the page.
        """
        super().__init__(driver)

    def get_username(self):
        """
        Gets the text displayed in the username field.

        Returns:
            str: The text content of the username field.
        """
        return self.get_text(self.USERNAME)

    def get_password(self):
        """
        Gets the text displayed in the password field (not recommended for security reasons).

        Returns:
            str: The text content of the password field.
        """
        return self.get_text(self.PASSWORD)

    def get_comment(self):
        """
        Gets the text displayed in the comment field.

        Returns:
            str: The text content of the comment field.
        """
        return self.get_text(self.COMMENT)

    def get_filename(self):
        """
        Gets the text displayed in the filename field.

        Returns:
            str: The text content of the filename field.
        """
        return self.get_text(self.FILE_NAME)

    def get_checkbox(self):
        """
        Gets the text displayed next to the checkbox element (may not be the actual checkbox state).

        Returns:
            str: The text content near the checkbox element.
        """
        return self.get_text(self.CHECKBOX)

    def get_radiobutton(self):
        """
        Gets the text displayed next to the radio button element (may not be the actual radio button state).

        Returns:
            str: The text content near the radio button element.
        """
        return self.get_text(self.RADIOBUTTON)

    def get_multi_select(self):
        """
        Gets the text displayed in the multi-select element (may not reflect all selected options).

        Returns:
            str: The text content of the multi-select element.
        """
        return self.get_text(self.MULTIPLE_SELECT)

    def get_dropdown(self):
        """
        Gets the text displayed in the currently selected dropdown option.

        Returns:
            str: The text content of the selected dropdown option.
        """
        return self.get_text(self.DROPDOWN)