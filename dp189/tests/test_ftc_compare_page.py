from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dp189.pages.compare_page import ComparePage
from dp189.constants import ComparePageConstants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--ignore-certificate-errors')
CHROME_DRIVER = '../driver/chromedriver'


class TestCompareItems:
    def setup(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER, options=options)
        self.driver.maximize_window()
        self.driver.get(ComparePageConstants.BASE_URL)#
        self.page = ComparePage(self.driver)
        self.page.find_element(ComparePageConstants.IPHONE).click()
        self.page.find_element(ComparePageConstants.CINEMA).click()
        self.page.go_to_site()
        self.page.get_rows_in_table()

    def test_add_product_to_cart_without_option(self):
        self.page.click_add_to_cart_button("iPhone")
        message = self.page.find_element(ComparePageConstants.MESSAGE)
        assert message.text == ComparePageConstants.RESULT

    def test_add_product_to_cart_with_option(self):
        self.page.click_add_to_cart_button('Apple Cinema 30"')
        WebDriverWait(self.driver, 3).until(EC.title_is(ComparePageConstants.RESULT2))
        assert self.driver.title == ComparePageConstants.RESULT2

    def test_remove_item_from_cart(self):
        self.page.click_remove_button("iPhone")
        message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(ComparePageConstants.MESSAGE))
        assert message.text == ComparePageConstants.RESULT3

    def teardown(self):
        self.driver.close()
