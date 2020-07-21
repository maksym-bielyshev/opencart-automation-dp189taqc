import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dp189.pages.checkout_page import CheckoutOptions
from dp189.components import ProductWidgetComponent
options = Options()
options.add_argument('--ignore-certificate-errors')
import time


class TestCheckoutPage():
    def setup(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get('https://34.71.14.206/index.php')
        ProductWidgetComponent(self.driver, 'iPhone').click_add_to_shopping_cart_button()
        self.driver.get('https://34.71.14.206/index.php?route=checkout/checkout')
        self.checkout_page = CheckoutOptions(self.driver)
        time.sleep(3)

    def test_guest_checkout_with_valid_data(self):
        time.sleep(2)
        self.checkout_page.email_field_returning_customer.clear_and_fill_input_field('a')
        time.sleep(2)
        self.checkout_page.click_guest_checkout_radio_button()

    def teardown(self):
        self.driver.close()
