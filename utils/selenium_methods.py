from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Create a logger for this module
logger = logging.getLogger(__name__)

class SeleniumMethods:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Default timeout

    def find_element(self, locator, timeout=10):
        """Waits for an element to be visible and returns it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        """Waits for elements to be visible and returns a list of them."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def hover_over_element(self, element):
        """Performs hover action on a given element."""
        self.actions.move_to_element(element).perform()

    def click_element(self, locator, timeout=10):
        """Clicks an element after ensuring it's clickable."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def get_title(self):
        """Returns the current page title."""
        return self.driver.title

    def _wait_and_find_element(self, locator, timeout=10):
        """
        Wait and find element with explicit wait

        Args:
            locator (tuple): Selenium locator strategy
            timeout (int, optional): Maximum wait time

        Returns:
            WebElement: Found element
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except Exception as e:
            logger.error(f"Element not found: {locator}")
            raise

    def get_text(self, locator):
        """Returns the text present in locator provided."""
        return self._wait_and_find_element(locator).text
