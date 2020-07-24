import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dp189.pages.product_page import ProductPage
from dp189.pages.shopping_cart_page import ShoppingCartPage
import csv

CHROME_DRIVER_PATH = 'C:/Users/Home/Downloads/chromedriver_win32/chromedriver.exe'
PRODUCT_URL = 'http://34.71.14.206/index.php?route=product/product&product_id=40'
SHOPPING_CART_URL = 'http://34.71.14.206/index.php?route=checkout/cart'


def get_test_data():
    with open('../testsData/test_data_shopping_cart_quantity.csv', 'r') as file:
        reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True, delimiter='\t')
        test_data_list = []
        for row in reader:
            test_data_list.append(tuple(row[0].strip('][').split(';')))
        return test_data_list


class TestShoppingCart:
    def setup(self):
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        self._driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)
        self._driver.maximize_window()

        self._driver.get(PRODUCT_URL)
        product = ProductPage(self._driver)
        product.available_options.click_add_to_cart_button()

        self._driver.get(SHOPPING_CART_URL)

        self.cart = ShoppingCartPage(self._driver)
        self.cart.generate_products_list()

    def test_shopping_cart_change_quantity_positive(self):
        """Positive test to check correct changing quantity of product.
        :param expected: str
        """
        self.cart.change_product_quantity('iPhone', '5')

        assert 'Success: You have modified your shopping cart!' in self.cart.catch_info_message.get_info_message()

    @pytest.mark.parametrize('test_input,expected', get_test_data())
    def test_shopping_cart_change_quantity_negative(self, test_input: str, expected: str):
        """Negative test for checking changes in the cart when invalid data is entered.
        :param test_input: str
        :param expected: str
        """
        self.cart = self.cart.change_product_quantity('iPhone', test_input)

        assert self.cart.get_text_empty_cart() == expected

    def teardown(self):
        self._driver.close()