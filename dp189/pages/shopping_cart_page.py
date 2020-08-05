import re
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from dp189.components import InputFieldComponent, DropdownComponent, RadioButtonComponent
from dp189.pages.base_page import BasePage
from dp189.locators import LocatorsShoppingCartPage
from dp189.pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPage(BasePage):
    """This class describes methods that we need to work with 'Shopping Cart' page."""
    def __init__(self, driver: Remote):
        """Initialize driver and objects to works with 'Shopping Cart' page..

        :param driver: Remote
        """
        super().__init__(driver)
        self.coupon_panel = CouponPanel(driver)
        self.estimate_shipping_panel = EstimateShippingPanel(driver)
        self.gift_certificate_panel = GiftCertificatePanel(driver)
        self.products_list = []

    def generate_products_list(self) -> list:
        """Fills product_list with ProductInCart class instances.
        This method must be called before you start working with product methods.

        :return: ProductInCart class instances list
        """
        product_lines = self._driver.find_elements(*LocatorsShoppingCartPage.PRODUCT_LINES)
        for product in product_lines:
            self.products_list.append(ProductInCart(product, self._driver))
        return self.products_list

    def get_products_name_list(self) -> list:
        """Creates list filled by product names in cart.

        :return: products list
        """
        products_name_list = []
        for product in self.products_list:
            products_name_list.append(product.get_name())
        return products_name_list

    def get_product_quantity(self, product_name: str) -> str:
        """Gets product unit price found by product name.

        :param product_name: string
        :return: string
        """
        for product in self.products_list:
            if product.get_name() == product_name:
                return product.get_quantity()

    def get_product_unit_price(self, product_name: str) -> float:
        """Gets product unit price found by product name.

        :param product_name: string
        :return: float
        """
        for product in self.products_list:
            if product.get_name() == product_name:
                return product.get_unit_price()

    def get_product_total_price(self, product_name: str) -> float:
        """Gets product total price found by product name.

        :param product_name: string
        :return: float
        """
        for product in self.products_list:
            if product.get_name() == product_name:
                return product.get_total_price()

    def change_product_quantity(self, product_name: str, product_quantity: str) -> object:
        """Changes product quantity found by product name.

        :param product_name: string
        :param product_quantity: string
        :return: ShoppingCartPage: object
        """
        for product in self.products_list:
            if product.get_name() == product_name:
                product.quantity.clear_and_fill_input_field(product_quantity)
                product.click_update_button()
                return ShoppingCartPage(self._driver)

    def click_remove_product_button(self, product_name: str) -> None:
        """Removes some product from cart found by product name.

        :param product_name: string
        :return: None
        """
        for product in self.products_list:
            if product.get_name() == product_name:
                product.click_remove_button()
                self.products_list.remove(product)

    def click_continue_shipping_button(self) -> object:
        """Click 'Continue Shopping' button.

        :return: HomePage object
        """
        self._driver.find_element(*LocatorsShoppingCartPage.CONTINUE_SHIPPING_BUTTON).click()
        return HomePage(self._driver)

    def click_checkout_button(self) -> object:
        """Click 'Checkout' button.

        :return: CheckoutPage object
        """
        self._driver.find_element(*LocatorsShoppingCartPage.CHECKOUT_BUTTON).click()
        # return CheckoutPage(self._driver)

    def get_flat_shipping_rate(self) -> float:
        """Gets 'Flat Shipping Rate' sum.

        :return: float
        """
        return self._cut_number(self._driver.find_element(*LocatorsShoppingCartPage.FLAT_SHIPPING_RATE))

    def get_coupon_sum(self) -> float:
        """Gets 'Coupon' sum.

        :return: float
        """
        return self._cut_number(self._driver.find_element(*LocatorsShoppingCartPage.COUPON_SUM))

    def get_gift_certificate_sum(self) -> float:
        """Gets 'Gift Certificate' sum.

        :return: float
        """
        return self._cut_number(self._driver.find_element(*LocatorsShoppingCartPage.GIFT_CERTIFICATE_SUM))

    def get_sub_total_sum(self) -> float:
        """Gets 'Sub-Total' sum.

        :return: float
        """
        return self._cut_number(self._driver.find_element(*LocatorsShoppingCartPage.SUB_TOTAL_ORDER_SUM))

    def get_total_sum(self) -> float:
        """Gets 'Total' sum.

        :return: float
        """
        return self._cut_number(self._driver.find_element(*LocatorsShoppingCartPage.TOTAL_ORDER_SUM))

    def get_text_empty_cart(self) -> str:
        """Gets content empty cart.

        :return: string content text
        """
        cart_message = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located(LocatorsShoppingCartPage.CONTENT_EMPTY_CART)
        )
        return cart_message.text

    @staticmethod
    def _cut_number(web_text: WebElement) -> float:
        """Cuts number from string to return float without other symbols.
        
        :param web_text: WebElement
        :return: float
        """""
        return float(''.join(re.findall(r'\d+\.\d+', web_text.text)))


class CouponPanel:
    """This class describes methods that we need to work with 'Coupon' panel"""
    def __init__(self, driver: Remote):
        """Initialize driver and coupon_field to work with 'Coupon' panel.

        :param driver: Remote
        """
        self._driver = driver
        self.coupon_field = InputFieldComponent(self._driver, LocatorsShoppingCartPage.COUPON_FIELD)

    def open_coupon_panel(self) -> None:
        """Click on 'Use Coupon Code' panel to open it.

        :return: None
        """
        self._driver.find_element(*LocatorsShoppingCartPage.COUPON_PANEL).click()

    def click_apply_coupon_button(self) -> None:
        """Click 'Apply Coupon' button.

        :return: None
        """
        self._driver.find_element(*LocatorsShoppingCartPage.COUPON_APPLY_BUTTON).click()


class EstimateShippingPanel:
    """This class describes methods that we need to work with 'Estimate Shipping & Taxes' panel"""
    def __init__(self, driver: Remote):
        """Initialize driver and other field, selectors, radiobutton to work with 'Estimate Shipping & Taxes' panel
        and it`s modal window.

        :param driver: Remote
        """
        self._driver = driver
        self.post_code_field = InputFieldComponent(self._driver, LocatorsShoppingCartPage.POST_CODE_FIELD)
        self.country_selector = DropdownComponent(self._driver, LocatorsShoppingCartPage.COUNTRY_SELECTOR)
        self.region_selector = DropdownComponent(self._driver, LocatorsShoppingCartPage.REGION_SELECTOR)
        self.modal_shipping_radio_button = RadioButtonComponent(self._driver,
                                                                LocatorsShoppingCartPage.MODAL_SHIPPING_RADIO)

    def open_estimate_shipping_panel(self) -> None:
        """Click on 'Estimate Shipping & Taxes' panel to open it.

        :return: None
        """
        self._driver.find_element(*LocatorsShoppingCartPage.ESTIMATE_SHIPPING_PANEL).click()

    def click_get_quotes_button(self) -> None:
        """Click on 'Get Quotes' button.

        :return: None
        """
        self._driver.find_element(*LocatorsShoppingCartPage.GET_QUOTES_BUTTON).click()

    def click_modal_shipping_cancel_button(self) -> None:
        """Click 'Cancel' button in modal window.

        :return: None
        """
        self._driver.find_element(*LocatorsShoppingCartPage.MODAL_SHIPPING_CANCEL_BUTTON).click()

    def click_modal_apply_shipping_button(self) -> None:
        """Click 'Apply Shipping' button in modal window.

        :return: None
        """
        self._driver.find_element(*LocatorsShoppingCartPage.MODAL_SHIPPING_APPlY_BUTTON).click()


class GiftCertificatePanel:
    """This class describes methods that we need to work with 'Gift Certificate' panel"""
    def __init__(self, driver: Remote):
        """Initialize driver, gift_certificate_field to work with 'Gift Certificate' panel.

        :param driver: Remote
        """
        self._driver = driver
        self.gift_certificate_field = InputFieldComponent(self._driver, LocatorsShoppingCartPage.CERTIFICATE_FIELD)

    def open_gift_certificate_panel(self) -> None:
        """Click on 'Use Gift Certificate' panel to open it.

        :return: None
        """
        self._driver.find_element(*LocatorsShoppingCartPage.GIFT_CERTIFICATE_PANEL).click()

    def click_apply_gift_certificate_button(self) -> None:
        """Click on 'Apply Gift Certificate' button.

        :return: None
        """
        self._driver.find_element(*LocatorsShoppingCartPage.CERTIFICATE_APPLY_BUTTON).click()


class ProductInCart:
    """This class describes methods that we need to work with separate product in cart."""
    def __init__(self, product_line: WebElement, driver: Remote):
        """Initialize driver, parent WebElement and product quantity to work with separate product in cart.

        :param product_line: WebElement
        :param driver: Remote
        """
        self._driver = driver
        self._product_line = product_line
        self.quantity = InputFieldComponent(self._driver,
                                            LocatorsShoppingCartPage.PRODUCT_QUANTITY, self._product_line)

    def get_name(self) -> str:
        """Gets product name.

        :return: string
        """
        return self._product_line.find_element(*LocatorsShoppingCartPage.PRODUCT_NAME).text

    def get_model(self) -> str:
        """Gets product model.

        :return: string
        """
        return self._product_line.find_element(*LocatorsShoppingCartPage.PRODUCT_MODEL).text

    def get_unit_price(self) -> float:
        """Gets product unit price.

        :return: float
        """
        return self._cut_number(self._product_line.find_element(*LocatorsShoppingCartPage.PRODUCT_UNIT_PRICE))

    def get_total_price(self) -> float:
        """Gets product total price.

        :return: float
        """
        return self._cut_number(self._product_line.find_element(*LocatorsShoppingCartPage.PRODUCT_TOTAL_PRICE))

    def get_quantity(self) -> str:
        """Gets product quantity.

        :return: string
        """
        return self._product_line.find_element(*LocatorsShoppingCartPage.PRODUCT_QUANTITY).get_attribute('value')

    def click_update_button(self) -> None:
        """Click update product quantity button.

        :return: None
        """
        self._product_line.find_element(*LocatorsShoppingCartPage.PRODUCT_UPDATE_QUANTITY_BUTTON).click()

    def click_remove_button(self) -> None:
        """Click remove product from cart button.

        :return: None
        """
        self._product_line.find_element(*LocatorsShoppingCartPage.PRODUCT_REMOVE_BUTTON).click()

    @staticmethod
    def _cut_number(web_text: WebElement) -> float:
        """Cuts number from string to return float without other symbols.

        :param path: WebElement
        :return: float
        """""
        return float(''.join(re.findall(r'\d+\.\d+', web_text.text)))