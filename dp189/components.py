from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from .locators import LocatorsShoppingCartButton, LocatorsYourPersonalDetailsComponent, \
    LocatorsYourPasswordComponent, LocatorsNewsletterComponent, LocatorsAddAddressComponent, \
    LocatorsBasePageNavBar, LocatorsRightMenuRegisterPage, LocatorProductCompareLink, \
    LocatorsViewModeButton, LocatorProductWidget, LocatorsInfoMessages, LocatorsAvailableOptions, \
    LocatorsPrivacyPolicyComponent, LocatorsLoginComponent


class ShopCartButtonComponent:
    # TODO test functionality
    def __init__(self, driver):
        self._driver = driver
        self._shop_cart_button = driver.find_element(*LocatorsShoppingCartButton.SHOP_CART_BUTTON)

    def click_shop_cart_button(self):
        self._shop_cart_button.click()
        cart_items = self._driver.find_elements(*LocatorsShoppingCartButton.CART_ITEMS)
        if len(cart_items) == 0:
            return 'Your cart is empty!'
        else:
            return ShopCartDropdownComponent(self._driver)


class ShopCartDropdownComponent:
    """Component for black shopping cart drop-down button."""

    def __init__(self, driver: Remote) -> None:
        """Initialise shopping cart drop-down button.

        :param driver: Remote driver.
        """
        self._driver = driver

    def click_product_title(self, product_title: str) -> None:
        """Click on the provided product title.

        :return: None.
        """
        self._driver.find_element(By.XPATH, f'//*[@id="cart"]//td[2]//a[(text()="{product_title}")]').click()

    def click_remove_button(self, product_title: str) -> None:
        """Click on the remove from the shopping cart button.
            return self._driver

        :return: None.
        """
        product_title = self._driver.find_element(By.XPATH, f'//*[@id="cart"]//td[2]//a[(text()="{product_title}")]')
        self._driver.find_element(By.XPATH, f'{product_title}/../../td[5]/button').click()

    def click_view_cart_link(self) -> None:
        """Click on the 'View Cart' link.

        :return: None.
        """
        self._driver.find_element(*LocatorsShoppingCartButton.VIEW_CART).click()

    def click_checkout_link(self) -> None:
        """Click on the 'Checkout' link.

        :return: None.
        """
        self._driver.find_element(*LocatorsShoppingCartButton.CHECKOUT).click()


class BasePageNavBarComponent:
    """This class describes the top nav bar of the base page"""

    def __init__(self, driver):
        self._driver = driver
        self.nav_bar = self.wait_load_nav_bar()

    def wait_load_nav_bar(self):
        return WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(LocatorsBasePageNavBar.NAVBAR)
        )

    def change_currency(self, specific_currency: str):
        # """EUR, USD, GBP"""
        currency_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(LocatorsBasePageNavBar.CURRENCY)
        )
        currency_button.click()
        self._driver.find_element(By.XPATH, f"//button[@name='{specific_currency}']").click()

    def click_contact_us_link(self):
        self.nav_bar.find_element(*LocatorsBasePageNavBar.CONTACT_US).click()

    def click_wishlist_link(self):
        self.nav_bar.find_element(*LocatorsBasePageNavBar.WISH_LIST).click()

    def click_shopping_cart_link(self):
        self.nav_bar.find_element(*LocatorsBasePageNavBar.SHOPPING_CART).click()

    def click_checkout_link(self):
        self.nav_bar.find_element(*LocatorsBasePageNavBar.CHECKOUT).click()


class RegisterPageRightMenuComponent:
    def __init__(self, driver) -> None:
        self._driver = driver
        self._right_menu = driver.find_element_by_class_name('list-group')

    def click_my_account(self):
        self._right_menu.find_element(*LocatorsRightMenuRegisterPage.MY_ACCOUNT).click()

    def click_address_book(self):
        self._right_menu.find_element(*LocatorsRightMenuRegisterPage.ADDRESS_BOOK).click()

    def click_wish_list(self):
        self._right_menu.find_element(*LocatorsRightMenuRegisterPage.WISH_LIST).click()

    def click_order_history(self):
        self._right_menu.find_element(*LocatorsRightMenuRegisterPage.ORDER_HISTORY).click()

    def click_downloads(self):
        self._right_menu.find_element(*LocatorsRightMenuRegisterPage.DOWNLOADS).click()

    def click_recurring_payments(self):
        self._right_menu.find_element(*LocatorsRightMenuRegisterPage.RECURRING_PAYMENTS).click()

    def click_reward_points(self):
        self._right_menu.find_element(*LocatorsRightMenuRegisterPage.REWARD_POINTS).click()

    def click_returns(self):
        self._right_menu.find_element(*LocatorsRightMenuRegisterPage.RETURNS).click()

    def click_transactions(self):
        self._right_menu.find_element(*LocatorsRightMenuRegisterPage.TRANSACTIONS).click()

    def click_newsletter(self):
        self._right_menu.find_element(*LocatorsRightMenuRegisterPage.NEWSLETTER).click()


class ProductWidgetsListComponent:
    """All products on the 'Category' page."""

    def __init__(self, driver: Remote):
        """Initialise a driver and an empty list.

        :param driver: Remote driver.
        """
        self._driver = driver
        self.product_widgets_list = []

    def get_list_product_widgets(self) -> list:
        """Get a list of all products on the 'Category' page.

        :return: List of all products on the 'Category' page.
        """
        self.product_widgets_list = self._driver.find_elements(*LocatorProductWidget.PRODUCT_WIDGET)
        return self.product_widgets_list


class ProductWidgetComponent:
    """Widget for products on the category page."""

    def __init__(self, driver: Remote, product_title: str) -> None:
        """Initialise the widget and the buttons.

        :param driver: Remote driver.
        :param product_title: The title of the product.
        """
        self._driver = driver
        self.product_title = product_title

    def click_add_to_shopping_cart_button(self) -> None:
        """Click on the "Add to shopping cart" button.

        :return: None.
        """
        self._driver.find_element \
            (By.XPATH, f'//a[text()="{self.product_title}"]/../../..//span[text()="Add to Cart"]/..').click()

    def click_add_to_wish_list_button(self) -> None:
        """Click on the "Add to Wish List" button.

        :return: None.
        """
        self._driver.find_element(
            By.XPATH,
            f'//a[text()="{self.product_title}"]/../../..//button[@data-original-title ="Add to Wish List"]').click()

    def click_add_to_compare_button(self) -> None:
        """Click on the "Compare this Product" button.

        :return: None.
        """
        self._driver.find_element(
            By.XPATH,
            f'//a[text()="{self.product_title}"]/../../..//button[@data-original-title="Compare this Product"]').click()


class ProductCompareLinkComponent:
    """A link to compare the products added to the comparison."""

    def __init__(self, driver: Remote) -> None:
        """Initialise the link.

        :param driver: Remote driver.
        """
        self._driver = driver

    def open_compare_page(self) -> None:
        """Click on the 'Product Compare' link.

        :return: None.
        """
        self._driver.find_element(*LocatorProductCompareLink.PRODUCT_COMPARE).click()


class ProductsViewModeComponent:
    """Two buttons to change the view of the products."""

    def __init__(self, driver: Remote) -> None:
        self._driver = driver

    def click_list_view_button(self) -> None:
        """Click on the 'List' button.

        :return: None.
        """
        self._driver.find_element(*LocatorsViewModeButton.LIST_VIEW_BUTTON).click()

    def click_grid_view_button(self) -> None:
        """Click on the 'Grid' button.

        :return: None.
        """
        self._driver.find_element(*LocatorsViewModeButton.GRID_VIEW_BUTTON).click()


class YourPersonalDetailsComponent:
    """Your personal details form сonsists four fields to fill first name, last name, email, telephone."""

    def __init__(self, driver: Remote, parent_element: WebElement) -> None:
        """Initialize input fields first name, last name, email, telephone.

        :param driver: Remote.
        :param parent_element: WebElement
        """
        self._driver = driver
        self._parent_element = parent_element
        self.first_name_field = InputFieldComponent(self._driver,
                                                    LocatorsYourPersonalDetailsComponent.FIRST_NAME_FIELD,
                                                    self._parent_element)
        self.last_name_field = InputFieldComponent(self._driver,
                                                   LocatorsYourPersonalDetailsComponent.LAST_NAME_FIELD,
                                                   self._parent_element)
        self.email_field = InputFieldComponent(self._driver,
                                               LocatorsYourPersonalDetailsComponent.EMAIL_FIELD,
                                               self._parent_element)
        self.telephone_field = InputFieldComponent(self._driver,
                                                   LocatorsYourPersonalDetailsComponent.TELEPHONE_FIELD,
                                                   self._parent_element)


class YourPasswordComponent:
    """Your password form сonsists two fields to fill password, password confirm."""

    def __init__(self, driver: Remote, parent_element: WebElement) -> None:
        """Initialize input fields password field, password confirm field.

        :param driver: Remote
        :param parent_element: WebElement
        :return: None
        """
        self._driver = driver
        self._parent_element = parent_element
        self.password_field = InputFieldComponent(self._driver, LocatorsYourPasswordComponent.PASSWORD_FIELD,
                                                  self._parent_element)
        self.password_confirm_field = InputFieldComponent(self._driver,
                                                          LocatorsYourPasswordComponent.PASSWORD_CONFIRM_FIELD,
                                                          self._parent_element)


class InputFieldComponent:
    """An input field to fill with data from user."""

    def __init__(self, driver: Remote, input_field_locator: tuple, parent_element: WebElement = None) -> None:
        """Initialize the input field.

        :param driver: Remote
        :param input_field_locator: tuple (example: PASSWORD_FIELD=(By.ID, 'input-password'))
        :return: None
        """
        self._driver = driver
        self.input_field_locator = input_field_locator
        self.parent_element = parent_element
        self.error_message = ErrorMessageComponent(self._driver, self.input_field_locator)

    def _find_input_field(self) -> None:
        """Find input field by parent element or driver.

        :return: None
        """
        if self.parent_element:
            self.input_field = self.parent_element.find_element(*self.input_field_locator)
        else:
            self.input_field = self._driver.find_element(*self.input_field_locator)

    def clear_and_fill_input_field(self, data: str) -> None:
        """Clear and fill input field with data.

        :param data: str
        :return: None
        """
        self._find_input_field()
        self.input_field.clear()
        self.input_field.send_keys(data)


class RadioButtonComponent:
    """Radio buttons to choose some option and check which option is chosen."""

    def __init__(self, driver: Remote, radio_buttons_locator: tuple, parent_element: WebElement = None) -> None:
        """Initialize radio buttons.

        :param driver: Remote
        :param radio_buttons_locator: tuple
        :return: None
        """
        self._driver = driver
        self.radio_buttons_locator = radio_buttons_locator
        self.parent_element = parent_element
        self.error_message = ErrorMessageComponent(self._driver, self.radio_buttons_locator)

    def _find_radio_button(self) -> None:
        """Find input field by parent element or driver.

        :return: None
        """
        if self.parent_element:
            self.radio_buttons_container = self.parent_element.find_element(*self.radio_buttons_locator)
        else:
            self.radio_buttons_container = self._driver.find_element(*self.radio_buttons_locator)

    def which_option_is_chosen(self) -> str:
        """Return text of chosen option.

        :return: str
        """
        self._find_radio_button()
        radio_button_labels = self.radio_buttons_container.find_elements(*LocatorsAvailableOptions.RADIO_BUTTON_LABEL)
        for label in radio_button_labels:
            radio_button_input = label.find_element(By.TAG_NAME, 'input')
            if radio_button_input.get_attribute('checked'):
                return label.text

    def choose_radio_button_option(self, data: str) -> None:
        """Choose some option. data - string of desired option.

        :param data: str
        :return: None
        """
        self._find_radio_button()
        self.radio_buttons_container.find_element(By.XPATH, f'//label[contains(.,"{data}")]/input').click()


class CheckboxComponent:
    """Checkbox to choose option and check which option is chosen."""

    def __init__(self, driver: Remote, checkbox_locator: tuple, parent_element: WebElement = None) -> None:
        """Initialize checkbox.

        :param driver: Remote
        :param checkbox_locator: tuple
        :return: None
        """
        self._driver = driver
        self.checkbox_locator = checkbox_locator
        self.parent_element = parent_element
        self.error_message = ErrorMessageComponent(self._driver, self.checkbox_locator)

    def _find_checkbox(self):
        """Find input field by parent element or driver.

        :return: None
        """
        if self.parent_element:
            self.checkbox_container = self.parent_element.find_element(*self.checkbox_locator)
        else:
            self.checkbox_container = self._driver.find_element(*self.checkbox_locator)

    def which_option_is_chosen(self) -> list:
        """Return list which consists text of desired options.

        :return: list
        """
        self._find_checkbox()
        choosen_options = list()
        checkbox_labels = self.checkbox_container.find_elements(*LocatorsAvailableOptions.CHECKBOX_LABEL)
        for label in checkbox_labels:
            checkbox_input = label.find_element(By.TAG_NAME, 'input')
            if checkbox_input.get_attribute('checked'):
                choosen_options.append(label.text)
        return choosen_options

    def choose_checkbox_option(self, data: str) -> None:
        """Choose some option.

        :param data: str
        :return: None
        """
        self._find_checkbox()
        self.checkbox_container.find_element(By.XPATH, f'//label[contains(.,"{data}")]/input').click()


class DropdownComponent:
    """Drop-down menu to choose option and check which option is chosen."""

    def __init__(self, driver: Remote, dropdown_locator: tuple, parent_element: WebElement = None) -> None:
        """Initialize drop-down.

        :param driver: Remote
        :param dropdown_locator: tuple
        :return: None
        """
        self._driver = driver
        self.dropdown_locator = dropdown_locator
        self.parent_element = parent_element
        self.error_message = ErrorMessageComponent(self._driver, self.dropdown_locator)

    def _find_dropdown(self):
        """Find input field by parent element or driver.

        :return: None
        """
        WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable(self.dropdown_locator))
        if self.parent_element:
            self.checkbox_container = Select(self.parent_element.find_element(*self.dropdown_locator))
        else:
            self.checkbox_container = Select(self._driver.find_element(*self.dropdown_locator))

    def which_option_is_chosen(self) -> str:
        """Return text of chosen option.

        :return: str
        """
        self._find_dropdown()
        return self.checkbox_container.first_selected_option.text

    def choose_dropdown_option(self, data: str) -> None:
        """Choose some option.

        :param data: str
        :return: None
        """
        self._find_dropdown()
        self.checkbox_container.select_by_visible_text(data)


class ErrorMessageComponent:
    """Error message for input fields, radio buttons, checkboxes, drop-down menus and date, time input fields."""

    def __init__(self, driver: Remote, element_locator: tuple) -> None:
        """Initialize element locator to find error message for it.

        :param driver: Remote
        :param element_locator: tuple
        :return: None
        """
        self._driver = driver
        self.element_locator = element_locator

    def get_error_message(self):
        """Get error message. If there is no error message, None will be returned.
        This method has other error message locator for Date input and Time input fields.

        :return: str or None
        """
        try:
            if '@data-date-format' in self.element_locator[1]:
                error_message_locator = f'{self.element_locator[1]}/../following-sibling::div[@class="text-danger"]'
            else:
                error_message_locator = f'{self.element_locator[1]}/following-sibling::div[@class="text-danger"]'

            error_message = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, error_message_locator))
            )
            return error_message.text
        except TimeoutException:
            return ''


class CatchPageTitleComponent:
    """This component created to get title of current page"""

    def __init__(self, driver: Remote) -> None:
        self._driver = driver

    def get_title_page(self, page_title: str):
        """This method gets title page until it loads

        :return: str
        """
        WebDriverWait(self._driver, 5).until(EC.title_is(page_title))
        return page_title


class CatchMessageComponent:
    """This component created to find a specific info message after action on the site."""

    def __init__(self, driver: Remote) -> None:
        """Initialize a driver to CatchMessageComponent."""
        self._driver = driver

    def get_info_message(self) -> str:
        """Get message such as 'Info:'.

        :returns str"""
        try:
            info_message = WebDriverWait(self._driver, 5).until(
                EC.presence_of_element_located(LocatorsInfoMessages.ALERT_INFO_MESSAGE)
            )
            return info_message.text
        except TimeoutException:
            return ''

    def get_success_message(self) -> str:
        """Get message such as 'Success:'.

        :returns str"""
        try:
            success_message = WebDriverWait(self._driver, 5).until(
                EC.presence_of_element_located(LocatorsInfoMessages.ALERT_SUCCESS_MESSAGE)
            )
            return success_message.text
        except TimeoutException:
            return ''

    def get_danger_message(self) -> str:
        """Get message such as 'Danger:' or 'Warning:'.

        :returns str
        """
        try:
            danger_message = WebDriverWait(self._driver, 5).until(
                EC.presence_of_element_located(LocatorsInfoMessages.ALERT_DANGER_MESSAGE)
            )
            return danger_message.text
        except TimeoutException:
            return ''


class NewsletterComponent:
    """Two radio buttons to subscribe or unsubscribe from newsletter."""

    def __init__(self, driver: Remote) -> None:
        """Initialize driver.

        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.subscribe_radio_button_labels = self._driver.find_elements \
            (*LocatorsNewsletterComponent.SUBSCRIBE_RADIO_BUTTONS)

    def get_subscription_status(self) -> str:
        """Get the status of subscription to newsletters, Yes or No.

        :return: str
        """
        for label in self.subscribe_radio_button_labels:
            subscribe_radio_button_input = label.find_element(By.TAG_NAME, 'input')
            if subscribe_radio_button_input.get_attribute('checked'):
                return label.text

    def subscribe_to_newsletter(self) -> None:
        """Subscribe to newsletter.

        :return: None
        """
        for label in self.subscribe_radio_button_labels:
            subscribe_radio_button_input = label.find_element(By.TAG_NAME, 'input')
            if label.text == 'Yes':
                subscribe_radio_button_input.click()

    def unsubscribe_from_newsletter(self) -> None:
        """Unsubscribe from newsletter.

        :return: None
        """
        for label in self.subscribe_radio_button_labels:
            subscribe_radio_button_input = label.find_element(By.TAG_NAME, 'input')
            if label.text == 'No':
                subscribe_radio_button_input.click()


class PrivacyPolicyComponent:
    """Checkbox Privacy Policy to agree with it."""

    def __init__(self, driver: Remote) -> None:
        """Initialize driver and privacy policy checkbox.

        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.privacy_policy_checkbox_input = self._driver.find_element \
            (*LocatorsPrivacyPolicyComponent.PRIVACY_POLICY_CHECKBOX)

    def agree_with_privacy_policy(self) -> None:
        """Agree with Privacy Policy.

        :return: None
        """
        self.privacy_policy_checkbox_input.click()

    def get_status_privacy_policy(self) -> str:
        """Check status: the user agrees with the policy or not.

        :return: str
        """
        if self.privacy_policy_checkbox_input.get_attribute('checked'):
            return 'I have read and agree to the Privacy Policy.'
        else:
            return 'I don\'t agree to the Privacy Policy.'


class AddAddressComponent:
    """Add Address form сonsists from fields: First Name, Last Name, Company,
    Address 1, Address 2, City, Country, Region."""

    def __init__(self, driver: Remote, parent_element: WebElement) -> None:
        """Initialize input form fields and dropdown form fields.

        :param driver: Remote
        :param parent_element: WebElement
        :return: None
        """
        self._driver = driver
        self._parent_element = parent_element
        self.first_name_field = InputFieldComponent(self._driver,
                                                    LocatorsAddAddressComponent.FIRST_NAME_INPUT, self._parent_element)
        self.last_name_field = InputFieldComponent(self._driver,
                                                   LocatorsAddAddressComponent.LAST_NAME_INPUT, self._parent_element)
        self.email_field = InputFieldComponent(self._driver,
                                               LocatorsAddAddressComponent.EMAIL_INPUT, self._parent_element)
        self.email_field_payment = InputFieldComponent(self._driver,
                                                       LocatorsAddAddressComponent.EMAIL_INPUT_PAYMENT,
                                                       self._parent_element)
        self.telephone_field = InputFieldComponent(self._driver,
                                                   LocatorsAddAddressComponent.TELEPHONE_INPUT, self._parent_element)
        self.company_field = InputFieldComponent(self._driver,
                                                 LocatorsAddAddressComponent.COMPANY_INPUT, self._parent_element)
        self.address_1_field = InputFieldComponent(self._driver,
                                                   LocatorsAddAddressComponent.ADDRESS_1_INPUT, self._parent_element)
        self.address_2_field = InputFieldComponent(self._driver,
                                                   LocatorsAddAddressComponent.ADDRESS_2_INPUT, self._parent_element)
        self.city_field = InputFieldComponent(self._driver,
                                              LocatorsAddAddressComponent.CITY_INPUT, self._parent_element)
        self.post_code_field = InputFieldComponent(self._driver,
                                                   LocatorsAddAddressComponent.POST_CODE_INPUT, self._parent_element)
        self.country = DropdownComponent(self._driver,
                                         LocatorsAddAddressComponent.COUNTRY_SELECTOR, self._parent_element)
        self.region = DropdownComponent(self._driver,
                                        LocatorsAddAddressComponent.REGION_SELECTOR, self._parent_element)


class LoginComponent:
    """Login component consists two fields: E-Mail Address and Password."""

    def __init__(self, driver: Remote) -> None:
        """Initialize input form fields.

        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.email_field = InputFieldComponent(self._driver, LocatorsLoginComponent.EMAIL_INPUT)
        self.password_field = InputFieldComponent(self._driver, LocatorsLoginComponent.PASSWORD_INPUT)

    def click_forgotten_password(self) -> None:
        """Click forgotten password button to restore password.

        :return: None
        """
        self._driver.find_element(*LocatorsLoginComponent.FORGOTTEN_PASSWORD_BUTTON).click()

    def click_login_button(self) -> None:
        """Click login button to return the user to the system.

        :return: None
        """
        self._driver.find_element(*LocatorsLoginComponent.LOGIN_BUTTON).click()
