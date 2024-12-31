import pytest
from selenium import webdriver
# from selenium.webdriver.common.service import
from selenium.webdriver import ChromeService
import logging
from utils.browser_factory import BrowserFactory
import time
from utils.path_creator import PathCreator

# Create a logger for this module
logger = logging.getLogger(__name__)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope='session')
def setup_driver(request):
    # Create WebDriver instance
    logger.info("Setup Driver")
    browser = request.config.getoption("--browser")
    driver = BrowserFactory.get_driver(browser)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def browser_setup(request):
    """
    Parameterized fixture for cross-browser testing

    Args:
        request: Pytest fixture request object

    Returns:
        Configured WebDriver instance
    """
    # Get the browser name from parameters
    browser = request.param

    # Log browser information
    logger.info(f"Setting up {browser.upper()} browser")

    # Create WebDriver instance
    driver = BrowserFactory.get_driver(browser)

    # Add implicit wait and set window size
    driver.implicitly_wait(10)

    # Attach browser name to the driver for later reference
    driver.browser_name = browser

    request.cls.driver = driver

    # Provide the driver to the test
    yield

    # Cleanup - quit the driver after test
    driver.quit()
    logger.info(f"Closed {browser.upper()} browser")


@pytest.fixture()
def open_html_form_example(request, setup_driver):
    request.cls.driver = setup_driver
    request.cls.driver.get('https://testpages.eviltester.com/styled/basic-html-form-test.html')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """This fixture takes screenshot of failed test cases"""
    # Execute the test
    outcome = yield
    result = outcome.get_result()

    # Check if the test has failed
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("setup_driver")  # Access the browser fixture
        if driver:
            timestamp = time.strftime("%Y_%m_%d_%H:%M:%S")
            screenshot_filename = f"{item.name}_{timestamp}.png"
            screenshot_path = PathCreator.relative_path_creator(file_path=f'{screenshot_filename}')
            driver.save_screenshot(screenshot_path)
            logger.info(f'Screenshot of failed test case is saved as - {screenshot_filename}')

