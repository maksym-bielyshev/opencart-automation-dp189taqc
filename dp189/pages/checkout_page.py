"""Module for the 'Checkout' page."""

from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.locators import LocatorsCheckoutPage
from dp189.components import InputFieldComponent, YourPersonalDetailsComponent, AddAddressComponent, \
    YourPasswordComponent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):
    """Main class for the all class instances."""

    def __init__(self, driver: Remote) -> None:
        """Initialize main class.

        :param driver: Remote.
        """
        super().__init__(driver)
        self.open_checkout_options = CheckoutOptions(self._driver)
        self.open_billing_details = BillingDetails(self._driver)
        self.open_account_billing_details = AccountAndBillingDetails(self._driver)
        self.open_delivery_details = DeliveryDetails(self._driver)
        self.open_delivery_method = DeliveryMethod(self._driver)
        self.open_payment_method = PaymentMethod(self._driver)
        self.open_confirm_order = ConfirmOrder(self._driver)


class CheckoutOptions:
    """'Checkout options' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver
        self.email_field_returning_customer = \
            InputFieldComponent(self._driver, LocatorsCheckoutPage.RETURNING_CUSTOMER_EMAIL_FIELD)
        self.password_field_returning_customer = \
            InputFieldComponent(self._driver, LocatorsCheckoutPage.RETURNING_CUSTOMER_PASSWORD_FIELD)

    def click_checkout_options_form(self) -> None:
        self._driver.find_element(LocatorsCheckoutPage.CHECKOUT_OPTIONS_FORM).click()

    def click_register_account_radio_button(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.REGISTER_CHECKOUT_RADIO_BUTTON).click()

    def click_guest_checkout_radio_button(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.GUEST_CHECKOUT_RADIO_BUTTON).click()

    def click_continue_button(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.CHECKOUT_OPTIONS_CONTINUE_BUTTON).click()

    def click_forgotten_password_link(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.FORGOTTEN_PASSWORD_LINK).click()

    def click_login_button(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.LOGIN_BUTTON).click()


class BillingDetails:
    """'Billing details' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver
        self.your_personal_details_form_container = \
            self._driver.find_element(*LocatorsCheckoutPage.YOUR_ADDRESS_ACCOUNT_AND_BILLING_DETAILS_PARENT)
        self.your_personal_details_form = YourPersonalDetailsComponent(self._driver,
                                                                       self.your_personal_details_form_container)
        self.your_address_form = AddAddressComponent(self._driver, self.your_personal_details_form_container)

    def click_continue_button_billing_details(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.BILLING_DETAILS_CONTINUE_BUTTON).click()

    def click_delivery_and_billing_addresses_checkbox(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.DELIVERY_AND_BILLING_ADDRESSES_CHECKBOX).click()


class AccountAndBillingDetails:
    """'Account and billing details' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver
        self.your_form_container = self._driver.\
            find_element(*LocatorsCheckoutPage.YOUR_ADDRESS_ACCOUNT_AND_BILLING_DETAILS_PARENT)
        self.your_personal_details_form = YourPersonalDetailsComponent(self._driver, self.your_form_container)
        self.your_password_form = YourPasswordComponent(self._driver, self.your_form_container)
        self.your_address_from = AddAddressComponent(self._driver, self.your_form_container)

    def click_newsletter_checkbox(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.NEWSLETTER_CHECKBOX).click()

    def click_delivery_and_billing_addresses_checkbox(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.DELIVERY_AND_BILLING_ADDRESSES_CHECKBOX).click()

    def click_privacy_policy_checkbox(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.PRIVACY_POLICY_CHECKBOX).click()

    def click_continue_button(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.ACCOUNT_AND_BILLING_DETAILS_CONTINUE_BUTTON).click()


class DeliveryDetails:
    """'Delivery details' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver
        self._form_parent_element = self._driver.find_element(*LocatorsCheckoutPage.DELIVERY_DETAILS_PARENT)
        self.delivery_details = AddAddressComponent(self._driver, self._form_parent_element)

    def click_continue_button(self):
        continue_button = WebDriverWait(self._driver, 5). \
            until(EC.presence_of_element_located(LocatorsCheckoutPage.DELIVERY_DETAILS_CONTINUE_BUTTON))
        continue_button.click()


class DeliveryMethod:
    """'Delivery method' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver

    def fill_delivery_method_text_area(self) -> None:
        InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_METHOD_TEXT_AREA)

    def click_continue_button(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.DELIVERY_METHOD_CONTINUE_BUTTON).click()


class PaymentMethod:
    """'Payment method' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver

    def fill_payment_method_text_area(self) -> None:
        InputFieldComponent(self._driver, LocatorsCheckoutPage.PAYMENT_METHOD_TEXT_AREA)

    def click_terms_and_conditions_checkbox(self) -> None:
        terms_and_conditions = WebDriverWait(self._driver, 5).\
            until(EC.presence_of_element_located(LocatorsCheckoutPage.TERMS_AND_CONDITIONS_CHECKBOX))
        terms_and_conditions.click()

    def click_continue_button(self) -> None:
        self._driver.find_element(*LocatorsCheckoutPage.PAYMENT_METHOD_CONTINUE_BUTTON).click()


class ConfirmOrder:
    """'Confirm order' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver

    def click_confirm_order_button(self) -> None:
        confirm_order_button = WebDriverWait(self._driver, 5). \
            until(EC.presence_of_element_located(LocatorsCheckoutPage.CONFIRM_ORDER_BUTTON))
        confirm_order_button.click()
