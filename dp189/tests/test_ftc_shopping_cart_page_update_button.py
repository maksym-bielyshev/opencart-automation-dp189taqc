from dp189.tests.base_test import BaseTest
from dp189.routes import *
from dp189.pages.home_page import HomePage
from dp189.pages.shopping_cart_page import ShoppingCartPage
from dp189.locators import LocatorsShoppingCartPageTest
from dp189.constants import ShoppingCartPageConstants


class TestShoppingCartPageUpdateButton(BaseTest):
    def setup(self):
        super().setup()
        self.driver.maximize_window()
        self.driver.get(HOME_PAGE_URL)
        self.page = HomePage(self.driver)
        self.page.find_element(LocatorsShoppingCartPageTest.IPHONE).click()
        self.driver.get(CART_PAGE_URL)
        self.page = ShoppingCartPage(self.driver)
        self.page.generate_products_list()
        self.page = self.page.change_product_quantity(ShoppingCartPageConstants.TEST_ITEM1, "2")
        self.page.generate_products_list()

    def test_catch_info_message(self):
        assert ShoppingCartPageConstants.RESULT in self.page.catch_info_message.get_info_message()

    def test_total_price_of_product(self):
        total_price = self.page.get_product_total_price(ShoppingCartPageConstants.TEST_ITEM1)
        print(total_price)
        assert ShoppingCartPageConstants.RESULT2 == total_price
