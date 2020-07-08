from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from locators import LocatorsShoppingCartPage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Remote


class ShoppingCartPage(BasePage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    def open_coupon_panel(self):
        return self._driver.find_element(*LocatorsShoppingCartPage.COUPON_PANEL)

    def fill_coupon_field(self, item: str):
        return self._driver.find_element(*LocatorsShoppingCartPage.COUPON_FIELD).send_keys(item)

    def click_apply_coupon_button(self):
        return self._driver.find_element(*LocatorsShoppingCartPage.COUPON_APPLY_BUTTON).click()

    def open_estimate_shipping_panel(self):
        return self._driver.find_element(*LocatorsShoppingCartPage.ESTIMATE_SHIPPING_PANEL).click()

    def fill_post_code_field(self, item: str):
        return self._driver.find_element(*LocatorsShoppingCartPage.POST_CODE_FIELD).send_keys(item)

    def click_get_quotes_button(self):
        return self._driver.find_element(*LocatorsShoppingCartPage.GET_QUOTES_BUTTON).click()

    def open_gift_certificate_panel(self):
        return self._driver.find_element(*LocatorsShoppingCartPage.GIFT_CERTIFICATE_PANEL)

    def fill_gift_certificate_field(self, item: str):
        return self._driver.find_element(*LocatorsShoppingCartPage.CERTIFICATE_FIELD).send_keys(item)

    def click_apply_gift_certificate_button(self):
        return self._driver.find_element(*LocatorsShoppingCartPage.CERTIFICATE_APPLY_BUTTON).click()

    def click_continue_shipping_button(self):
        self._driver.find_element(*LocatorsShoppingCartPage.CONTINUE_SHIPPING_BUTTON).click()
        # return HomePage(self._driver)

    def click_checkout_button(self):
        self._driver.find_element(*LocatorsShoppingCartPage.CHECKOUT_BUTTON).click()
        # return CheckoutPage(self._driver)

    def get_sub_total_sum(self):
        return self._driver.find_element(*LocatorsShoppingCartPage.SUB_TOTAL_ORDER_SUM).text()

    def get_total_sum(self):
        return self._driver.find_element(*LocatorsShoppingCartPage.TOTAL_ORDER_SUM).text()


class ProductInCart:
    def __init__(self, driver):
        self._driver = driver
        # self.model =
        # self.unit_price =
        # self.price =

