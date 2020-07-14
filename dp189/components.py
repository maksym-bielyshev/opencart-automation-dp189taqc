from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from dp189.locators import LocatorsSearch, LocatorsNavBar, RightMenuLocators, LocatorsShoppingCartButton, \
    LocatorProductCompareLink, LocatorListViewButton, LocatorGridViewButton, LocatorProductWidget


class SearchArea:
    """"This class describes the search area common in all pages. It consists or search field and search button"""
    def __init__(self, driver):
        self._driver = driver
        self._search_field = driver.find_element(*LocatorsSearch.SEARCH_FIELD)
        self._search_button = driver.find_element(*LocatorsSearch.SEARCH_BUTTON)


    def fill_search_field_and_hit_return(self, item: str):
        self._search_field.clear()
        self._search_field.send_keys(item).send_keys(Keys.RETURN)
        #return SearchPage(self._driver)
    
    def fill_search_field_and_click(self, item: str):
        self._search_field.clear()
        self._search_field.send_keys(item)
        self._search_button.click()
        #return SearchPage(self._driver)


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
        self._product_title = driver.find_element(
            By.XPATH, f"//*[@id='cart']//ul//li//table//tbody//tr//td[2]//a[(text()='{product_title}')]")
        self._remove_button = driver.find_element(By.XPATH, f"{self._product_title}/../../td[5]/button")
        self._view_cart_link = driver.find_element(*LocatorsShoppingCartButton.VIEW_CART)
        self._checkout_link = driver.find_element(*LocatorsShoppingCartButton.CHECKOUT)

    def click_product_title(self) -> None:
        """Click on the product title.

        :return: None.
        """
        self._product_title.click()

    def click_remove_button(self) -> None:
        """Click on the remove from the shopping cart button.

        :return:
        """
        self._remove_button.click()

    def click_view_cart_link(self) -> None:
        """Click on the 'View Cart' link.

        :return: None.
        """
        self._view_cart_link.click()

    def click_checkout_link(self) -> None:
        """Click on the 'Checkout' link.

        :return: None.
        """
        self._checkout_link.click()


class BaseNavBar:
    """This class describes the top nav bar of the base page"""
    def __init__(self, driver: Remote):
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


class ListProductWidgetsComponent:
    """All products on the 'Category' page."""

    def __init__(self, driver: Remote):
        """Initialise a driver and an empty list.

        :param driver: Remote driver.
        """
        self.driver = driver
        self.list_product_widgets = []

    def open_category(self, category_title: str) -> None:
        """Open a specific category.

        :param category_title: The title of the category.
        :return: None.
        """
        category_title = f"//div[@class='col-sm-6']//a[text()='{category_title}']"
        self.driver.find_element(By.XPATH, category_title).click()

    def get_list_product_widgets(self) -> list:
        """Get a list of all products on the 'Category' page.

        :return: List of all products on the 'Category' page.
        """
        self.list_product_widgets = self.driver.find_elements(*LocatorProductWidget.PRODUCT_WIDGET)
        return self.list_product_widgets


class CategoryProductWidgetComponent:
    """Widget for products on the category page."""

    def __init__(self, driver: Remote, product_title: str) -> None:
        """Initialise the widget and the buttons.

        :param driver: Remote river.
        :param product_title: The title of the product.
        """
        self.driver = driver

        self.product_title = f"//*[contains(@class, 'product-thumb')]//a[(text()='{product_title}')]"

        self.shopping_cart_button = driver.find_element(By.XPATH, f"{self.product_title}/../../../div[2]/button[1]")
        self.wish_list_button = driver.find_element(By.XPATH, f"{self.product_title}/../../../div[2]/button[2]")
        self.compare_button = driver.find_element(By.XPATH, f"{self.product_title}/../../../div[2]/button[3]")

    def click_add_to_shopping_cart_button(self) -> None:
        """Click on the "Add to shopping cart" button.

        :return: None.
        """
        self.shopping_cart_button.click()

    def click_add_to_wish_list_button(self) -> None:
        """Click on the "Add to Wish List" button.

        :return: None.
        """
        self.wish_list_button.click()

    def click_add_to_compare_button(self) -> None:
        """Click on the "Compare this Product" button.

        :return: None.
        """
        self.compare_button.click()


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

    def __init__(self, driver) -> None:
        """Initialise the link.

        :param driver: Driver.
        """
        self._driver = driver
        self._product_compare_link = driver.find_element(*LocatorProductCompareLink.PRODUCT_COMPARE)

    def click_product_compare_link(self) -> None:
        """Click on the 'Product Compare' link.

        :return: None.
        """
        self._product_compare_link.click()


class ListViewComponent:
    """A button to switch on the list view."""

    def __init__(self, driver: Remote) -> None:
        """Initialise the button.

        :param driver: Driver.
        """
        self._driver = driver
        self._list_view = driver.find_element(*LocatorListViewButton.BUTTON)

    def click_list_view(self) -> None:
        """Click on the 'List' button.

        :return: None.
        """
        self._list_view.click()


class GridViewComponent:
    """A button to switch on the list view."""

    def __init__(self, driver: Remote) -> None:
        """Initialise the button.

        :param driver: Remote driver.
        """
        self._driver = driver
        self._grid_view = driver.find_element(*LocatorGridViewButton.BUTTON)

    def click_grid_view(self) -> None:
        """Click on the 'Grid' button.

        :return: None.
        """
        self._grid_view.click()
