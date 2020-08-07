"""Module for the 'Compare' page tests."""

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dp189.locators import LocatorsComparePageTest
from dp189.pages.compare_page import ComparePage
from dp189.pages.home_page import HomePage
from dp189.constants import ComparePageConstants
from dp189.tests.base_test import BaseTest
from dp189.routes import HOME_PAGE_URL, COMPARE_PAGE_URL
from dp189.components import ProductWidgetComponent

class TestComparePage(BaseTest):
    """Class for the 'Compare' page testing."""

    def setup(self) -> None:
        """Setup for the tests.

        :return: None
        """
        self.driver.get(HOME_PAGE_URL)
        self.page = HomePage(self.driver)

        iphone = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsComparePageTest.IPHONE))
        iphone.click()

        apple_cinema = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsComparePageTest.CINEMA))
        apple_cinema.click()

        compare_page = COMPARE_PAGE_URL
        self.driver.get(compare_page)
        self.page = ComparePage(self.driver)
        self.page.get_rows_in_table()

    @allure.severity(allure.severity_level.NORMAL)
    def test_add_product_to_cart_without_option(self) -> None:
        """Testing addition of a product to the cart without an option.

        :return: None
        """
        self.page.click_add_to_cart_button(ComparePageConstants.IPHONE_ITEM)
        message = self.page.catch_info_message.get_success_message()
        assert ComparePageConstants.IPHONE_SHOPPING_CART_ADDED_MESSAGE in message

    @allure.severity(allure.severity_level.NORMAL)
    def test_add_product_to_cart_with_option(self) -> None:
        """Testing addition a product to the cart with an option.

        :return:
        """
        self.page.click_add_to_cart_button(ComparePageConstants.APPLE_CINEMA_30_ITEM)
        title = self.page.get_title.get_title_page(ComparePageConstants.APPLE_CINEMA_30_TITLE)
        assert title == ComparePageConstants.APPLE_CINEMA_30_TITLE

    @allure.severity(allure.severity_level.MINOR)
    def test_remove_item_from_cart(self) -> None:
        """Testing removal an item from the cart.

        :return: None
        """
        self.page.click_remove_button(ComparePageConstants.IPHONE_ITEM)
        message = self.page.catch_info_message.get_success_message()
        assert ComparePageConstants.PRODUCT_COMPARISON_MODIFIED_MESSAGE in message
