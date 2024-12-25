from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class AlertPage(BasePage):

    # Locators
    SHOW_ALERT_BOX = (By.ID, 'alertexamples')
    ALERT_EXPLANATION = (By.ID, 'alertexplanation')
    CONFIRM_ALERT_BOX = (By.ID, 'confirmexample')
    CONFIRM_EXPLANATION = (By.ID, 'confirmexplanation')

    LIST = (By.XPATH, '//li')

    def __init__(self, driver):
        """
        Initializes the Page Object with the given WebDriver instance.

        Args:
            driver: The WebDriver instance to be used.
        """
        super().__init__(driver)
        driver.get('https://testpages.eviltester.com/styled/alerts/alert-test.html')

    def click_show_alert_box(self):
        """
        Initializes the Page Object with the given WebDriver instance.

        Args:
            driver:
        """
        self.click_element(self.SHOW_ALERT_BOX)

    def click_confirm_alert_box(self):
        """
        Initializes the Page Object with the given WebDriver instance.

        Args:
            driver:
        """
        self.click_element(self.CONFIRM_ALERT_BOX)

    def show_alert_text(self):
        """

        Returns:

        """
        alert = self.driver.switch_to.alert
        return alert.text

    def accept_alert_popup(self):
        """

        Returns:

        """
        alert = self.driver.switch_to.alert
        alert.accept()

    def accept_alert_popup(self):
        """

        Returns:

        """
        alert = self.driver.switch_to.alert
        alert.accept()

    def show_alert_explanation_text(self):
        """

        Returns:

        """
        return self.get_text(self.ALERT_EXPLANATION)

    def show_confirm_explanation_text(self):
        """

        Returns:

        """
        return self.get_text(self.CONFIRM_EXPLANATION)



