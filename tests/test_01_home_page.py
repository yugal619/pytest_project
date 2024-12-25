import pytest
from pages.home_page import HomePage
import logging

# Create a logger for this module
logger = logging.getLogger(__name__)


class TestHomePage():

    @pytest.mark.smoke
    def test_01_home_page_title(self, setup_driver):
        """Verifies Title of Home page"""
        self.driver = setup_driver
        logger.info('Testing')
        home_page = HomePage(self.driver)
        title = 'Web Testing and Automation Practice Application Pages'
        expected_title = home_page.get_title()
        assert expected_title == title, (f'[FAILURE] Expected Title - "{expected_title}" '
                                         f'Actual - {title}')

    @pytest.mark.sanity
    def test_02_basic_web_page_example(self, setup_driver):
        """Tests Basic Web page example"""
        self.driver = setup_driver
        home_page = HomePage(self.driver)
        home_page.open_basic_web_page()
        title = 'Basic Web Page Title'
        expected_title = home_page.get_title()
        assert expected_title == title, (f'[FAILURE] Expected Title - "{expected_title}" '
                                         f'Actual Title- {title}')