from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from ..components import BasePageNavBarComponent, DropdownComponent, InputFieldComponent, ShopCartButtonComponent
from ..locators import LocatorsBasePageMainMenu, LocatorsBasePageNavBar, LocatorYourStoreLink, LocatorBasePageSearch
from ..locators import LocatorsBasePageNavBar

from dp189.components import SearchArea, BaseNavBar, ShopCartButton, CatchMessageComponent
from dp189.locators import LocatorsShoppingCartButton, LocatorYourStoreLink, LocatorsNavBar


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.top_nav_bar = BasePageNavBarComponent(driver)
        self.main_menu_desktops = DropdownComponent(driver, LocatorsBasePageMainMenu.DESKTOPS)
        self.main_menu_laptops_notebooks = DropdownComponent(driver, LocatorsBasePageMainMenu.LAPTOPS_NOTEBOOKS)
        self.main_menu_components = DropdownComponent(driver, LocatorsBasePageMainMenu.COMPONENTS)
        self.main_menu_tablets = DropdownComponent(driver, LocatorsBasePageMainMenu.TABLETS)
        self.main_menu_software = DropdownComponent(driver, LocatorsBasePageMainMenu.SOFTWARE)
        self.main_menu_phones_pdas = DropdownComponent(driver, LocatorsBasePageMainMenu.PHONES_PDAS)
        self.main_menu_cameras = DropdownComponent(driver, LocatorsBasePageMainMenu.CAMERAS)
        self.main_menu_mp3players = DropdownComponent(driver, LocatorsBasePageMainMenu.MP3_PLAYERS)
        self.my_account = driver.find_element(*LocatorsBasePageNavBar.MY_ACCOUNT)
        self.your_store_link = driver.find_element(*LocatorYourStoreLink.YOUR_STORE)
        self.search_field = InputFieldComponent(driver, LocatorBasePageSearch.SEARCH_FIELD)
        self.shop_cart_button = ShopCartButtonComponent(driver)
        self.catch_info_message = CatchMessageComponent(self._driver)

    def click_account_and_go_to_login(self):
        self.my_account.click()
        self.my_account.find_element(*LocatorsBasePageNavBar.LOGIN).click()
    
    def click_account_and_go_to_register(self):
        self.my_account.click()
        self.my_account.find_element(*LocatorsBasePageNavBar.REGISTER).click()
