from selenium.webdriver import Remote
from dp189.locators import LocatorsWishListPage
from dp189.pages.base_page import BasePage
from dp189.components import RegisterPageRightMenuComponent


class WishListPage(BasePage):
    """Wish list page class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize objects to work with this page.

        :param driver: Remote
        :return: None
        """
        super().__init__(driver)
        self.basepage = RegisterPageRightMenuComponent(driver)

    def get_list_items(self) -> list:
        """Print items on Wish List page.

        :return: list
        """
        list_items = []
        for item in self._driver.find_elements(*LocatorsWishListPage.ITEMS):
            list_items.append(item.text)
        return list_items

    def click_add_to_cart(self, item_name: str) -> None:
        """Add appointed item to card.

        :param item_name: str
        :return: None
        """
        for item in self._driver.find_elements(*LocatorsWishListPage.PRODUCT_NAME):
            if item.text == item_name:
                item.find_element(*LocatorsWishListPage.ADD_PRODUCT_TO_CARD).click()

    def click_remove_from_wishlist(self, item_name: str) -> object:
        """Remove appointed item from wishlist.

        :param item_name: str
        :return: object
        """
        for item in self._driver.find_elements(*LocatorsWishListPage.PRODUCT_NAME):
            if item.text == item_name:
                item.find_element(*LocatorsWishListPage.DELETE_PRODUCT_FROM_CARD).click()
                return WishListPage(self._driver)

    def click_button_continue(self) -> None:
        """Return Account page class.

        :return: None
        """
        self._driver.find_element(*LocatorsWishListPage.CONTINUE_BUTTON).click()
