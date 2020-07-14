import time
from selenium.webdriver import Chrome, ChromeOptions, Remote
from dp189.locators import LocatorsWishListPage
from dp189.pages.base_page import BasePage


class WishListPage(BasePage):
    """Wish list page class"""

    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self.basepage = BasePage(driver)

    def get_list_items(self):
        """Method which print items on wishlist page"""
        for item in self._driver.find_elements_by_xpath("//td[@class='text-left']//a"):
            print(item.text)

    def add_to_cart_button(self, item_name):
        """Method which add appointed item to card"""
        for item in self._driver.find_elements(*LocatorsWishListPage.PRODUCT_NAME):
            print(item.text)
            if item.text == item_name:
                item.find_element(*LocatorsWishListPage.ADD_PRODUCT_TO_CARD).click()
        self._driver.implicitly_wait(3)
        if self._driver.find_elements_by_xpath("//div[@class='alert alert-success alert-dismissible']"):
            print("Item successfully added to shopping cart")
        else:
            ProductPage()
            print('Go to product page')

    def remove_from_wishlist_button(self, item_name):
        """Method which remove appointed item from wishlist"""
        for item in self._driver.find_elements(*LocatorsWishListPage.PRODUCT_NAME):
            if item.text == item_name:
                item.find_element(*LocatorsWishListPage.DELETE_PRODUCT_FROM_CARD).click()
                return WishListPage(self._driver)

    def click_button_continue(self):
        """method which return Account page class"""
        self._driver.find_element(*LocatorsWishListPage.CONTINUE_BUTTON).click()


class ProductPage:
    pass


