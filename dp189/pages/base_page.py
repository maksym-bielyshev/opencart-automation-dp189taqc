from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from dp189.components import SearchArea, BaseNavBar, ShopCartButton, CatchMessageComponent
from dp189.locators import LocatorsShoppingCartButton, LocatorYourStoreLink, LocatorsNavBar


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._top_nav_bar = BaseNavBar(driver)
        self._my_account = driver.find_element(*LocatorsNavBar.MY_ACCOUNT)
        self._your_store_link = driver.find_element(*LocatorYourStoreLink.YOUR_STORE)
        self._search = SearchArea(driver)
        self._shop_cart_button = ShopCartButton(self._driver)
        self.catch_info_message = CatchMessageComponent(self._driver)
    
    def click_currency_euro(self):
        self._top_nav_bar.click_currency_euro()

    def click_currency_pound(self):
        self._top_nav_bar.click_currency_pound()

    def click_currency_usd(self):
        self._top_nav_bar.click_currency_usd()

    def click_contact_us(self):
        self._top_nav_bar.click_contact_us()
        #return ContactUsPage(self._driver)

    def click_wishlist(self):
        self._top_nav_bar.click_wishlist()
        #return WishListPage(self._driver)

    def click_shopping_cart(self):
        self._top_nav_bar.click_shopping_cart()
        #return ShoppingCartPage(self._driver)
    
    def click_my_account(self):
        self._my_account.click()
    
    def click_account_and_go_to_login(self):
        self._my_account.click()
        self._my_account.find_element(*LocatorsNavBar.LOGIN).click()
        #return LoginPage(self._driver)
    
    def click_account_and_go_to_register(self):
        self._my_account.click()
        self._my_account.find_element(*LocatorsNavBar.REGISTER).click()
        #return RegisterPage(self._driver)

