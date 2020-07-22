"""Module for the testing 'Checkout' page."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dp189.pages.checkout_page import CheckoutPage
from dp189.components import ProductWidgetComponent
options = Options()
options.add_argument('--ignore-certificate-errors')
import time


class TestCheckoutPage():
    """Class for the 'Checkout' page."""

    def setup(self) -> None:
        """Setup for the test.

        :return: None
        """
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://34.71.14.206/index.php')
        ProductWidgetComponent(self.driver, 'iPhone').click_add_to_shopping_cart_button()
        self.driver.get('https://34.71.14.206/index.php?route=checkout/checkout')

    def test_guest_checkout_with_valid_data(self) -> None:
        """Test the 'Checkout' page with valid data.

        :return: None.
        """
        checkout_page = CheckoutPage(self.driver)

        checkout_page.open_checkout_options.click_guest_checkout_radio_button()
        checkout_page.open_checkout_options.click_continue_button()

        checkout_page.open_billing_details.load_your_address_form()
        checkout_page.open_billing_details.your_address_form.first_name_field.clear_and_fill_input_field("Maksym")
        checkout_page.open_billing_details.your_address_form.last_name_field.clear_and_fill_input_field("Bielyshev")
        checkout_page.open_billing_details.your_address_form.email_field_payment.clear_and_fill_input_field("email@email.com")
        checkout_page.open_billing_details.your_address_form.telephone_field.clear_and_fill_input_field("12345")
        checkout_page.open_billing_details.your_address_form.company_field.clear_and_fill_input_field("test")
        checkout_page.open_billing_details.your_address_form.address_1_field.clear_and_fill_input_field("test")
        checkout_page.open_billing_details.your_address_form.address_2_field.clear_and_fill_input_field("test")
        checkout_page.open_billing_details.your_address_form.city_field.clear_and_fill_input_field("test")
        checkout_page.open_billing_details.your_address_form.post_code_field.clear_and_fill_input_field("test")
        checkout_page.open_billing_details.your_address_form.country.choose_dropdown_option("Ukraine")
        checkout_page.open_billing_details.your_address_form.region.choose_dropdown_option("Kyiv")
        checkout_page.open_billing_details.click_continue_button_billing_details()

        checkout_page.open_delivery_method.click_continue_button()
        time.sleep(1)

        checkout_page.open_payment_method.click_terms_and_conditions_checkbox()
        checkout_page.open_payment_method.click_continue_button()

        checkout_page.open_confirm_order.click_confirm_order_button()
        time.sleep(1)

        #todo move 'title' in constant
        assert "Your order has been placed!" in self.driver.title

    def teardown(self) -> None:
        """Close the driver.

        :return: None.
        """
        self.driver.close()
