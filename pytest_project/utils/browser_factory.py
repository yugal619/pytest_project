from selenium import webdriver
import logging

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
