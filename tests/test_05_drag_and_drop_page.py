import pytest
from pages.drag_and_drop_page import DragAndDropPage
import logging

# Create a logger for this module
logger = logging.getLogger(__name__)


class TestDragAndDropPage():

    @pytest.mark.smoke
    def test_01_alert_page_title(self, setup_driver):
        """Verifies Title of alert page"""
        self.driver = setup_driver
        logger.info('Testing')
        drag_and_drop_page = DragAndDropPage(self.driver)
        title = 'GUI User Interactions'
        expected_title = drag_and_drop_page.get_title()
        assert expected_title == title, (f'[FAILURE] Expected Title - "{expected_title}" '
                                         f'Actual - {title}')
        drag_and_drop_page.drag_and_drop_item()
        dropped_text_filed = drag_and_drop_page.get_text_from_droppable_1()
        expected_text = f'Dropped!'
        assert expected_text == dropped_text_filed, (f'[FAILURE] Expected Text - {expected_text}'
                                       f'\nActual Text - {dropped_text_filed}')


