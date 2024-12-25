import pytest
from pages.iframes_one_page import IFrameOnePage


class TestIFramePage:

    @pytest.mark.smoke
    def test_01_iframe_page_title(self, setup_driver):
        """Verifies Title of Home page"""
        driver = setup_driver
        iframe_one_page = IFrameOnePage(driver)
        title = "Nested Frames Simple Example"
        expected_title = iframe_one_page.get_title()
        assert expected_title == title, (f'[FAILURE] Expected Title - "{expected_title}" '
                                         f'Actual - {title}')

    @pytest.mark.sanity
    def test_02_iframe_page_left_text(self, setup_driver):
        """Verifies Title of Home page"""
        driver = setup_driver
        iframe_one_page = IFrameOnePage(driver)
        left_text = "Left"
        expected_text = iframe_one_page.get_text_from_left_frame()
        assert expected_text == left_text, (f'[FAILURE] Expected Text - "{expected_text}" '
                                         f'Actual - {left_text}')
        # driver.switch_to.default_content()

    @pytest.mark.regression
    def test_03_iframe_page_left_list_text(self, setup_driver):
        """Verifies Title of Home page"""
        driver = setup_driver
        iframe_one_page = IFrameOnePage(driver)
        left_text = "Left List Item 0"
        expected_text = iframe_one_page.get_list_from_left_frame()
        assert expected_text == left_text, (f'[FAILURE] Expected Text - "{expected_text}" '
                                         f'Actual - {left_text}')

    @pytest.mark.sanity
    def test_04_iframe_page_right_text(self, setup_driver):
        """Verifies Title of Home page"""
        driver = setup_driver
        iframe_one_page = IFrameOnePage(driver)
        left_text = "Right"
        expected_text = iframe_one_page.get_text_from_right_frame()
        assert expected_text == left_text, (f'[FAILURE] Expected Text - "{expected_text}" '
                                         f'Actual - {left_text}')

    @pytest.mark.regression
    def test_05_iframe_page_right_list_text(self, setup_driver):
        """Verifies Title of Home page"""
        driver = setup_driver
        iframe_one_page = IFrameOnePage(driver)
        left_text = "Right List Item 0"
        expected_text = iframe_one_page.get_list_from_right_frame()
        assert expected_text == left_text, (f'[FAILURE] Expected Text - "{expected_text}" '
                                         f'Actual - {left_text}')