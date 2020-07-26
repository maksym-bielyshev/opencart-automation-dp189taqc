from dp189.tests.base_test import BaseTest
from dp189.pages.home_page import HomePage
from dp189.pages.shopping_cart_page import ShoppingCartPage
from dp189.locators import LocatorsShoppingCartPageTest
from dp189.constants import ShoppingCartPageConstants
from dp189.routes import *

class TestShoppingCartPageContinueShoppingButton(BaseTest):
    def setup(self):
        super().setup()
        self.driver.maximize_window()
        self.driver.get(HOME_PAGE_URL)
        self.page = HomePage(self.driver)
        self.page.find_element(LocatorsShoppingCartPageTest.IPHONE).click()
        self.driver.get(CART_PAGE_URL)
        self.page = ShoppingCartPage(self.driver)

    def test_continue_shopping_button(self):
        self.page.click_checkout_button()
        assert self.page.get_title.get_title_page(ShoppingCartPageConstants.CHECKOUT_TITLE) == 'Checkout'