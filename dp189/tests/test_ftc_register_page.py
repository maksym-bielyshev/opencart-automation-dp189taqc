"""Module for the testing 'Register' page."""

import pytest
import allure
from dp189.pages.register_page import RegisterPage
from dp189.pages.home_page import HomePage
from dp189.tests.base_test import BaseTest
from dp189.tests.conftest import get_test_data
from dp189.routes import *


@allure.severity(allure.severity_level.NORMAL)
class TestRegisterPage(BaseTest):
    """Class for the 'Register' page."""

    def setup(self) -> None:
        """Setup for the test.

        :return: None
        """

        self.driver.maximize_window()
        self.driver.get(HOME_PAGE_URL)
        self.home_page = HomePage(self.driver)
        self.home_page.click_account_and_go_to_register()

        self.register_page = RegisterPage(self.driver)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('test_input', get_test_data('register_page/first_name_positive.csv'))
    def test_check_first_name_field_valid_data(self, test_input: str) -> None:
        """Check the 'First name' field with valid data on register page.

        :param test_input: test data for 'First name' field
        :return: None
        """

        self.register_page.your_personal_details_form.first_name_field.clear_and_fill_input_field(test_input)
        self.register_page.privacy_policy_checkbox.agree_with_privacy_policy()
        self.register_page.click_continue_button()

        assert not self.register_page.your_personal_details_form.first_name_field.error_message.get_error_message()

    @pytest.mark.parametrize('test_input', get_test_data('register_page/field_last_name.csv'))
    def test_check_last_name_field_valid_data(self, test_input: str) -> None:
        """Check the 'Last name' field with valid data on the register page.

        :param test_input: test data for the 'last name' field
        :return: None
        """

        self.register_page.your_personal_details_form.last_name_field.clear_and_fill_input_field(test_input)
        self.register_page.privacy_policy_checkbox.agree_with_privacy_policy()
        self.register_page.click_continue_button()

        assert not self.register_page.your_personal_details_form.last_name_field.error_message.get_error_message()


    def test_check_email_field_valid_data(self) -> None:
        """Check the 'Email' field with valid data on register page.

        :return: None
        """

        self.register_page.your_personal_details_form.email_field.clear_and_fill_input_field('test@gmail.com')
        self.register_page.click_continue_button()

        assert not self.register_page.your_personal_details_form.email_field.error_message.get_error_message()

    @pytest.mark.parametrize('test_input', get_test_data('register_page/field_telephone-valid.csv'))
    def test_check_telephone_field_valid_data(self, test_input: str) -> None:
        """Check the 'Telephone' field with valid data on register page.

        :param test_input: test data for 'first name' field
        :return: None
        """

        self.register_page.your_personal_details_form.telephone_field.clear_and_fill_input_field(test_input)
        self.register_page.click_continue_button()

        assert not self.register_page.your_personal_details_form.telephone_field.error_message.get_error_message()

    @pytest.mark.parametrize('test_input,expected', get_test_data('register_page/field_telephone_invalid.csv'))
    def test_check_telephone_field_invalid_data(self, test_input: str, expected: str) -> None:
        """Check the 'Telephone' field with invalid data on register page.

        :param test_input: test data for 'Telephone' field
        :param expected: expected result for 'Telephone' field
        :return: None
        """

        self.register_page.your_personal_details_form.telephone_field.clear_and_fill_input_field(test_input)
        self.register_page.click_continue_button()

        assert self.register_page.your_personal_details_form.telephone_field \
                   .error_message.get_error_message() == expected

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('test_input,error_message', get_test_data('register_page/last_name_negative.csv'))
    def test_check_last_name_field_invalid_data(self, test_input: str, error_message: str) -> None:
        """Check the 'First name' field with valid data on register page.

        :param test_input: test data for 'Last name' field
        :param error_message: error message under 'Last Name' field
        :return: None
        """

        self.register_page.your_personal_details_form.last_name_field.clear_and_fill_input_field(test_input)
        self.register_page.privacy_policy_checkbox.agree_with_privacy_policy()
        self.register_page.click_continue_button()

        assert self.register_page.your_personal_details_form.last_name_field.error_message. \
                   get_error_message() == error_message

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('test_input', get_test_data('register_page/field_password.csv'))
    def test_check_password_field_valid_data(self, test_input: str) -> None:
        """Check the 'Password' field with valid data on register page.

        :param test_input: test data for 'Password' field
        :return:None
        """
        self.register_page.your_password_form.password_field.clear_and_fill_input_field(test_input)
        self.register_page.click_continue_button()

        assert not self.register_page.your_password_form.password_field.error_message.get_error_message()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('test_input,expected', get_test_data('register_page/field_password_invalid.csv'))
    def test_check_password_field_invalid_data(self, test_input: str, expected: str) -> None:
        """Check the 'Password' field with valid data on register page.

        :param test_input: test data for 'Password' field
        :param expected: expected result for 'Password' field
        :return:None
        """
        self.register_page.your_password_form.password_field.clear_and_fill_input_field(test_input)
        self.register_page.click_continue_button()
        assert self.register_page.your_password_form.password_field \
                   .error_message.get_error_message() == expected

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('first_name_field,last_name_field,email_field,telephone_field,password_field,'
                             'password_confirm_field',get_test_data('register_page/registration_form_positive.csv'))
    def test_registration_form(self, first_name_field: str, last_name_field: str, email_field: str,
                               telephone_field: str, password_field: str, password_confirm_field: str) -> None:
        """Check the registration form on the registration page.

        :return: None
        """
        self.register_page.your_personal_details_form.first_name_field.clear_and_fill_input_field(first_name_field)
        self.register_page.your_personal_details_form.last_name_field.clear_and_fill_input_field(last_name_field)
        self.register_page.your_personal_details_form.email_field.clear_and_fill_input_field(email_field)
        self.register_page.your_personal_details_form.telephone_field.clear_and_fill_input_field(telephone_field)
        self.register_page.your_password_form.password_field.clear_and_fill_input_field(password_field)
        self.register_page.your_password_form.password_confirm_field.clear_and_fill_input_field(password_confirm_field)
        self.register_page.privacy_policy_checkbox.agree_with_privacy_policy()
        self.register_page.click_continue_button()

        assert self.register_page.get_title.get_title_page('Your Account Has Been Created!')
