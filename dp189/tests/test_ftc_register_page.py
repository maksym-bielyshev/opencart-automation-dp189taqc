"""Module for the testing 'Register' page."""

import pytest
import allure
from dp189.pages.register_page import RegisterPage
from dp189.pages.home_page import HomePage
from dp189.tests.base_test import BaseTest
from dp189.tests.conftest import get_test_data
from dp189.routes import *
from dp189.constants import RegistrationPageConstants


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
    @pytest.mark.parametrize('test_input', get_test_data('register_page/field_first_name_valid.csv'))
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
    @pytest.mark.parametrize('test_input,error_message', get_test_data('register_page/field_last_name_invalid.csv'))
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
    @pytest.mark.parametrize('test_input,expected', get_test_data('register_page/field_email_invalid.csv'))
    def test_check_email_field_invalid_data(self, test_input: str, expected: str) -> None:
        """Check the 'E-mail' field with invalid data on the register page.

        :param test_input: test data for the 'E-mail' field
        :param expected: expected result for 'E-mail' field
        :return: None
        """
        self.register_page.your_personal_details_form.email_field.clear_and_fill_input_field(test_input)
        self.register_page.click_continue_button()
        assert self.register_page.your_personal_details_form.email_field \
                   .error_message.get_error_message() == expected

    @allure.severity(allure.severity_level.MINOR)
    def test_check_confirm_password_field_valid_data(self):
        """Check the 'Confirm password' field with valid data on register page.

        :return: None
        """
        self.register_page.your_password_form.password_field.clear_and_fill_input_field('testpass')
        self.register_page.your_password_form.password_confirm_field.clear_and_fill_input_field('testpass')
        self.register_page.privacy_policy_checkbox.agree_with_privacy_policy()
        self.register_page.click_continue_button()

        assert not self.register_page.your_password_form.password_confirm_field.error_message.get_error_message()

    @allure.severity(allure.severity_level.NORMAL)
    def test_checked_privacy_policy(self) -> None:
        """Check for no warning message if "Privacy Policy" is checked.

        :return:None
        """
        self.register_page.privacy_policy_checkbox.agree_with_privacy_policy()
        self.register_page.click_continue_button()
        assert not self.register_page.catch_info_message.get_danger_message()

    @allure.severity(allure.severity_level.MINOR)
    def test_unchecked_privacy_policy(self) -> None:
        """Check displaying warning message if 'Privacy Policy' is unchecked.

        :return:None
        """
        self.register_page.click_continue_button()
        assert self.register_page.catch_info_message.get_danger_message() == \
               RegistrationPageConstants.PRIVACY_POLICY_WARNING_MESSAGE

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('test_input,expected', get_test_data('register_page/field_password_confirm_invalid.csv'))
    def test_check_password_confirm_field_invalid_data(self, test_input: str, expected: str) -> None:
        """Check the 'Password Confirm' field with invalid data on the register page.

        :param test_input: test data for the 'Password Confirm' field
        :param expected: expected result for the 'Password Confirm' field
        :return: None
        """
        self.register_page.your_password_form.password_field.clear_and_fill_input_field('testpass')
        self.register_page.your_password_form.password_confirm_field.clear_and_fill_input_field(test_input)
        self.register_page.privacy_policy_checkbox.agree_with_privacy_policy()
        self.register_page.click_continue_button()
        assert self.register_page.your_password_form.password_confirm_field \
                   .error_message.get_error_message() == expected
