import pytest
from pages.html_page import HtmlPage
from pages.form_processor_page import FormProcessorPage
from utils.read_data import ReadData
from utils.path_creator import PathCreator
import logging

# Create a logger for this module
logger = logging.getLogger(__name__)

test_data = ReadData.load_test_data(file_path="data/html_form.json")


class TestHtmlPage:

    @pytest.mark.cross_browser
    def test_01_html_page_title(self, browser_setup: object):
        """Verifies Title of Html page"""
        driver = browser_setup
        logger.info(f"Browser: {driver.browser_name}")
        html_page = HtmlPage(driver)
        driver.get('https://testpages.eviltester.com/styled/basic-html-form-test.html')
        title = html_page.get_title()
        assert title == 'HTML Form Elements', (f'[FAILURE] Actual Title - "{title}" '
                                               f'Expected Title - "HTML Form Elements"')

    @pytest.mark.regression
    @pytest.mark.usefixtures('open_html_form_example')
    @pytest.mark.parametrize("form_data", test_data)
    def test_02_html_page(self, form_data: list):
        """Fill form in Html page, click on Submit Button, verify correct data is shown in Form processor page"""

        # Get data
        username = form_data.get('username')
        password = form_data.get('password')
        comment = form_data.get('comment')
        file_path = form_data.get('file_path')
        checkbox_value = form_data.get('checkbox_value')
        multiple_select_text = form_data.get('multiple_select_text')
        drop_down_option = form_data.get('drop_down_option')

        html_page = HtmlPage(self.driver)
        html_page.enter_username(username=username)
        html_page.enter_password(password=password)
        html_page.enter_comment(comment=comment)
        file_path = PathCreator.relative_path_creator(file_path=file_path)
        html_page.upload_file(file_path=file_path)
        html_page.select_checkbox(value=checkbox_value)
        html_page.select_radiobutton()
        html_page.select_multiple_select_option(text=multiple_select_text)
        html_page.select_from_dropdown(option=drop_down_option)
        html_page.click_submit()

        form_processor_page = FormProcessorPage(self.driver)

        actual_username = form_processor_page.get_username()
        assert actual_username == username, (f'[FAILURE] Actual Username - {actual_username}'
                                                                f'Expected Username - {username}')
        actual_password = form_processor_page.get_password()
        assert actual_password == password, (f'[FAILURE] Actual Password - {actual_password}'
                                                                f'Expected Password - {password}')
        actual_comment = form_processor_page.get_comment()
        assert actual_comment == comment, (f'[FAILURE] Actual Comment - {actual_comment}'
                                                                f'Expected Comment - {comment}')
        actual_filename = form_processor_page.get_filename()
        assert actual_filename in file_path, (f'[FAILURE] Actual Filename - {actual_filename}'
                                             f'Expected File - {file_path}')
        actual_checkbox = form_processor_page.get_checkbox()
        assert actual_checkbox == checkbox_value, (f'[FAILURE] Actual Checkbox Value - {actual_checkbox}'
                                             f'Expected Checkbox Value - {checkbox_value}')
        actual_drop_down_option = form_processor_page.get_dropdown()
        assert actual_drop_down_option == drop_down_option, (
            f'[FAILURE] Actual Drop down Option Value - {actual_drop_down_option}'
            f'Expected Drop Down Option Value - {drop_down_option}')
