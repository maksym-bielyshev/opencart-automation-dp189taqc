from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement

from dp189.components import InputFieldComponent, ShopCartButtonComponent
from dp189.components import CatchMessageComponent, CatchPageTitleComponent, MainMenuComponent
from dp189.locators import LocatorBasePageSearch
from dp189.locators import LocatorsBasePageNavBar


class BasePage:
    """Base page class."""

    def __init__(self, driver: Remote):
        """Initialize main class.

        :param driver: Remote.
        """
        self._driver = driver
        self.main_menu = MainMenuComponent(self._driver)
        self.search_field = InputFieldComponent(self._driver, LocatorBasePageSearch.SEARCH_FIELD)
        self.shop_cart_button = ShopCartButtonComponent(self._driver)
        self.catch_info_message = CatchMessageComponent(self._driver)
        self.get_title = CatchPageTitleComponent(self._driver)

    def get_my_account(self) -> WebElement:
        """Method get 'My account' WebElement.

        :return: WebElement
        """
        return self._driver.find_element(*LocatorsBasePageNavBar.MY_ACCOUNT)

    def click_account_and_go_to_login(self):
        """Method which click on link and go to Login page.

        :return: None
        """
        my_account = self.get_my_account()
        my_account.click()
        my_account.find_element(*LocatorsBasePageNavBar.LOGIN).click()

    def click_account_and_go_to_register(self):
        """Method which click on link and go to Register page.

        :return: None
        """
        my_account = self.get_my_account()
        my_account.click()
        my_account.find_element(*LocatorsBasePageNavBar.REGISTER).click()

    def find_element(self, locator: tuple):
        """Method which find element on page.


        :param: Tuple[str, str]
        :return: WebElement
        """
        self._driver.implicitly_wait(8)
        return self._driver.find_element(*locator)



