from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FormProcessorPage(BasePage):

    # Locators
    USERNAME = (By.ID, '_valueusername')
    PASSWORD = (By.ID, '_valuepassword')
    COMMENT = (By.ID, '_valuecomments')
    FILE_NAME = (By.ID,  '_valuefilename')
    CHECKBOX = (By.ID, '_valuecheckboxes0')
    RADIOBUTTON = (By.ID, '_valueradioval')
    MULTIPLE_SELECT = (By.ID, '_valuemultipleselect0')
    DROPDOWN = (By.ID, '_valuedropdown')

    def __init__(self, driver):
        super().__init__(driver)

    def get_username(self):
        return self.get_text(self.USERNAME)

    def get_password(self):
        return self.get_text(self.PASSWORD)

    def get_comment(self):
        return self.get_text(self.COMMENT)

    def get_filename(self):
        return self.get_text(self.FILE_NAME)

    def get_checkbox(self):
        return self.get_text(self.CHECKBOX)

    def get_radiobutton(self):
        return self.get_text(self.RADIOBUTTON)

    def get_multi_select(self):
        return self.get_text(self.MULTIPLE_SELECT)

    def get_dropdown(self):
        return self.get_text(self.DROPDOWN)
