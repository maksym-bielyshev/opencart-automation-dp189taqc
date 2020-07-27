"""Module for the testing 'Checkout' page."""
import pytest

from dp189.pages.checkout_page import CheckoutPage
from dp189.components import ProductWidgetComponent
from dp189.tests.base_test import BaseTest
from dp189.routes import *
import time

from dp189.tests.conftest import get_test_data


class TestCheckoutPage(BaseTest):
    """Class for the 'Checkout' page."""

    def setup(self) -> None:
        """Setup for the test.

        :return: None
        """

        self.driver.maximize_window()
        self.driver.get(HOME_PAGE_URL)
        ProductWidgetComponent(self.driver, 'iPhone').click_add_to_shopping_cart_button()
        self.driver.get(CHECKOUT_PAGE_URL)

        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.open_checkout_options.click_guest_checkout_radio_button()
        self.checkout_page.open_checkout_options.click_continue_button()

    def test_guest_checkout_with_valid_data(self) -> None:
        """Test the 'Checkout' page with valid data.

        :return: None.
        """
        self.checkout_page.open_billing_details.load_your_address_form()
        self.checkout_page.open_billing_details.your_address_form.first_name_field.clear_and_fill_input_field("Maksym")
        self.checkout_page.open_billing_details.your_address_form.last_name_field.clear_and_fill_input_field("Bielyshev")
        self.checkout_page.open_billing_details.your_address_form.email_field_payment.clear_and_fill_input_field("email@email.com")
        self.checkout_page.open_billing_details.your_address_form.telephone_field.clear_and_fill_input_field("12345")
        self.checkout_page.open_billing_details.your_address_form.company_field.clear_and_fill_input_field("test")
        self.checkout_page.open_billing_details.your_address_form.address_1_field.clear_and_fill_input_field("test")
        self.checkout_page.open_billing_details.your_address_form.address_2_field.clear_and_fill_input_field("test")
        self.checkout_page.open_billing_details.your_address_form.city_field.clear_and_fill_input_field("test")
        self.checkout_page.open_billing_details.your_address_form.post_code_field.clear_and_fill_input_field("test")
        self.checkout_page.open_billing_details.your_address_form.country.choose_dropdown_option("Ukraine")
        self.checkout_page.open_billing_details.your_address_form.region.choose_dropdown_option("Kyiv")
        self.checkout_page.open_billing_details.click_continue_button_billing_details()

        self.checkout_page.open_delivery_method.click_continue_button()
        time.sleep(1)

        self.checkout_page.open_payment_method.click_terms_and_conditions_checkbox()
        self.checkout_page.open_payment_method.click_continue_button()

        self.checkout_page.open_confirm_order.click_confirm_order_button()
        time.sleep(1)

        #todo move 'title' in constant
        assert "Your order has been placed!" in self.driver.title

    @pytest.mark.parametrize('test_input,expected', get_test_data('test_data_checkout_page_first_name-negative.csv'))
    def test_guest_checkout_billing_details_first_name_negative(self, test_input: str, expected: str) -> None:
        """Check 'First Name' field with invalid data in 'Step 2: Billing Details' tab.

        :param test_input: test data for 'First Name' field
        :param expected: error message under 'First Name' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_personal_details_form\
            .first_name_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert self.checkout_page.open_billing_details\
                   .your_personal_details_form.first_name_field\
                   .error_message.get_error_message() == expected

    @pytest.mark.parametrize('test_input', get_test_data('test_data_checkout_page_first_name-positive.csv'))
    def test_guest_checkout_billing_details_first_name_positive(self, test_input: str) -> None:
        """Check 'First Name' field with valid data in 'Step 2: Billing Details' tab.

        :param test_input: test data for 'First Name' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_personal_details_form\
            .first_name_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert not self.checkout_page.open_billing_details.your_personal_details_form.first_name_field\
                       .error_message.get_error_message()

    @pytest.mark.parametrize('test_input', get_test_data('test_data_checkout_page_telephone_field_positive.csv'))
    def test_guest_checkout_billing_details_telephone_field_positive(self, test_input: str) -> None:
        """Check 'Telephone' field with valid data in 'Step 2: Billing Details' tab.

       :param test_input: test data for the 'Telephone' field
       :return: None
       """
        self.checkout_page.open_billing_details.your_personal_details_form \
            .telephone_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert not self.checkout_page.open_billing_details.your_personal_details_form.telephone_field \
            .error_message.get_error_message()

    @pytest.mark.parametrize('test_input,expected',
                             get_test_data('test_data_checkout_page_telephone_field_negative.csv'))
    def test_guest_checkout_billing_details_telephone_field_negative(self, test_input: str, expected: str) -> None:
        """Check 'Telephone' field with invalid data in 'Step 2: Billing Details' tab.

       :param test_input: test data for 'Telephone' field
       :param expected: error message under 'Telephone' field
       :return: None
       """
        self.checkout_page.open_billing_details.your_personal_details_form \
            .first_name_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert self.checkout_page.open_billing_details \
                   .your_personal_details_form.telephone_field \
                   .error_message.get_error_message() == expected


    @pytest.mark.parametrize('test_input,expected', get_test_data('test_data_checkout_page_city_field-negative.csv'))
    def test_guest_checkout_billing_details_city_field_negative(self, test_input: str, expected: str) -> None:
        """Check 'City' field with invalid data in 'Step 2: Billing Details' tab.

        :param test_input: test data for the 'City' field
        :param expected: error message under the 'City' field
        :return: None
        """
        self.checkout_page.open_billing_details.load_your_address_form()
        self.checkout_page.open_billing_details.your_address_form\
            .city_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert self.checkout_page.open_billing_details\
                   .your_address_form.city_field\
                   .error_message.get_error_message() == expected

    @pytest.mark.parametrize('test_input', get_test_data('test_data_checkout_page_city_field-positive.csv'))
    def test_guest_checkout_billing_details_city_field_positive(self, test_input: str) -> None:
        """Check the 'City' field with valid data in 'Step 2: Billing Details' tab.

        :param test_input: test data for the 'City' field
        :return: None
        """
        self.checkout_page.open_billing_details.load_your_address_form()
        self.checkout_page.open_billing_details.your_address_form\
            .city_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert not self.checkout_page.open_billing_details.your_address_form.city_field\
                       .error_message.get_error_message()
