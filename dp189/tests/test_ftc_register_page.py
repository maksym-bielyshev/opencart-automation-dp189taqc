"""Module for the testing 'Register' page."""

import pytest
from dp189.pages.register_page import RegisterPage
from dp189.pages.home_page import HomePage
from dp189.tests.base_test import BaseTest
from dp189.tests.conftest import get_test_data
from dp189.routes import *


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

    @pytest.mark.parametrize('first_name', get_test_data('register_page/first_name_positive.csv'))
    def test_check_first_name_field_valid_data(self, first_name: str) -> None:
        """Check the 'First name' field with valid data on register page.

        :param first_name: test data for 'First name' field
        :return: None
        """

        self.register_page.your_personal_details_form.first_name_field.clear_and_fill_input_field(first_name)
        self.register_page.privacy_policy_checkbox.agree_with_privacy_policy()
        self.register_page.click_continue_button()

        assert not self.register_page.your_personal_details_form.first_name_field.error_message.get_error_message()

    def test_check_email_field_valid_data(self) -> None:
        """Check the 'Email' field with valid data on register page.

        :return: None
        """

        self.register_page.your_personal_details_form.email_field.clear_and_fill_input_field('test@gmail.com')
        self.register_page.click_continue_button()

        assert not self.register_page.your_personal_details_form.email_field.error_message.get_error_message()

    @pytest.mark.parametrize('last_name,error_message', get_test_data('register_page/last_name_negative.csv'))
    def test_check_last_name_field_invalid_data(self, last_name: str, error_message: str) -> None:
        """Check the 'First name' field with valid data on register page.

        :param last_name: test data for 'Last name' field
        :param error_message: error message under 'Last Name' field
        :return: None
        """

        self.register_page.your_personal_details_form.last_name_field.clear_and_fill_input_field(last_name)
        self.register_page.privacy_policy_checkbox.agree_with_privacy_policy()
        self.register_page.click_continue_button()

        assert self.register_page.your_personal_details_form.last_name_field.error_message.\
            get_error_message() == error_message
