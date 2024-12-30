from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AlertPage(BasePage):
    """
    This class represents the Alert Page on Test Pages (https://testpages.eviltester.com/styled/alerts/alert-test.html).
    It provides methods to interact with various alert elements and retrieve their content.

    Attributes:
        driver (WebDriver): The WebDriver instance used to interact with the page.
    """
    
    # Locators
    SHOW_ALERT_BOX = (By.ID, 'alertexamples') 
    ALERT_EXPLANATION = (By.ID, 'alertexplanation')
    CONFIRM_ALERT_BOX = (By.ID, 'confirmexample')
    CONFIRM_EXPLANATION = (By.ID, 'confirmexplanation')
    SHOW_PROMPT_BOX = (By.ID, 'promptexample')
    PROMPT_TEXT = (By.ID, 'promptexplanation')

    def __init__(self, driver):
        """
        Initializes the AlertPage object with the given WebDriver instance.

        Args:
            driver (WebDriver): The WebDriver instance to use for interacting with the page.
        """
        super().__init__(driver)
        self.driver.get('https://testpages.eviltester.com/styled/alerts/alert-test.html')

    def click_show_alert_box(self):
        """
        Clicks the 'Show Alert' button to trigger a simple alert.

        Returns:
            None
        """
        self.click_element(self.SHOW_ALERT_BOX)

    def click_show_prompt_box(self):
        """
        Clicks the 'Show Prompt' button to trigger a prompt alert.

        Returns:
            None
        """
        self.click_element(self.SHOW_PROMPT_BOX)

    def click_confirm_alert_box(self):
        """
        Clicks the 'Confirm Alert' button to trigger a confirmation alert.

        Returns:
            None
        """
        self.click_element(self.CONFIRM_ALERT_BOX)

    def show_alert_text(self):
        """
        Gets the text displayed in the simple alert.

        Returns:
            str: The text content of the simple alert.
        """
        alert = self.driver.switch_to.alert
        return alert.text

    def send_prompt_in_alert(self, message='New Message'):
        """
        Sends the specified message to the prompt alert.

        Args:
            message (str, optional): The message to enter in the prompt alert. Defaults to 'New Message'.

        Returns:
            None
        """
        alert = self.driver.switch_to.alert
        alert.send_keys(message)

    def accept_alert_popup(self):
        """
        Accepts the currently displayed alert (simple or confirm).

        Returns:
            None
        """
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert_popup(self):
        """
        Dismisses the currently displayed confirm alert.

        Returns:
            None
        """
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def show_alert_explanation_text(self):
        """
        Gets the text displayed below the simple alert.

        Returns:
            str: The explanation text below the simple alert.
        """
        return self.get_text(self.ALERT_EXPLANATION)

    def show_confirm_explanation_text(self):
        """
        Gets the text displayed below the confirm alert.

        Returns:
            str: The explanation text below the confirm alert.
        """
        return self.get_text(self.CONFIRM_EXPLANATION)

    def show_prompt_text(self):
        """
        Gets the text displayed below the prompt alert.

        Returns:
            str: The explanation text below the prompt alert.
        """
        return self.get_text(self.PROMPT_TEXT)