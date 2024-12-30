from typing import Any, List, Optional, Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotVisibleException,
    ElementNotInteractableException,
    WebDriverException
)
import logging
import functools
import time

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def retry_on_exception(retries: int = 3, delay: float = 1):
    """
    Decorator to retry operations on specific exceptions.

    Args:
        retries (int): Number of retry attempts
        delay (float): Delay between retries in seconds
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (StaleElementReferenceException, ElementClickInterceptedException) as e:
                    last_exception = e
                    if attempt == retries - 1:
                        logger.error(f"Max retries ({retries}) reached for {func.__name__}")
                        raise
                    logger.warning(f"Retry attempt {attempt + 1} for {func.__name__}")
                    time.sleep(delay)
            raise last_exception

        return wrapper

    return decorator


class SeleniumMethods:
    """
    Utility class providing enhanced Selenium operations with retry mechanisms
    and comprehensive error handling.
    """
    default_timeout = 10

    def __init__(self, driver):
        """
        Initialize SeleniumMethods with WebDriver instance.

        Args:
            driver: WebDriver instance
            default_timeout (int): Default timeout for wait operations in seconds
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, self.default_timeout)
        self.actions = ActionChains(driver)

    @retry_on_exception()
    def find_element(self, locator: Tuple[By, str], timeout: Optional[int] = None) -> WebElement:
        """
        Waits for an element to be visible and returns it.

        Args:
            locator: Tuple of By strategy and locator string
            timeout: Wait timeout in seconds (uses default_timeout if None)

        Returns:
            WebElement: Found element

        Raises:
            TimeoutException: If element is not found within timeout
            WebDriverException: For other WebDriver related errors
        """
        try:
            timeout = timeout or self.default_timeout
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException as e:
            logger.error(f"Element not found: {locator}. Exception: {e}")
            raise
        except WebDriverException as e:
            logger.error(f"WebDriver error finding element {locator}: {str(e)}")
            raise

    @retry_on_exception()
    def find_elements(self, locator: Tuple[By, str], timeout: Optional[int] = None) -> List[WebElement]:
        """
        Waits for elements to be visible and returns them.

        Args:
            locator: Tuple of By strategy and locator string
            timeout: Wait timeout in seconds

        Returns:
            List[WebElement]: List of found elements

        Raises:
            TimeoutException: If no elements are found within timeout
        """
        try:
            timeout = timeout or self.default_timeout
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return elements
        except TimeoutException as e:
            logger.error(f"No elements found: {locator}. Exception: {e}")
            raise

    @retry_on_exception()
    def hover_over_element(self, element: WebElement) -> None:
        """
        Performs hover action on a given element.

        Args:
            element: WebElement to hover over

        Raises:
            ElementNotInteractableException: If element cannot be interacted with
        """
        try:
            self.actions.move_to_element(element).perform()
        except ElementNotInteractableException as e:
            logger.error(f"Could not hover over element: {str(e)}. Exception: {e}")
            raise

    @retry_on_exception()
    def click_element(self, locator: Tuple[By, str], timeout: Optional[int] = None) -> None:
        """
        Clicks an element after ensuring it's clickable.

        Args:
            locator: Tuple of By strategy and locator string
            timeout: Wait timeout in seconds

        Raises:
            ElementClickInterceptedException: If element click is intercepted
            TimeoutException: If element is not clickable within timeout
        """
        try:
            timeout = timeout or self.default_timeout
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            # Scroll element into view before clicking
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)  # Small delay after scroll
            element.click()
        except ElementClickInterceptedException:
            # Fallback to JavaScript click
            logger.warning(f"Click intercepted for {locator}, trying JavaScript click")
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            logger.error(f"Click failed on {locator}: {str(e)}. Exception: {e}")
            raise

    def get_title(self) -> str:
        """
        Returns the current page title.

        Returns:
            str: Current page title
        """
        try:
            return self.driver.title
        except WebDriverException as e:
            logger.error(f"Failed to get page title: {str(e)}")
            raise

    @retry_on_exception()
    def get_text(self, locator: Tuple[By, str]) -> str:
        """
        Returns the text present in locator provided.

        Args:
            locator: Tuple of By strategy and locator string

        Returns:
            str: Text content of the element

        Raises:
            TimeoutException: If element is not found
        """
        try:
            element = self.find_element(locator)
            return element.text.strip()
        except Exception as e:
            logger.error(f"Failed to get text from {locator}: {str(e)}. Exception: {e}")
            raise

    def wait_for_page_load(self, timeout: Optional[int] = None) -> None:
        """
        Waits for page load to complete.

        Args:
            timeout: Wait timeout in seconds

        Raises:
            TimeoutException: If page does not load within timeout
        """
        try:
            timeout = timeout or self.default_timeout
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
        except TimeoutException as e:
            logger.error(f"Page load timeout. Exception: {e}")
            raise

    @retry_on_exception()
    def drag_and_drop(
            self,
            source_locator: Tuple[By, str],
            target_locator: Tuple[By, str]
    ) -> None:
        """
        Performs drag and drop operation from source element to target element.

        Args:
            source_locator: Tuple of By strategy and locator string for source element
            target_locator: Tuple of By strategy and locator string for target element

        Raises:
            TimeoutException: If elements are not found
            WebDriverException: If drag and drop operation fails
        """
        try:
            source = self.find_element(source_locator)
            target = self.find_element(target_locator)

            # Scroll source into view
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", source)
            time.sleep(0.5)  # Small delay after scroll

            self.actions.drag_and_drop(source, target).perform()
            logger.info(f"Drag and drop performed from {source_locator} to {target_locator}")

        except Exception as e:
            logger.error(
                f"Drag and drop failed from {source_locator} to {target_locator}: {str(e)}. "
                f"Exception: {e}"
            )
