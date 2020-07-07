from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from components import SearchArea, NavBarNotLoggedIn, NavBarLoggedIn, RightMenuNotLoggedIn, RightMenuLoggedIn, ShopCartButton
from locators import LocatorsShoppingCartButton, LocatorYourStoreLink


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.your_store_link = driver.find_element_by(*LocatorYourStoreLink.YOUR_STORE)
        self._search = SearchArea(driver)
        self._shop_cart_button = ShopCartButton(self._driver)


class BasePageNotLoggedIn(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.nav_bar = NavBarNotLoggedIn(driver)
        self._right_menu = RightMenuNotLoggedIn(driver)


class BasePageLoggedIn(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.nav_bar = NavBarLoggedIn(driver)
        self._right_menu = RightMenuLoggedIn(driver)
