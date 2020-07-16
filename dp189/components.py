from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .locators import LocatorsSearch, LocatorsNavBar, RightMenuLocators, LocatorsShoppingCartButton, \
    LocatorsYourPersonalDetailsComponent, LocatorsYourPasswordComponent, LocatorsRegisterPage, \
    LocatorsNewsletterComponent, LocatorsSearch, LocatorsNavBar, RightMenuLocators, LocatorsShoppingCartButton, \
    LocatorProductCompareLink, LocatorsViewModeButton, LocatorProductWidget


class SearchArea:
    """"This class describes the search area common in all pages. It consists or search field and search button"""

    def __init__(self, driver):
        self._driver = driver
        self._search_field = driver.find_element(*LocatorsSearch.SEARCH_FIELD)
        self._search_button = driver.find_element(*LocatorsSearch.SEARCH_BUTTON)

    def fill_search_field_and_hit_return(self, item: str):
        self._search_field.clear()
        self._search_field.send_keys(item).send_keys(Keys.RETURN)
        # return SearchPage(self._driver)

    def fill_search_field_and_click(self, item: str):
        self._search_field.clear()
        self._search_field.send_keys(item)
        self._search_button.click()
        # return SearchPage(self._driver)


class ShopCartButton:
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

    def __init__(self, driver: Remote, product_title: str) -> None:
        """Initialise shopping cart drop-down button.

        :param driver: Remote driver.
        :param product_title: The title of the product.
        """
        self._driver = driver
        self.product_title = driver.find_element(
            By.XPATH, f'//*[@id="cart"]//td[2]//a[(text()="{product_title}")]')
        self.remove_button = driver.find_element(By.XPATH, f"{self.product_title}/../../td[5]/button")
        self.view_cart_link = driver.find_element(*LocatorsShoppingCartButton.VIEW_CART)
        self.checkout_link = driver.find_element(*LocatorsShoppingCartButton.CHECKOUT)

    def click_product_title(self) -> None:
        """Click on the product title.

        :return: None.
        """
        self.product_title.click()

    def click_remove_button(self) -> None:
        """Click on the remove from the shopping cart button.

        :return:
        """
        self.remove_button.click()

    def click_view_cart_link(self) -> None:
        """Click on the 'View Cart' link.

        :return: None.
        """
        self.view_cart_link.click()

    def click_checkout_link(self) -> None:
        """Click on the 'Checkout' link.

        :return: None.
        """
        self.checkout_link.click()


class BaseNavBar:
    """This class describes the top nav bar of the base page"""

    def __init__(self, driver):
        self._driver = driver
        self._currency = driver.find_element(*LocatorsNavBar.CURRENCY)
        self._nav_bar = driver.find_element(*LocatorsNavBar.NAVBAR)

    def click_currency_euro(self):
        self._currency.click()
        self._currency.find_element(*LocatorsNavBar.EUR).click()

    def click_currency_pound(self):
        self._currency.click()
        self._currency.find_element(*LocatorsNavBar.POUND).click()

    def click_currency_usd(self):
        self._currency.click()
        self._currency.find_element(*LocatorsNavBar.USD).click()

    def click_contact_us(self):
        self._nav_bar.find_element(*LocatorsNavBar.CONTACT_US).click()

    def click_wishlist(self):
        self._nav_bar.find_element(*LocatorsNavBar.WISH_LIST).click()

    def click_shopping_cart(self):
        self._nav_bar.find_element(*LocatorsNavBar.SHOPPING_CART).click()


class BaseRightMenu:
    def __init__(self, driver) -> None:
        self._driver = driver
        self._right_menu = driver.find_element_by_class_name('list-group')

    def click_my_account(self):
        self._right_menu.find_element(*RightMenuLocators.MY_ACCOUNT).click()

    def click_address_book(self):
        self._right_menu.find_element(*RightMenuLocators.ADDRESS_BOOK).click()

    def click_wish_list(self):
        self._right_menu.find_element(*RightMenuLocators.WISH_LIST).click()

    def click_order_history(self):
        self._right_menu.find_element(*RightMenuLocators.ORDER_HISTORY).click()

    def click_downloads(self):
        self._right_menu.find_element(*RightMenuLocators.DOWNLOADS).click()

    def click_recurring_payments(self):
        self._right_menu.find_element(*RightMenuLocators.RECURRING_PAYMENTS).click()

    def click_reward_points(self):
        self._right_menu.find_element(*RightMenuLocators.REWARD_POINTS).click()

    def click_returns(self):
        self._right_menu.find_element(*RightMenuLocators.RETURNS).click()

    def click_transactions(self):
        self._right_menu.find_element(*RightMenuLocators.TRANSACTIONS).click()

    def click_newsletter(self):
        self._right_menu.find_element(*RightMenuLocators.NEWSLETTER).click()


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
        self._driver.find_element\
            (By.XPATH, f"//a[text()='{self.product_title}']/../../..//span[text()='Add to Cart']/..").click()

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


class SortByDropdownComponent:
    """Sort products by provided option."""

    def __init__(self, driver: Remote) -> None:
        """Initialise a driver.

        :param driver: Remote driver.
        """
        self._driver = driver

    def click_option(self, option) -> None:
        """Click on the specific option.

        :param option: Provided option to click on it.
        :return: None.
        """
        self._driver.find_element(By.XPATH, f"//select[@id='input-sort']//option[.='{option}']").click()


class ShowNumberProductsDropdownComponent:
    """Show provided number of products."""

    def __init__(self, driver: Remote) -> None:
        """Initialise a driver.

        :param driver: Remote driver.
        """
        self._driver = driver

    def click_option(self, option):
        """Click on the specific option.

        :param option: Provided option to click on it.
        :return: None.
        """
        self._driver.find_element(By.XPATH, f"//select[@id='input-limit']//option[.='{option}']").click()


class ProductCompareLinkComponent:
    """A link to compare the products added to the comparison."""

    def __init__(self, driver: Remote) -> None:
        """Initialise the link.

        :param driver: Remote driver.
        """
        self._driver = driver
        self.product_compare_link = driver.find_element(*LocatorProductCompareLink.PRODUCT_COMPARE)

    def click_product_compare_link(self) -> None:
        """Click on the 'Product Compare' link.

        :return: None.
        """
        self.product_compare_link.click()


class ProductsViewModeComponent:
    def __init__(self, driver: Remote) -> None:
        self._driver = driver
        self.list_view_button = driver.find_element(*LocatorsViewModeButton.LIST_VIEW_BUTTON)
        self.grid_view_button = driver.find_element(*LocatorsViewModeButton.GRID_VIEW_BUTTON)

    def click_list_view_button(self) -> None:
        """Click on the 'List' button.

        :return: None.
        """
        self.list_view_button.click()

    def click_grid_view(self) -> None:
        """Click on the 'Grid' button.

        :return: None.
        """
        self.grid_view_button.click()

class YourPersonalDetailsComponent:
    """Your personal details form сonsists four fields to fill first name, last name, email, telephone."""

    def __init__(self, driver: Remote) -> None:
        """Initialize input fields first name, last name, email, telephone.

        :param driver: Remote.
        """
        self._driver = driver
        self.first_name_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.FIRST_NAME_FIELD)
        self.last_name_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.LAST_NAME_FIELD)
        self.email_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.EMAIL_FIELD)
        self.telephone_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.TELEPHONE_FIELD)


class YourPasswordComponent:
    """Your password form сonsists two fields to fill password, password confirm."""

    def __init__(self, driver: Remote) -> None:
        """Initialize input fields password field, password confirm field.

        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.password_field = InputFieldComponent(self._driver, LocatorsYourPasswordComponent.PASSWORD_FIELD)
        self.password_confirm_field = InputFieldComponent(self._driver,
                                                          LocatorsYourPasswordComponent.PASSWORD_CONFIRM_FIELD)


class InputFieldComponent:
    """An input field to fill with data from user."""

    def __init__(self, driver: Remote, input_field_locator: tuple) -> None:
        """Initialize the input field.

        :param driver: Remote
        :param input_field_locator: tuple (example: PASSWORD_FIELD=(By.ID, 'input-password'))
        :return: None
        """
        self._driver = driver
        self.input_field_locator = input_field_locator

    def clear_and_fill_input_field(self, data: str) -> None:
        """Clear and fill input field with data.

        :param data: str
        :return: None
        """
        self.input_field = self._driver.find_element(*self.input_field_locator)
        self.input_field.clear()
        self.input_field.send_keys(data)

    def get_error_message_for_input_field(self) -> str:
        """Get error message for input field if it were incorrect data.

        :return: str
        """
        self.error_message_locator = f'#{self.input_field_locator[1]} ~ div.text-danger'
        self.error_message = WebDriverWait(self._driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.error_message_locator))
        )
        return self.error_message.text


class NewsletterComponent:
    """Two radio buttons to subscribe or unsubscribe to newsletter."""

    def __init__(self, driver: Remote) -> None:
        """Initialize radio buttons.

        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.subscribe_radio_buttons_locator = LocatorsNewsletterComponent.SUBSCRIBE_RADIO_BUTTONS

    def is_subscribed(self) -> bool:
        """Check user is subscribed or not.

        :return: bool
        """
        self.subscribe_radio_buttons = self._driver.find_elements(*self.subscribe_radio_buttons_locator)
        for button in self.subscribe_radio_buttons:
            if button.get_attribute('checked') == 'true' and button.get_attribute('value') == '1':
                return True
        return False

    def subscribe_to_newsletter(self) -> None:
        """Subscribe to newsletter.

        :return: None
        """
        self.subscribe_to_newsletter_locator = f'[{self.subscribe_radio_buttons_locator[0]}="{self.subscribe_radio_buttons_locator[1]}"][value="1"]'
        self._driver.find_element_by_css_selector(self.subscribe_to_newsletter_locator).click()
