"""Module for the testing 'Product' page."""
import datetime

import pytest

from dp189.pages.product_page import ProductPage
from dp189.routes import get_product_url
from dp189.tests.base_test import BaseTest
from dp189.tests.conftest import get_test_data
from dp189.routes import *


class TestAvailableOptions(BaseTest):
    def setup(self) -> None:
        """Setup for the test.

        :return: None
        """

        self.driver.maximize_window()
        self.driver.get(get_product_url('42'))
        self.product_page = ProductPage(self.driver)

    def test_radio_option_is_not_selected(self) -> None:
        """Test for checking if available option Radio is empty and it will be error message for this option after attempt
        to add product to cart.

        :return: None
        """
        if self.product_page.available_options.radio.which_option_is_chosen() is None:
            self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'Radio required!'
        assert self.product_page.available_options.radio.error_message.get_error_message() == expected_result

    @pytest.mark.parametrize('radio_option, expected_result',
                             get_test_data('product_page/test_data_product_page_radio_positive.csv'))
    def test_radio_option_is_selected(self, radio_option, expected_result) -> None:
        """Test for checking if available option Radio is selected and it will be this option after attempt
        to add product to cart.

        :param radio_option: str (example: Small (+$10.00))
        :param expected_result: str (example: Medium (+$20.00))
        :return: None
        """
        if self.product_page.available_options.radio.which_option_is_chosen() is None:
            self.product_page.available_options.radio.choose_radio_button_option(radio_option)
            self.product_page.available_options.click_add_to_cart_button()
        assert self.product_page.available_options.radio.which_option_is_chosen() == expected_result

    def test_checkbox_option_is_not_selected(self) -> None:
        """Test for checking if available option Checkbox is empty and it will be error message for this option after
        attempt to add product to cart.

        :return: None
        """
        if self.product_page.available_options.checkbox.which_option_is_chosen() == []:
            self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'Checkbox required!'
        assert self.product_page.available_options.checkbox.error_message.get_error_message() == expected_result

    @pytest.mark.parametrize('checkbox_option, expected_result',
                             get_test_data('product_page/test_data_product_page_checkbox_positive.csv'))
    def test_checkbox_option_is_selected(self, checkbox_option, expected_result) -> None:
        """Test for checking if available option Checkbox is selected and it will be this option after attempt
        to add product to cart.

        :param checkbox_option: str (example: Checkbox 1 (+$10.00))
        :param expected_result: str (example: Checkbox 2 (+$20.00)
        :return: None
        """
        self.product_page.available_options.checkbox.choose_checkbox_option(checkbox_option)
        self.product_page.available_options.click_add_to_cart_button()
        assert self.product_page.available_options.checkbox.which_option_is_chosen() == expected_result

    def test_color_is_not_selected(self) -> None:
        """Test for checking if available option Color is empty and it will be error message for this option after attempt
        to add product to cart.

        :return: None
        """
        initial_state = ' --- Please Select --- '
        if self.product_page.available_options.select.which_option_is_chosen() == initial_state:
            self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'Color required!'
        assert self.product_page.available_options.select.error_message.get_error_message() == expected_result

    @pytest.mark.parametrize('color_option, expected_result',
                             get_test_data('product_page/test_data_product_page_color_positive.csv'))
    def test_color_option_is_selected(self, color_option, expected_result) -> None:
        """Functionality test for checking if color select option is working.

        :return: None
        """
        self.product_page.available_options.select.choose_dropdown_option(color_option)
        self.product_page.available_options.click_add_to_cart_button()
        option_list = self.product_page.available_options.select.which_option_is_chosen().split()
        assert ' '.join(option_list) == expected_result

    def test_date_field_is_not_filled(self) -> None:
        """Test for checking if available option Date is empty and it will be error message for this option after attempt
        to add product to cart.

        :return: None
        """
        self.product_page.available_options.data_field.clear_and_fill_input_field('')
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'Date required!'
        assert self.product_page.available_options.data_field.error_message.get_error_message() == expected_result

    @pytest.mark.parametrize('date_field_input',
                             get_test_data('product_page/test_data_product_page_date_invalid_data.csv'))
    def test_date_field_is_filled_invalid_data(self, date_field_input: str) -> None:
        """Test for checking if available option Date field is filled with invalid data that consists invalid format,
        letters or symbols and it will be error message for this option after attempt to add product to cart.

        :param date_field_input: str (example: First of August)
        :return: None
        """
        self.product_page.available_options.data_field.clear_and_fill_input_field(date_field_input)
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'Date does not appear to be valid. Date format: YYYY-MM-DD.'
        assert self.product_page.available_options.data_field.error_message.get_error_message() == expected_result

    def test_date_field_is_filled_wrong_date(self) -> None:
        """Test for checking if available option Date field is filled with wrong date that consists date of today,
        yesterday or previous days it will be error message for this option after attempt to add product to cart.

        :return: None
        """
        today = str(datetime.date.today())
        self.product_page.available_options.data_field.clear_and_fill_input_field(today)
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'You can choose only tomorrow\'s date or more.'
        assert self.product_page.available_options.data_field.error_message.get_error_message() == expected_result

    def test_date_field_is_filled_valid_data(self) -> None:
        """Test for checking if available option Date field is filled with valid data that consists date of tomorrow,
        yesterday or subsequent days it will be no error message for this option after attempt to add product to cart.

        :return: None
        """
        today = datetime.date.today()
        tomorrow = str(today + datetime.timedelta(days=1))
        self.product_page.available_options.data_field.clear_and_fill_input_field(tomorrow)
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = False
        assert self.product_page.available_options.data_field.error_message.get_error_message() == expected_result

    def test_time_field_is_not_filled(self) -> None:
        """Test for checking if available option Time is empty and it will be error message for this option after attempt
        to add product to cart.

        :return: None
        """
        self.product_page.available_options.time.clear_and_fill_input_field('')
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'Time required!'
        assert self.product_page.available_options.time.error_message.get_error_message() == expected_result

    @pytest.mark.parametrize('time_field_input',
                             get_test_data('product_page/test_data_product_page_time_invalid_data.csv'))
    def test_time_field_is_filled_invalid_data(self, time_field_input: str) -> None:
        """Test for checking if available option Time field is filled with invalid data that consists invalid format,
        letters or symbols and it will be error message for this option after attempt to add product to cart.

        :param time_field_input: str (example: 04:00 p.m.)
        :return: None
        """
        self.product_page.available_options.time.clear_and_fill_input_field(time_field_input)
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'Time does not appear to be valid. Time format: HH-mm.'
        assert self.product_page.available_options.time.error_message.get_error_message() == expected_result

    @pytest.mark.parametrize('time_field_input',
                             get_test_data('product_page/test_data_product_page_time_wrong_time.csv'))
    def test_time_field_is_filled_wrong_time(self, time_field_input: str) -> None:
        """Test for checking if available option Time field is filled with wrong time that consists from 08:00 to 20:00
        it will be error message for this option after attempt to add product to cart.

        :param time_field_input: str (example: 07:59)
        :return: None
        """
        self.product_page.available_options.time.clear_and_fill_input_field(time_field_input)
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'You can choose time only from 08:00 to 20:00.'
        assert self.product_page.available_options.time.error_message.get_error_message() == expected_result

    @pytest.mark.parametrize('time_field_input',
                             get_test_data('product_page/test_data_product_page_time_valid_data.csv'))
    def test_time_field_is_filled_valid_data(self, time_field_input) -> None:
        """Test for checking if available option Date field is filled with valid data that consists from 08:00 to 20:00
        it will be no error message for this option after attempt to add product to cart.

        :param time_field_input: str (example: 16:00)
        :return: None
        """
        self.product_page.available_options.time.clear_and_fill_input_field(time_field_input)
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = False
        assert self.product_page.available_options.time.error_message.get_error_message() == expected_result

    def test_text_field_not_filled(self) -> None:
        """Test for checking if available option Text is empty. There will be error message for this option after
        attempt to add product to cart.

        :return: None
        """
        self.product_page.available_options.text_field.clear_and_fill_input_field('')
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'Text required!'
        assert self.product_page.available_options.text_field.error_message.get_error_message() == expected_result

    @pytest.mark.parametrize('text_field_input',
                             get_test_data('product_page/test_data_product_page_text_field.csv'))
    def test_text_field_is_filled_valid_data(self, text_field_input: str) -> None:
        """Test for checking if available option Text field is filled with valid data that consists from 1 to 40
        characters. There will be no error message for this option after attempt to add product to cart.

        :param text_field_input: str (example: 'test')
        :return: None
        """
        self.product_page.available_options.text_field.clear_and_fill_input_field(text_field_input)
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = False
        assert self.product_page.available_options.text_field.error_message.get_error_message() == expected_result

    def test_text_field_is_filled_invalid_data(self) -> None:
        """Test for checking if available option Text is filled with text string that is longer than 40 characters.
        There should be error message 'Text must be between 1 and 40 characters!' for this option after attempt
        to add product to cart.

        :return: None
        """
        text_field_input = 'testtesttesttesttesttesttesttesttesttestt'
        self.product_page.available_options.text_field.clear_and_fill_input_field(text_field_input)
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'Text must be between 1 and 40 characters!'
        assert self.product_page.available_options.text_field.error_message.get_error_message() == expected_result

    def test_quantity_field_not_filled(self) -> None:
        """Test for checking if available option Quantity field is empty. There will be error message for this option
        after attempt to add product to cart.

        :return: None
        """
        self.product_page.available_options.quantity.clear_and_fill_input_field('')
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'Quantity required!'
        assert self.product_page.available_options.quantity.error_message.get_error_message() == expected_result

    def test_quantity_field_is_filled_valid_data(self) -> None:
        """Test for checking if available option Quantity field is filled with valid data: more than 2.
        There will be no error message for this option after attempt to add product to cart.

        :return: None
        """
        self.product_page.available_options.quantity.clear_and_fill_input_field('5')
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = False
        assert self.product_page.available_options.quantity.error_message.get_error_message() == expected_result

    def test_quantity_field_is_filled_invalid_data(self) -> None:
        """Test for checking if available option Quantity field is filled with invalid data: less than 2.
        There will be error message for this option after attempt to add product to cart.

        :return: None
        """
        self.product_page.available_options.quantity.clear_and_fill_input_field('1')
        self.product_page.available_options.click_add_to_cart_button()
        expected_result = 'This product has a minimum quantity of 2!'
        assert self.product_page.available_options.quantity.error_message.get_error_message() == expected_result

    def test_add_to_cart_button_with_all_selected_available_options(self) -> None:
        """Check correct work of clicking on 'Add to Cart' button by filling all required fields.

        :return: None
        """
        today = datetime.date.today()
        tomorrow = str(today + datetime.timedelta(days=1))

        self.product_page.available_options.radio.choose_radio_button_option('Medium')
        self.product_page.available_options.checkbox.choose_checkbox_option('Checkbox 2')
        self.product_page.available_options.text_field.clear_and_fill_input_field('Test text')
        self.product_page.available_options.select.choose_dropdown_option('Blue (+$3.00)')
        self.product_page.available_options.text_area_field.clear_and_fill_input_field('Test textarea')
        self.product_page.available_options.data_field.clear_and_fill_input_field(tomorrow)
        self.product_page.available_options.time.clear_and_fill_input_field('16:00')
        self.product_page.available_options.quantity.clear_and_fill_input_field('5')
        self.product_page.available_options.click_add_to_cart_button()
        info_message = 'Success: You have added Apple Cinema 30" to your shopping cart!'
        assert info_message in self.product_page.catch_info_message.get_success_message()

    def test_click_compare_button(self) -> None:
        """Check correct work of clicking on 'Compare this product' button.

        :return: None
        """
        self.product_page.click_compare_this_product_button()
        info_message = 'Success: You have added Apple Cinema 30" to your product comparison!'
        assert info_message in self.product_page.catch_info_message.get_success_message()

    def test_click_add_to_wish_list_as_not_logged_user(self):
        """Check correct work of clicking 'Add to Wish List' button.

        :return: None
        """
        self.product_page.click_add_to_wish_list_button()
        info_message = 'You must login or create an account to save Apple Cinema 30" to your wish list!'
        assert info_message in self.product_page.catch_info_message.get_success_message()
