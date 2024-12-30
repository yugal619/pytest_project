from utils.selenium_methods import SeleniumMethods


# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(SeleniumMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.timeout = 30
