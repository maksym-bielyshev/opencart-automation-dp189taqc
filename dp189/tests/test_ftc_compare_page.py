from dp189.locators import LocatorsComparePageTest
from selenium.webdriver.chrome.options import Options
from dp189.pages.compare_page import ComparePage
from dp189.constants import ComparePageConstants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dp189.tests.base_test import BaseTest
from dp189.routes import *


class TestCompareItems(BaseTest):
    def setup(self):
        super().setup()
        self.driver.maximize_window()
        self.driver.get(HOME_PAGE_URL)
        self.page = ComparePage(self.driver)
        self.page.find_element(LocatorsComparePageTest.IPHONE).click()
        self.page.find_element(LocatorsComparePageTest.CINEMA).click()
        self.page.go_to_site()
        self.page.get_rows_in_table()

    def test_add_product_to_cart_without_option(self):
        self.page.click_add_to_cart_button(ComparePageConstants.TEST_ITEM1)
        message = self.page.find_element(LocatorsComparePageTest.MESSAGE)
        assert message.text == ComparePageConstants.RESULT

    def test_add_product_to_cart_with_option(self):
        self.page.click_add_to_cart_button(ComparePageConstants.TEST_ITEM2)
        WebDriverWait(self.driver, 3).until(EC.title_is(ComparePageConstants.RESULT2))
        title = self.page.title_is()
        assert title == ComparePageConstants.RESULT2

    def test_remove_item_from_cart(self):
        self.page.click_remove_button(ComparePageConstants.TEST_ITEM1)
        message = self.page.find_element(LocatorsComparePageTest.MESSAGE)
        assert message.text == ComparePageConstants.RESULT3

    def teardown(self):
        self.driver.close()
