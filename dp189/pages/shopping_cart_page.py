from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from dp189.components import InputFieldComponent
from dp189.pages.base_page import BasePage
from dp189.locators import LocatorsShoppingCartPage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Remote


class ShoppingCartPage(BasePage):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.coupon_panel = CouponPanel(driver)
        self.estimate_shipping_panel = EstimateShippingPanel(driver)
        self.gift_certificate_panel = GiftCertificatePanel(driver)
        self.products_list = []

    def get_products_list(self) -> list:
        product_lines = self._driver.find_elements(*LocatorsShoppingCartPage.PRODUCT_LINES)
        for product in product_lines:
            self.products_list.append(ProductInCart(product))
        return self.products_list

    def get_products_name_list(self) -> list:
        products_name_list = []
        for product in self.products_list:
            products_name_list.append(product.get_name())
        return products_name_list

    def get_products_total_price_list(self) -> list:
        products_total_price_list = []
        for product in self.products_list:
            products_total_price_list.append(product.get_total_price())
        return products_total_price_list

    def get_product_quantity(self, name: str) -> None:
        for product in self.products_list:
            if product.name() == name:
                return product.get_quantity()

    def get_product_unit_price(self, name: str) -> None:
        for product in self.products_list:
            if product.get_name() == name:
                return product.get_unit_price()

    def get_product_total_price(self, name: str) -> None:
        print(self.products_list)
        for product in self.products_list:
            print(product.name)
            if product.name() == name:
                return product.get_total_price()

    def change_product_quantity(self, name: str, quantity) -> object:
        for product in self.products_list:
            if product.name() == name:
                product.set_quantity(quantity)
                product.click_update_button()
                return ShoppingCartPage(self._driver)

    def click_remove_product_button(self, name: str) -> None:
        for product in self.products_list:
            if product.get_name() == name:
                product.click_remove_button()
                self.products_list.remove(product)

    def click_continue_shipping_button(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.CONTINUE_SHIPPING_BUTTON).click()
        # return HomePage(self._driver)

    def click_checkout_button(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.CHECKOUT_BUTTON).click()
        # return CheckoutPage(self._driver)

    def get_flat_shipping_rate(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.FLAT_SHIPPING_RATE).text()

    def get_coupon_sum(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.COUPON_SUM).text()

    def get_sub_total_sum(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.SUB_TOTAL_ORDER_SUM).text()

    def get_total_sum(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.TOTAL_ORDER_SUM).text()


class CouponPanel:
    def __init__(self, driver: Remote):
        self._driver = driver
        self.coupon_field = InputFieldComponent(self._driver, LocatorsShoppingCartPage.COUPON_FIELD)

    def open_coupon_panel(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.COUPON_PANEL).click()

    def click_apply_coupon_button(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.COUPON_APPLY_BUTTON).click()


class EstimateShippingPanel:
    def __init__(self, driver: Remote):
        self._driver = driver
        self.post_code_field = InputFieldComponent(self._driver, LocatorsShoppingCartPage.POST_CODE_FIELD)

    def open_estimate_shipping_panel(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.ESTIMATE_SHIPPING_PANEL).click()

    def select_country(self, country: str) -> None:
        country_selector = Select(self._driver.find_element(*LocatorsShoppingCartPage.COUNTRY_SELECTOR))
        country_selector.select_by_visible_text(country)

    def select_region(self, region: str) -> None:
        country_selector = Select(self._driver.find_element(*LocatorsShoppingCartPage.REGION_SELECTOR))
        country_selector.select_by_visible_text(region)

    def click_get_quotes_button(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.GET_QUOTES_BUTTON).click()

    def click_modal_shipping_radio_button(self, radio_text) -> None:
        self._driver.find_element(By.XPATH, f'//label[text()="{radio_text}"]/input').click()

    def click_modal_shipping_cancel_button(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.MODAL_SHIPPING_CANCEL_BUTTON).click()

    def click_modal_shipping_apply_button(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.MODAL_SHIPPING_APPlY_BUTTON).click()


class GiftCertificatePanel:
    def __init__(self, driver: Remote):
        self._driver = driver
        self.gift_certificate_field = InputFieldComponent(self._driver, LocatorsShoppingCartPage.CERTIFICATE_FIELD)

    def open_gift_certificate_panel(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.GIFT_CERTIFICATE_PANEL)

    def click_apply_gift_certificate_button(self) -> None:
        self._driver.find_element(*LocatorsShoppingCartPage.CERTIFICATE_APPLY_BUTTON).click()


class ProductInCart:
    def __init__(self, product: WebElement):
        # self._driver = driver
        self._product = product
        # self.name = self._product.find_element(*LocatorsShoppingCartPage.PRODUCT_NAME).text
        # self.quantity = self._product.find_element(*LocatorsShoppingCartPage.PRODUCT_QUANTITY).get_attribute('value')
        # self.quantity_field = InputFieldComponent(self._driver, LocatorsShoppingCartPage.PRODUCT_QUANTITY)

    def get_name(self) -> str:
        return self._product.find_element(*LocatorsShoppingCartPage.PRODUCT_NAME).text

    def get_model(self) -> str:
        return self._product.find_element(*LocatorsShoppingCartPage.PRODUCT_MODEL).text

    def get_unit_price(self) -> str:
        return self._product.find_element(*LocatorsShoppingCartPage.PRODUCT_UNIT_PRICE).text

    def get_total_price(self) -> str:
        return self._product.find_element(*LocatorsShoppingCartPage.PRODUCT_TOTAL_PRICE).text

    def get_quantity(self) -> str:
        return self._product.find_element(*LocatorsShoppingCartPage.PRODUCT_QUANTITY).get_attribute('value')

    def set_quantity(self, value: int):
        quantity_input = self._product.find_element(*LocatorsShoppingCartPage.PRODUCT_QUANTITY)
        quantity_input.clear()
        quantity_input.send_keys(value)

    def click_update_button(self) -> None:
        self._product.find_element(*LocatorsShoppingCartPage.PRODUCT_UPDATE_QUANTITY_BUTTON).click()

    def click_remove_button(self) -> None:
        self._product.find_element(*LocatorsShoppingCartPage.PRODUCT_REMOVE_BUTTON).click()
