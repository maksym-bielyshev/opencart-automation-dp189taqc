from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
#MacOS imports
from ..components import SearchArea, BaseNavBar, ShopCartButton
from ..locators import LocatorsShoppingCartButton, LocatorYourStoreLink, LocatorsNavBar


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.top_nav_bar = BaseNavBar(driver)
        self.my_account = driver.find_element(*LocatorsNavBar.MY_ACCOUNT)
        self.your_store_link = driver.find_element(*LocatorYourStoreLink.YOUR_STORE)
        self.search = SearchArea(driver)
        self.shop_cart_button = ShopCartButton(driver)

    def click_my_account(self):
        self.my_account.click()
    
    def click_account_and_go_to_login(self):
        self.my_account.click()
        self.my_account.find_element(*LocatorsNavBar.LOGIN).click()
    
    def click_account_and_go_to_register(self):
        self.my_account.click()
        self.my_account.find_element(*LocatorsNavBar.REGISTER).click()
