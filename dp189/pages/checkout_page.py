from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.locators import LocatorsCheckoutPage
from dp189.components import InputFieldComponent


class CheckoutOptions(BasePage):
    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self._driver = driver
        self.email_field_returning_customer = \
            InputFieldComponent(self._driver, LocatorsCheckoutPage.EMAIL_FIELD_RETURNING_CUSTOMER)
        self.password_field_returning_customer = \
            InputFieldComponent(self._driver, LocatorsCheckoutPage.PASSWORD_FIELD_RETURNING_CUSTOMER)

    def click_register_account_radio_button(self):
        self._driver.find_element(LocatorsCheckoutPage.REGISTER_ACCOUNT_RADIO_BUTTON).click()

    def click_guest_checkout_radio_button(self):
        self._driver.find_element(LocatorsCheckoutPage.GUEST_CHECKOUT_RADIO_BUTTON).click()

    def click_continue_button(self):
        self._driver.find_element(LocatorsCheckoutPage.CONTINUE_BUTTON).click()

    def click_forgotten_password_link(self):
        self._driver.find_element(LocatorsCheckoutPage.FORGOTTEN_PASSWORD_LINK).click()

    def click_login_button(self):
        self._driver.find_element(LocatorsCheckoutPage.LOGIN_BUTTON).click()


class BillingDetails:
    def __init__(self, driver: Remote) -> None:
        self._driver = driver


class AccountAndBillingDetails:
    def __init__(self, driver: Remote) -> None:
        self._driver = driver


class DeliveryDetails:
    def __init__(self, driver: Remote) -> None:
        self._driver = driver


class DeliveryMethod:
    def __init__(self, driver: Remote) -> None:
        self._driver = driver


class PaymentMethod:
    def __init__(self, driver: Remote) -> None:
        self._driver = driver


class ConfirmOrder:
    def __init__(self, driver: Remote) -> None:
        self._driver = driver
