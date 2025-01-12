from selenium import webdriver
import logging
from utils.path_creator import PathCreator
from selenium.webdriver import ChromeService

# Configure logger
logger = logging.getLogger(__name__)


class BrowserFactory:
    @staticmethod
    def get_driver(browser):
        """
        Factory method to create WebDriver instances
        """
        if browser == "chrome":
            # Setup Chrome browser

            # chromedriver_path = PathCreator.relative_path_creator(file_path="chromedriver/chromedriver")
            # service = ChromeService(executable_path=chromedriver_path)
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-extensions")
            return webdriver.Chrome(options=options)

        elif browser == "firefox":
            # Setup Firefox browser
            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-extensions")
            return webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")
