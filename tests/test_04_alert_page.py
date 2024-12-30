import pytest
from pages.alert_page import AlertPage
import logging

# Create a logger for this module
logger = logging.getLogger(__name__)


class TestAlertPage():

    @pytest.mark.smoke
    def test_01_alert_page_title(self, setup_driver):
        """Verifies Title of alert page"""
        self.driver = setup_driver
        logger.info('Testing')
        alert_page = AlertPage(self.driver)
        title = 'Test Page For JavaScript Alerts'
        expected_title = alert_page.get_title()
        assert expected_title == title, (f'[FAILURE] Expected Title - "{expected_title}" '
                                         f'Actual - {title}')

    @pytest.mark.sanity
    def test_02_basic_alert_example(self, setup_driver):
        """Tests Basic Alert example"""
        self.driver = setup_driver
        alert_page = AlertPage(self.driver)
        alert_page.click_show_alert_box()
        text = alert_page.show_alert_text()
        expected_text = 'I am an alert box!'
        assert text == expected_text, (f'[FAILURE] Expected Text - {expected_text}'
                                       f'\nActual Text - {text}')

        alert_page.accept_alert_popup()
        alert_explanation_text = alert_page.show_alert_explanation_text()
        expected_text = 'You triggered and handled the alert dialog'
        assert expected_text == alert_explanation_text, (f'[FAILURE] Expected Text - {expected_text}'
                                       f'\nActual Text - {alert_explanation_text}')

    @pytest.mark.sanity
    @pytest.mark.parametrize("data", [('OK', 'true'), ('Cancel', 'false')])
    def test_03_confirm_alert_example(self, setup_driver, data):
        """Tests Confirm Alert example"""
        self.driver = setup_driver
        alert_page = AlertPage(self.driver)
        alert_page.click_confirm_alert_box()
        text = alert_page.show_alert_text()
        expected_text = 'I am a confirm alert'
        assert text == expected_text, (f'[FAILURE] Expected Text - {expected_text}'
                                       f'Actual Text - {text}')
        if data[0] == 'OK':
            alert_page.accept_alert_popup()
        elif data[0] == 'Cancel':
            alert_page.dismiss_alert_popup()
        alert_explanation_text = alert_page.show_confirm_explanation_text()
        expected_text = f'You clicked {data[0]}, confirm returned {data[1]}.'
        assert expected_text == alert_explanation_text, (f'[FAILURE] Expected Text - {expected_text}'
                                       f'\nActual Text - {alert_explanation_text}')

    @pytest.mark.regression
    @pytest.mark.parametrize("data", [('OK', 'New Message'), ('Cancel', 'null')])
    def test_03_confirm_alert_example(self, setup_driver, data):
        """Tests Confirm Alert example"""
        self.driver = setup_driver
        alert_page = AlertPage(self.driver)
        alert_page.click_show_prompt_box()
        text = alert_page.show_alert_text()
        expected_text = 'I prompt you'
        assert text == expected_text, (f'[FAILURE] Expected Text - {expected_text}'
                                       f'Actual Text - {text}')
        if data[0] == 'OK':
            alert_page.send_prompt_in_alert(data[1])
            alert_page.accept_alert_popup()
        elif data[0] == 'Cancel':
            alert_page.dismiss_alert_popup()
        alert_explanation_text = alert_page.show_prompt_text()
        expected_text = f"You clicked {data[0]}. 'prompt' returned {data[1]}"
        assert expected_text == alert_explanation_text, (f'[FAILURE] Expected Text - {expected_text}'
                                       f'\nActual Text - {alert_explanation_text}')
