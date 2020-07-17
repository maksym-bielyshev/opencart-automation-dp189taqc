from selenium.webdriver import Remote
from dp189.locators import LocatorsWishListPage
from dp189.pages.base_page import BasePage
from dp189.components import BaseRightMenu


class WishListPage(BasePage):
    """Wish list page class"""

    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self.basepage = BaseRightMenu(driver)

    def get_list_items(self):
        """Method which print items on wishlist page"""
        list_items = []
        for item in self._driver.find_elements(*LocatorsWishListPage.ITEMS):
            list_items.append(item.text)
        return list_items

    def click_add_to_cart(self, item_name: str):
        """Method which add appointed item to card"""
        for item in self._driver.find_elements(*LocatorsWishListPage.PRODUCT_NAME):
            print(item.text)
            if item.text == item_name:
                item.find_element(*LocatorsWishListPage.ADD_PRODUCT_TO_CARD).click()

    def click_remove_from_wishlist(self, item_name: str):
        """Method which remove appointed item from wishlist"""
        for item in self._driver.find_elements(*LocatorsWishListPage.PRODUCT_NAME):
            if item.text == item_name:
                item.find_element(*LocatorsWishListPage.DELETE_PRODUCT_FROM_CARD).click()
                return WishListPage(self._driver)

    def click_button_continue(self):
        """method which return Account page class"""
        self._driver.find_element(*LocatorsWishListPage.CONTINUE_BUTTON).click()
