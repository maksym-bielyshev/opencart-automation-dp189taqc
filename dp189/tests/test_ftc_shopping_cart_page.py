import pytest
from dp189.pages.product_page import ProductPage
from dp189.pages.shopping_cart_page import ShoppingCartPage
from dp189.tests.conftest import get_test_data
from dp189.tests.base_test import BaseTest


PRODUCT_URL = 'http://34.71.14.206/index.php?route=product/product&product_id=40'
SHOPPING_CART_URL = 'http://34.71.14.206/index.php?route=checkout/cart'


class TestShoppingCart(BaseTest):
    def setup(self):
        self.driver.maximize_window()

        self.driver.get(PRODUCT_URL)
        product = ProductPage(self.driver)
        product.available_options.click_add_to_cart_button()

        self.driver.get(SHOPPING_CART_URL)

        self.cart = ShoppingCartPage(self.driver)
        self.cart.generate_products_list()

    def test_shopping_cart_change_quantity_positive(self):
        """Positive test to check correct changing quantity of product."""
        self.cart.change_product_quantity('iPhone', '5')

        assert 'Success: You have modified your shopping cart!' in self.cart.catch_info_message.get_info_message()

    @pytest.mark.parametrize('test_input,expected', get_test_data('test_data_shopping_cart_quantity.csv'))
    def test_shopping_cart_change_quantity_negative(self, test_input: str, expected: str):
        """Negative test for checking changes in the cart when invalid data is entered.
        :param test_input: str
        :param expected: str
        """
        self.cart.change_product_quantity('iPhone', test_input)

        assert self.cart.get_text_empty_cart() == expected
