from dp189.pages.base_page import BasePage
from selenium.webdriver import Remote
from dp189.locators import LocatorsComparePage


class ComparePage(BasePage):
    """Compare page class."""

    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)

    def get_list_items(self) -> list:
        """Method which returns list of items on compare page.

        :return: list
        """
        list_items = []
        for item in self._driver.find_elements(*LocatorsComparePage.ITEMS):
            list_items.append(item.text)
        return list_items

    def click_add_to_card_button(self, product: str) -> None:
        """Method which add appointed item to the cart.

        :return: None
        """
        add_button_items = []
        item_index = self.get_list_items().index(product)
        print(item_index)
        for add_button in self._driver.find_elements(*LocatorsComparePage.ADD_BUTTONS):
            add_button_items.append(add_button)
        add_button_items[item_index].click()

    def click_remove_button(self, product: str) -> object:
        """Method which remove appointed item on compare page.

        :return: object
        """
        remove_button_items = []
        item_index = self.get_list_items().index(product)
        for remove_button in self._driver.find_elements(*LocatorsComparePage.REMOVE_BUTTONS):
            remove_button_items.append(remove_button)
        if remove_button_items[item_index]: remove_button_items[item_index].click()
        return ComparePage(self._driver)
