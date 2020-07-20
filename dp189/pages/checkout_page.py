from selenium.webdriver import Remote
from dp189.locators import LocatorsCheckoutPage


class CheckoutOptions:
    def __init__(self, driver: Remote) -> None:
        self._driver = driver

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
