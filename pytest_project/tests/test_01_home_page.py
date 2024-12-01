import pytest
from pages.home_page import HomePage
import logging

from utils.path_creator import PathCreator

# Create a logger for this module
logger = logging.getLogger(__name__)


@pytest.mark.usefixtures('open_home_page')
class TestHomePage:

    @pytest.mark.smoke
    def test_01_home_page_title(self):
        """Verifies Title of Home page"""
        logger.info('Testing')
        home_page = HomePage(self.driver)
        title = 'Web Testing and Automation Practice Application Paes'
        expected_title = home_page.get_title()
        assert expected_title == title, (f'[FAILURE] Expected Title - "{expected_title}" '
                                         f'Actual - {title}')

    @pytest.mark.smoke
    def test_02_basic_web_page_example(self):
        """Tests Basic Web page example"""
        home_page = HomePage(self.driver)
        home_page.open_basic_web_page()
        title = 'Basic Web Page Title'
        expected_title = home_page.get_title()
        assert expected_title == title, (f'[FAILURE] Expected Title - "{expected_title}" '
                                         f'Actual Title- {title}')

