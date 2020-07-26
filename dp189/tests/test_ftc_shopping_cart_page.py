import pytest
from dp189.pages.product_page import ProductPage
from dp189.pages.shopping_cart_page import ShoppingCartPage
from dp189.tests.conftest import get_test_data
from dp189.tests.base_test import BaseTest
from dp189.routes import *
from dp189.constants import ShoppingCartPageUpdateButtonConstants


class TestShoppingCart(BaseTest):
    def setup(self):
        self.driver.maximize_window()

        self.driver.get(get_product_url('40'))
        product = ProductPage(self.driver)
        product.available_options.click_add_to_cart_button()

        self.driver.get(CART_PAGE_URL)

        self.cart = ShoppingCartPage(self.driver)
        self.cart.generate_products_list()

    def test_shopping_cart_change_quantity_positive(self):
        """Positive test to check correct changing quantity of product.
        :param expected: str
        """
        self.cart.change_product_quantity(ShoppingCartPageUpdateButtonConstants.TEST_ITEM1, '5')

        assert ShoppingCartPageUpdateButtonConstants.RESULT in self.cart.catch_info_message.get_info_message()

    @pytest.mark.parametrize('test_input,expected', get_test_data('test_data_shopping_cart_quantity.csv'))
    def test_shopping_cart_change_quantity_negative(self, test_input: str, expected: str):
        """Negative test for checking changes in the cart when invalid data is entered.
        :param test_input: str
        :param expected: str
        """
        self.cart.change_product_quantity(ShoppingCartPageUpdateButtonConstants.TEST_ITEM1, test_input)

        assert self.cart.get_text_empty_cart() == expected

    def test_shopping_cart_click_remove_button(self):
        """Positive test to check correct changing after remove product from shopping cart."""
        self.cart.click_remove_product_button(ShoppingCartPageUpdateButtonConstants.TEST_ITEM1)

        assert ShoppingCartPageUpdateButtonConstants.RESULT3 == self.cart.get_text_empty_cart()
