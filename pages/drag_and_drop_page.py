from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DragAndDropPage(BasePage):
    """
    This class represents the Drag And Drop Page on Test Pages (https://testpages.eviltester.com/styled/drag-drop-javascript.html).
    It provides methods to interact with various alert elements and retrieve their content.

    Attributes:
        driver (WebDriver): The WebDriver instance used to interact with the page.
    """
    
    # Locators
    DRAGGABLE_ITEM_1 = (By.ID, 'draggable1')
    DRAGGABLE_ITEM_2 = (By.ID, 'draggable2')
    DROPPABLE_1 = (By.ID, 'droppable1')
    DROPPABLE_2 = (By.ID, 'droppable2')

    def __init__(self, driver):
        """
        Initializes the DragAndDropPage object with the given WebDriver instance.

        Args:
            driver (WebDriver): The WebDriver instance to use for interacting with the page.
        """
        super().__init__(driver)
        self.driver.get('https://testpages.eviltester.com/styled/drag-drop-javascript.html')

    def drag_and_drop_item(self) -> None:
        """
        Drag Item DRAGGABLE_ITEM_1 and drops it in DROPPABLE_1 position
        Returns:
            None
        """
        self.drag_and_drop(self.DRAGGABLE_ITEM_1, self.DROPPABLE_1)

    def get_text_from_droppable_1(self) -> str:
        """
        Returns the text present in locator provided.
        """
        return self.get_text(self.DROPPABLE_1)