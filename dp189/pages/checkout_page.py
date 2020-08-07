"""Module for the 'Checkout' page."""

from selenium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from dp189.components import InputFieldComponent, YourPersonalDetailsComponent, AddAddressComponent, \
    YourPasswordComponent
from dp189.locators import LocatorsCheckoutPage

from dp189.pages.base_page import BasePage

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

    def click_register_account_radio_button(self) -> None:
        """Click on the 'Register Account' radio button.

        :return: None
        """
        register_account_radio_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.REGISTER_CHECKOUT_RADIO_BUTTON))
        register_account_radio_button.click()

    def click_guest_checkout_radio_button(self) -> None:
        """Click on the 'Guest Checkout' radio button.

        :return: None
        """
        guest_checkout_radio_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.GUEST_CHECKOUT_RADIO_BUTTON))
        guest_checkout_radio_button.click()

    def click_continue_button(self) -> None:
        """Click on the 'Continue' button.

        :return: None
        """
        continue_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.CHECKOUT_OPTIONS_CONTINUE_BUTTON))
        continue_button.click()

    def click_forgotten_password_link(self) -> None:
        """Click on the 'Forgotten Password' link.

        :return: None
        """
        forgotten_password_link = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.FORGOTTEN_PASSWORD_LINK))
        forgotten_password_link.click()

    def click_login_button(self) -> None:
        """Click on the 'Login' button.

        :return: None
        """
        login_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.LOGIN_BUTTON))
        login_button.click()


class BillingDetails:
    """'Billing details' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver
        self.your_personal_details_form = YourPersonalDetailsComponent(self._driver,
                                                                       self.get_your_personal_details_form())
        self.your_address_form = AddAddressComponent(self._driver, self.get_your_personal_details_form())

    def get_your_personal_details_form(self):
        """Load the 'Your Personal Details' form.

        :return: None
        """
        return WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(LocatorsCheckoutPage.YOUR_ADDRESS_ACCOUNT_AND_BILLING_DETAILS_PARENT))

    def click_continue_button_billing_details(self) -> None:
        """Click on the 'Continue' button.

        :return: None
        """
        continue_button_billing_details = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.BILLING_DETAILS_CONTINUE_BUTTON))
        continue_button_billing_details.click()

    def click_delivery_and_billing_addresses_checkbox(self) -> None:
        """Click on the 'My delivery and billing addresses are the same.' checkbox.

        :return: None
        """
        delivery_and_billing_addresses_checkbox = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.DELIVERY_AND_BILLING_ADDRESSES_CHECKBOX))
        delivery_and_billing_addresses_checkbox.click()


class AccountAndBillingDetails:
    """'Account and billing details' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver
        self.your_personal_details_form = YourPersonalDetailsComponent(self._driver,
                                                                       self.get_your_personal_details_form())
        self.your_password_form = YourPasswordComponent(self._driver, self.get_your_personal_details_form())
        self.your_address_from = AddAddressComponent(self._driver, self.get_your_personal_details_form())

    def get_your_personal_details_form(self) -> WebElement:
        """Load the 'Your Personal Details' form.

        :return: WebElement
        """
        return WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located(LocatorsCheckoutPage.YOUR_ADDRESS_ACCOUNT_AND_BILLING_DETAILS_PARENT))

    def click_newsletter_checkbox(self) -> None:
        """Click on the 'I wish to subscribe to the Your Store newsletter.' checkbox.

        :return: None
        """
        newsletter_checkbox = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.NEWSLETTER_CHECKBOX))
        newsletter_checkbox.click()

    def click_delivery_and_billing_addresses_checkbox(self) -> None:
        """Click on the 'My delivery and billing addresses are the same.' checkbox.

        :return: None
        """
        delivery_and_billing_addresses_checkbox = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.DELIVERY_AND_BILLING_ADDRESSES_CHECKBOX))
        delivery_and_billing_addresses_checkbox.click()

    def click_privacy_policy_checkbox(self) -> None:
        """Click on the 'I have read and agree to the Privacy Policy' checkbox.

        :return: None
        """
        privacy_policy_checkbox = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.PRIVACY_POLICY_CHECKBOX))
        privacy_policy_checkbox.click()

    def click_continue_button(self) -> None:
        """Click on the 'Continue' button.

        :return: None
        """
        continue_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.ACCOUNT_AND_BILLING_DETAILS_CONTINUE_BUTTON))
        continue_button.click()


class DeliveryDetails:
    """'Delivery details' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver
        self._form_parent_element = self._driver.find_element(*LocatorsCheckoutPage.DELIVERY_DETAILS_PARENT)
        self.delivery_details = AddAddressComponent(self._driver, self._form_parent_element)

    def click_continue_button(self) -> None:
        """Click on the 'Continue' button.

        :return: None
        """
        continue_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.DELIVERY_DETAILS_CONTINUE_BUTTON))
        continue_button.click()


class DeliveryMethod:
    """'Delivery method' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver

    def fill_delivery_method_text_area(self) -> None:
        """Fill in the 'Add Comments About Your Order' field.

        :return: None
        """
        InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_METHOD_TEXT_AREA)

    def click_continue_button(self) -> None:
        """Click on the 'Continue' button.

        :return: None
        """
        continue_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.DELIVERY_METHOD_CONTINUE_BUTTON))
        continue_button.click()


class PaymentMethod:
    """'Payment method' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver

    def fill_payment_method_text_area(self) -> None:
        """Fill in the 'Add Comments About Your Order' field.

        :return: None
        """
        InputFieldComponent(self._driver, LocatorsCheckoutPage.PAYMENT_METHOD_TEXT_AREA)

    def click_terms_and_conditions_checkbox(self) -> None:
        """Click on the 'I have read and agree to the Terms & Conditions' checkbox.

        :return: None
        """
        terms_and_conditions = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.TERMS_AND_CONDITIONS_CHECKBOX))
        terms_and_conditions.click()

    def click_continue_button(self) -> None:
        """Clcik on the 'Continue' button.

        :return: None
        """
        continue_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.PAYMENT_METHOD_CONTINUE_BUTTON))
        continue_button.click()


class ConfirmOrder:
    """'Confirm order' tab class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize the class.

        :param driver: Remote.
        """
        self._driver = driver

    def click_confirm_order_button(self) -> None:
        """Click on the 'Confirm Order' button.

        :return: None
        """
        confirm_order_button = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable(LocatorsCheckoutPage.CONFIRM_ORDER_BUTTON))
        confirm_order_button.click()
