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

    def test_check_first_name_field_valid_data(self):
        pass
