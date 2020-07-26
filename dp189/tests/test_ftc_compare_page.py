from dp189.locators import LocatorsComparePageTest
from selenium.webdriver.chrome.options import Options
from dp189.pages.compare_page import ComparePage
from dp189.pages.home_page import HomePage
from dp189.constants import ComparePageConstants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dp189.tests.base_test import BaseTest
from dp189.routes import *


class TestComparePage(BaseTest):
    def setup(self):
        super().setup()
        self.driver.maximize_window()
        self.driver.get(HOME_PAGE_URL)
        self.page = HomePage(self.driver)
        self.page.find_element(LocatorsComparePageTest.IPHONE).click()
        self.page.find_element(LocatorsComparePageTest.CINEMA).click()
        self.driver.get(COMPARE_PAGE_URL)
        self.page = ComparePage(self.driver)
        self.page.get_rows_in_table()

    def test_add_product_to_cart_without_option(self):
        self.page.click_add_to_cart_button(ComparePageConstants.TEST_ITEM1)
        message = self.page.catch_info_message.get_info_message()
        assert message == ComparePageConstants.RESULT

    def test_add_product_to_cart_with_option(self):
        self.page.click_add_to_cart_button(ComparePageConstants.TEST_ITEM2)
        title = self.page.get_title.get_title_page(ComparePageConstants.RESULT2)
        assert title == ComparePageConstants.RESULT2

    def test_remove_item_from_cart(self):
        self.page.click_remove_button(ComparePageConstants.TEST_ITEM1)
        message = self.page.catch_info_message.get_info_message()
        assert message == ComparePageConstants.RESULT3

    def teardown(self):
        self.driver.close()
