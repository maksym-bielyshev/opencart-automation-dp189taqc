from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.locators import LocatorsCheckoutPage
from dp189.components import InputFieldComponent, YourPersonalDetailsComponent, AddAddressComponent, YourPasswordComponent


class CheckoutOptions(BasePage):
    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self._driver = driver
        self.email_field_returning_customer = \
            InputFieldComponent(self._driver, LocatorsCheckoutPage.RETURNING_CUSTOMER_EMAIL_FIELD)
        self.password_field_returning_customer = \
            InputFieldComponent(self._driver, LocatorsCheckoutPage.RETURNING_CUSTOMER_PASSWORD_FIELD)

    def click_register_account_radio_button(self):
        self._driver.find_element(LocatorsCheckoutPage.REGISTER_CHECKOUT_RADIO_BUTTON).click()

    def click_guest_checkout_radio_button(self):
        self._driver.find_element(LocatorsCheckoutPage.GUEST_CHECKOUT_RADIO_BUTTON).click()

    def click_continue_button(self):
        self._driver.find_element(LocatorsCheckoutPage.CHECKOUT_OPTIONS_CONTINUE_BUTTON).click()

    def click_forgotten_password_link(self):
        self._driver.find_element(LocatorsCheckoutPage.FORGOTTEN_PASSWORD_LINK).click()

    def click_login_button(self):
        self._driver.find_element(LocatorsCheckoutPage.LOGIN_BUTTON).click()


class BillingDetails:
    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self._driver = driver
        self.your_personal_details_form = YourPersonalDetailsComponent(self._driver)
        self.your_address_form = AddAddressComponent(self._driver, LocatorsCheckoutPage.ADD_ADDRESS_BILLING_DETAILS_PARENT)

    def click_continue_button_billing_details(self):
        self._driver.find_element(LocatorsCheckoutPage.CHECKOUT_OPTIONS_CONTINUE_BUTTON).click()

    def click_delivery_and_billing_addresses_checkbox(self):
        self._driver.find_element(LocatorsCheckoutPage.DELIVERY_AND_BILLING_ADDRESSES_CHECKBOX).click()


class AccountAndBillingDetails:
    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self._driver = driver
        self.your_personal_details_form = YourPersonalDetailsComponent(self._driver)
        self.your_password_form = YourPasswordComponent(self._driver)
        self.your_address_from = AddAddressComponent(self._driver, LocatorsCheckoutPage.YOUR_ADDRESS_ACCOUNT_AND_BILLING_DETAILS_PARENT)

    def click_newsletter_checkbox(self):
        self._driver.find_element(LocatorsCheckoutPage.NEWSLETTER_CHECKBOX).click()

    def click_delivery_and_billing_addresses_checkbox(self):
        self._driver.find_element(LocatorsCheckoutPage.DELIVERY_AND_BILLING_ADDRESSES_CHECKBOX).click()

    def click_privacy_policy_checkbox(self):
        self._driver.find_element(LocatorsCheckoutPage.PRIVACY_POLICY_CHECKBOX).click()

    def click_continue_button(self):
        self._driver.find_element(LocatorsCheckoutPage.ACCOUNT_AND_BILLING_DETAILS_CONTINUE_BUTTON).click()


class DeliveryDetails:
    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self._driver = driver
        self.fill_first_name_field = InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_DETAILS_FIRST_NAME_FIELD)
        self.last_name_field = InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_DETAILS_LAST_NAME_FIELD)
        self.company_field = InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_DETAILS_COMPANY_FIELD)
        self.first_address_field = InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_DETAILS_FIRST_ADDRESS_FIELD)
        self.second_address_field = InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_DETAILS_SECOND_ADDRESS_FIELD)
        self.city_field = InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_DETAILS_CITY_FIELD)
        self.post_code_field = InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_DETAILS_POST_CODE_FIELD)
        self.country_field = InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_DETAILS_COUNTRY_FIELD)
        self.region_state_field = InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_DETAILS_REGION_STATE_DROPDOWN)


class DeliveryMethod:
    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self._driver = driver

    def fill_delivery_method_text_area(self):
        InputFieldComponent(self._driver, LocatorsCheckoutPage.DELIVERY_METHOD_TEXT_AREA)

    def click_continue_button(self):
        self._driver.find_element(LocatorsCheckoutPage.DELIVERY_METHOD_CONTINUE_BUTTON).click()


class PaymentMethod:
    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self._driver = driver

    def fill_payment_method_text_area(self):
        InputFieldComponent(self._driver, LocatorsCheckoutPage.PAYMENT_METHOD_TEXT_AREA)

    def click_terms_and_conditions_checkbox(self):
        self._driver.find_element(LocatorsCheckoutPage.TERMS_AND_CONDITIONS_CHECKBOX).click()

    def click_continue_button(self):
        self._driver.find_element(LocatorsCheckoutPage.PAYMENT_METHOD_CONTINUE_BUTTON).click()


class ConfirmOrder:
    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self._driver = driver

    def click_confirm_order_button(self):
        self._driver.find_element(LocatorsCheckoutPage.CONFIRM_ORDER_BUTTON).click()
