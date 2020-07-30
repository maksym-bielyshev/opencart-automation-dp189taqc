"""Module for the testing 'Checkout' page."""

import pytest
from dp189.components import ProductWidgetComponent
from dp189.constants import CheckoutPageConstants
from dp189.pages.checkout_page import CheckoutPage
from dp189.pages.home_page import HomePage
from dp189.tests.base_test import BaseTest
from dp189.tests.conftest import get_test_data
from dp189.routes import *


class TestCheckoutPage(BaseTest):
    def setup(self) -> None:
        """
        Basic set up for Register and Unregister user.

        :return: None
        """
        self.driver.maximize_window()
        self.driver.get(HOME_PAGE_URL)
        self.home_page = HomePage(self.driver)
        ProductWidgetComponent(self.driver, 'iPhone').click_add_to_shopping_cart_button()
        self.home_page.top_nav_bar.click_checkout_link()
        self.checkout_page = CheckoutPage(self.driver)


class TestCheckoutPageGuest(TestCheckoutPage):
    """Class for the 'Checkout' page."""

    def setup(self) -> None:
        """Setup for the test.

        :return: None
        """
        super(TestCheckoutPageGuest, self).setup()
        self.checkout_page.open_checkout_options.click_guest_checkout_radio_button()
        self.checkout_page.open_checkout_options.click_continue_button()

    def test_guest_checkout_with_valid_data(self) -> None:
        """Test the 'Checkout' page with valid data.

        :return: None.
        """
        self.checkout_page.open_billing_details.your_address_form.first_name_field.clear_and_fill_input_field("Maksym")
        self.checkout_page.open_billing_details.your_address_form.last_name_field.clear_and_fill_input_field(
            "Bielyshev")
        self.checkout_page.open_billing_details.your_address_form.email_field_payment.clear_and_fill_input_field(
            "email@email.com")
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

        self.checkout_page.open_payment_method.click_terms_and_conditions_checkbox()
        self.checkout_page.open_payment_method.click_continue_button()

        self.checkout_page.open_confirm_order.click_confirm_order_button()

        assert self.checkout_page.get_title.get_title_page('Your order has been placed!')

    @pytest.mark.parametrize('first_name,error_message',
                             get_test_data('test_data_checkout_page_first_name-negative.csv'))
    def test_guest_checkout_billing_details_first_name_negative(self, first_name: str, error_message: str) -> None:
        """Check 'First Name' field with invalid data in 'Step 2: Billing Details' tab.

        :param first_name: test data for 'First Name' field
        :param error_message: error message under 'First Name' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_personal_details_form \
            .first_name_field.clear_and_fill_input_field(first_name)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert self.checkout_page.open_billing_details \
                   .your_personal_details_form.first_name_field \
                   .error_message.get_error_message() == error_message

    @pytest.mark.parametrize('first_name', get_test_data('test_data_checkout_page_first_name-positive.csv'))
    def test_guest_checkout_billing_details_first_name_positive(self, first_name: str) -> None:
        """Check 'First Name' field with valid data in 'Step 2: Billing Details' tab.

        :param first_name: test data for 'First Name' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_personal_details_form \
            .first_name_field.clear_and_fill_input_field(first_name)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert not self.checkout_page.open_billing_details.your_personal_details_form.first_name_field \
            .error_message.get_error_message()

    @pytest.mark.parametrize('test_input', get_test_data('test_data_checkout_page_last_name-positive .csv'))
    def test_guest_checkout_billing_details_last_name_positive(self, test_input: str) -> None:
        """Check 'Last Name' field with valid data in 'Step 2: Billing Details' tab.

        :param test_input: test data for 'Last Name' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_personal_details_form \
            .last_name_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert not self.checkout_page.open_billing_details.your_personal_details_form \
            .last_name_field.error_message.get_error_message()

    @pytest.mark.parametrize('test_input,expected', get_test_data('test_data_checkout_page_last_name-negative.csv'))
    def test_guest_checkout_billing_details_last_name_negative(self, test_input: str, expected: str) -> None:
        """Check 'Last Name' field with invalid data in 'Step 2: Billing Details' tab.

        :param test_input: test data for 'Last Name' field
        :param expected: error message under 'Last Name' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_personal_details_form \
            .last_name_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert self.checkout_page.open_billing_details \
                   .your_personal_details_form.last_name_field \
                   .error_message.get_error_message() == expected

    @pytest.mark.parametrize('test_data', get_test_data('test_data_checkout_page_address_1-positive.csv'))
    def test_guest_checkout_billing_details_address_1_positive(self, test_data: str) -> None:
        """Check 'Address 1' field with valid data in 'Step 2: Billing Details' tab.

        :param test_data: test data for 'Address 1' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_address_form.address_1_field.clear_and_fill_input_field(test_data)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert not self.checkout_page.open_billing_details.your_address_form.address_1_field \
            .error_message.get_error_message()

    @pytest.mark.parametrize('test_input,expected', get_test_data('test_data_checkout_page_address_1-negative.csv'))
    def test_guest_checkout_billing_details_address_1_negative(self, test_input: str, expected: str) -> None:
        """Check 'Address 1' field with valid data in 'Step 2: Billing Details' tab.

        :param test_input: test data for 'Address 1' field
        :param expected: error message under 'Address 1' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_address_form.address_1_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert self.checkout_page.open_billing_details.your_address_form.address_1_field \
                   .error_message.get_error_message() == expected

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
        self.checkout_page.open_billing_details.your_address_form \
            .city_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert self.checkout_page.open_billing_details \
                   .your_address_form.city_field \
                   .error_message.get_error_message() == expected

    @pytest.mark.parametrize('test_input', get_test_data('test_data_checkout_page_city_field-positive.csv'))
    def test_guest_checkout_billing_details_city_field_positive(self, test_input: str) -> None:
        """Check the 'City' field with valid data in 'Step 2: Billing Details' tab.

        :param test_input: test data for the 'City' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_address_form \
            .city_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert not self.checkout_page.open_billing_details.your_address_form.city_field \
            .error_message.get_error_message()

    def test_guest_checkout_billing_details_email_positive(self) -> None:
        """Check 'Email' field with invalid data in 'Step 2: Billing Details' tab.
        :return: None
        """
        self.checkout_page.open_billing_details.your_personal_details_form \
            .email_field.clear_and_fill_input_field('john@gmail.com')
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert not self.checkout_page.open_billing_details.your_personal_details_form \
            .email_field.error_message.get_error_message()

    @pytest.mark.parametrize('email, error_message',
                             get_test_data('test_data_checkout_page_email-negative.csv'))
    def test_guest_checkout_billing_details_email_negative(self, email: str, error_message: str) -> None:
        """Check 'Email' field with invalid data in 'Step 2: Billing Details' tab.

        :param email: test data for 'Email' field
        :param error_message: error message under 'Email' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_personal_details_form \
            .email_field.clear_and_fill_input_field(email)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert self.checkout_page.open_billing_details.your_personal_details_form \
                   .email_field.error_message.get_error_message() == error_message

    @pytest.mark.parametrize('test_input,expected', get_test_data('test_data_checkout_page_post_code_negative.csv'))
    def test_guest_checkout_billing_details_post_code_field_negative(self, test_input: str, expected: str) -> None:
        """Check the 'Post Code' field with invalid data in 'Step 2: Billing Details' tab.

        :param test_input: test data for the 'Post Code' field
        :param expected: error message under the 'Post Code' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_address_form \
            .post_code_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert self.checkout_page.open_billing_details \
                   .your_address_form.post_code_field \
                   .error_message.get_error_message() == expected

    @pytest.mark.parametrize('test_input', get_test_data('test_data_checkout_page_post_code_positive.csv'))
    def test_guest_checkout_billing_details_post_code_field_positive(self, test_input: str) -> None:
        """Check the 'Post Code' field with valid data in 'Step 2: Billing Details' tab.

        :param test_input: test data for the 'Post Code' field
        :return: None
        """

        self.checkout_page.open_billing_details.your_address_form \
            .post_code_field.clear_and_fill_input_field(test_input)
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert not self.checkout_page.open_billing_details.your_address_form.post_code_field \
            .error_message.get_error_message()

    def test_guest_checkout_billing_details_country_positive(self) -> None:
        """Check the 'Country' field with valid data in 'Step 2: Billing Details' tab.

        :return: None
        """
        self.checkout_page.open_billing_details.your_address_form.country.choose_dropdown_option('United States')
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert not self.checkout_page.open_billing_details.your_address_form.country.error_message.get_error_message()

    @pytest.mark.parametrize('test_input,expected', get_test_data('test_data_checkout_page_country-negative.csv'))
    def test_guest_checkout_billing_details_country_negative(self, test_input: str, expected: str) -> None:
        """Check the 'Country' field with valid data in 'Step 2: Billing Details' tab.

        :param test_input: test data for the 'Country' field
        :param expected: error message under 'Country' field
        :return: None
        """
        self.checkout_page.open_billing_details.your_address_form.country.choose_dropdown_option(f" {test_input}")
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert self.checkout_page.open_billing_details.your_address_form.country \
                   .error_message.get_error_message() == expected

    def test_guest_checkout_billing_details_region_positive(self) -> None:
        """Check the 'Region' field with valid data in 'Step 2: Billing Details' tab.

        :return: None
        """
        self.checkout_page.open_billing_details.your_address_form.country.choose_dropdown_option('United States')
        self.checkout_page.open_billing_details.your_address_form.region.choose_dropdown_option('Nevada')
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert not self.checkout_page.open_billing_details.your_address_form.region.error_message.get_error_message()

    def test_guest_checkout_billing_details_region_negative(self) -> None:
        """Check the 'Region' field with valid data in 'Step 2: Billing Details' tab.

        :return: None
        """
        self.checkout_page.open_billing_details.your_address_form.country.choose_dropdown_option('United States')
        self.checkout_page.open_billing_details.click_continue_button_billing_details()
        assert self.checkout_page.open_billing_details.your_address_form.region \
                   .error_message.get_error_message() == CheckoutPageConstants.REGION_FIELD_ERROR_MESSAGE


class TestCheckoutPageRegister(TestCheckoutPage):

    def setup(self) -> None:
        """Setup for the test.

        :return: None
        """
        super(TestCheckoutPageRegister, self).setup()
        self.checkout_page.open_checkout_options.click_register_account_radio_button()
        self.checkout_page.open_checkout_options.click_continue_button()

    def test_checkout_register_account_valid_data(self):
        """Check the functionality of checkout process with register account and valid data."""

        self.checkout_page.open_account_billing_details.your_personal_details_form.first_name_field. \
            clear_and_fill_input_field('John')
        self.checkout_page.open_account_billing_details.your_personal_details_form.last_name_field. \
            clear_and_fill_input_field('Smith')
        self.checkout_page.open_account_billing_details.your_personal_details_form.email_field. \
            clear_and_fill_input_field('jgoe202@gmail.com')
        self.checkout_page.open_account_billing_details.your_personal_details_form.telephone_field. \
            clear_and_fill_input_field('17777777777')
        self.checkout_page.open_account_billing_details.your_password_form.password_field.clear_and_fill_input_field(
            '1234@')
        self.checkout_page.open_account_billing_details.your_password_form.password_confirm_field. \
            clear_and_fill_input_field('1234@')

        self.checkout_page.open_account_billing_details.your_address_from.address_1_field. \
            clear_and_fill_input_field('29 Street')
        self.checkout_page.open_account_billing_details.your_address_from.city_field. \
            clear_and_fill_input_field('Las Vegas')
        self.checkout_page.open_account_billing_details.your_address_from.country. \
            choose_dropdown_option('United States')
        self.checkout_page.open_account_billing_details.your_address_from.region. \
            choose_dropdown_option('Nevada')

        self.checkout_page.open_account_billing_details.click_privacy_policy_checkbox()
        self.checkout_page.open_account_billing_details.click_continue_button()

        self.checkout_page.open_delivery_details.click_continue_button()

        self.checkout_page.open_delivery_method.click_continue_button()

        self.checkout_page.open_payment_method.click_terms_and_conditions_checkbox()
        self.checkout_page.open_payment_method.click_continue_button()

        self.checkout_page.open_confirm_order.click_confirm_order_button()

        assert self.checkout_page.get_title.get_title_page('Your order has been placed!')
