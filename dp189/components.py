from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from dp189.locators import LocatorsSearch, LocatorsNavBar, RightMenuLocators, LocatorsShoppingCartButton, \
    LocatorSortBy, LocatorsLeftCategoryMenu, LocatorShowNumberProducts, LocatorProductCompareLink, \
    LocatorListViewButton, LocatorGridViewButton, LocatorsShopCartDropdown


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
            return ShopCartDropdown(self._driver)


class ShopCartDropdown:
    def __init__(self, driver, product_title):
        self._driver = driver
        self._product_title = driver.find_element(By.XPATH, f"//*[@id='cart']//ul//li//table//tbody//tr//td[2]//a[(text()='{product_title}')]")
        self._remove_button = driver.find_element(By.XPATH, f"{self._product_title}/../../td[5]/button")
        self._view_cart_link = driver.find_element(*LocatorsShoppingCartButton.VIEW_CART)
        self._checkout_link = driver.find_element(*LocatorsShoppingCartButton.CHECKOUT)

    def click_product_title(self):
        self._product_title.click()

    def click_remove_button(self):
        self._remove_button.click()

    def click_view_cart_link(self):
        self._view_cart_link.click()

    def click_checkout_link(self):
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


class LeftCategoryMenuComponent:
    """Left navigation menu on the category page."""

    def __init__(self, driver) -> None:
        """Initialise a driver.

        :param driver: Initialisation of a driver.
        """
        self._driver = driver

    def click_desktops(self) -> None:
        """Click on the 'Desktops' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.DESKTOPS).click()

    def click_pc(self) -> None:
        """Click on the 'PC' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.PC).click()

    def click_mac(self) -> None:
        """Click on the 'Mac' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.MAC).click()

    def click_laptops_and_notebooks(self) -> None:
        """Click on the 'Laptops & Notebooks' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.LAPTOPS_AND_NOTEBOOKS).click()

    def click_macs(self) -> None:
        """Click on the 'Macs' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.MACS).click()

    def click_windows(self) -> None:
        """Click on the 'Windows' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.WINDOWS).click()

    def click_components(self) -> None:
        """Click on the 'Components' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.COMPONENTS).click()

    def click_mice_and_trackballs(self) -> None:
        """Click on the 'Mice and Trackballs' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.MICE_AND_TRACKBALLS).click()

    def click_monitors(self) -> None:
        """Click on the 'Monitors' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.MONITORS).click()

    def click_printers(self) -> None:
        """Click on the 'Printers' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.PRINTERS).click()

    def click_scanners(self) -> None:
        """Click on the 'Scanners' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.SCANNERS).click()

    def click_web_cameras(self) -> None:
        """Click on the 'Web Cameras' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.WEB_CAMERAS).click()

    def click_tablets(self) -> None:
        """Click on the 'Tablets' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.TABLETS).click()

    def click_software(self) -> None:
        """Click on the 'Software' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.SOFTWARE).click()

    def click_phones_and_pdas(self) -> None:
        """Click on the 'Phones & PDAs' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.PHONES_AND_PDAS).click()

    def click_cameras(self) -> None:
        """Click on the 'Cameras' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.CAMERAS).click()

    def click_mp3_players(self) -> None:
        """Click on the 'MP3 Players' link.

        :return: None
        """
        self._driver.find_element(*LocatorsLeftCategoryMenu.MP3_PLAYERS).click()


class CategoryProductWidgetComponent:
    """Widget for products on the category page."""

    def __init__(self, driver, product_title: str) -> None:
        """Initialise the widget and the buttons.

        :param driver: Driver.
        :param product_title: Title of a product.
        """
        self.driver = driver

        self.product_title = f"//*[contains(@class, 'product-thumb')]//a[(text()='{product_title}')]"

        self.shopping_cart_button = driver.find_element(By.XPATH, f"{self.product_title}/../../../div[2]/button[1]")
        self.wish_list_button = driver.find_element(By.XPATH, f"{self.product_title}/../../../div[2]/button[2]")
        self.compare_button = driver.find_element(By.XPATH, f"{self.product_title}/../../../div[2]/button[3]")

    def click_add_to_shopping_cart_button(self) -> None:
        """Click on the "Add to shopping cart" button.

        :return: None
        """
        self.shopping_cart_button.click()

    def click_add_to_wish_list_button(self) -> None:
        """Click on the "Add to Wish List" button.

        :return: None
        """
        self.wish_list_button.click()

    def click_add_to_compare_button(self) -> None:
        """Click on the "Compare this Product" button.

        :return: None
        """
        self.compare_button.click()


class SortByDropdownComponent:
    """A drop-down list with sorting options."""

    def __init__(self, driver) -> None:
        """All sorting options in a drop-down list.

        :param driver: Driver.
        """
        self._driver = driver
        self._drop_down = driver.find_element(*LocatorSortBy.DROP_DOWN)
        self._default = driver.find_element(*LocatorSortBy.DEFAULT)
        self._name_a_z = driver.find_element(*LocatorSortBy.NAME_A_Z)
        self._name_z_a = driver.find_element(*LocatorSortBy.NAME_Z_A)
        self._price_low_high = driver.find_element(*LocatorSortBy.PRICE_LOW_HIGH)
        self._price_high_low = driver.find_element(*LocatorSortBy.PRICE_HIGH_LOW)
        self._rating_highest = driver.find_element(*LocatorSortBy.RATING_HIGHEST)
        self._rating_lowest = driver.find_element(*LocatorSortBy.RATING_LOWEST)
        self._model_a_z = driver.find_element(*LocatorSortBy.MODEL_A_Z)
        self._model_z_a = driver.find_element(*LocatorSortBy.MODEL_Z_A)

    def click_drop_down(self) -> None:
        """Click on the sorting drop-down.

        :return: None
        """
        self._drop_down.click()

    def click_default(self) -> None:
        """Click on the sorting drop-down and on the 'Default' option.

        :return: None
        """
        self.click_drop_down()
        self._default()

    def click_name_a_z(self) -> None:
        """Click on the sorting drop-down and on the 'Name (A - Z)' option.

        :return: None
        """
        self.click_drop_down()
        self._name_a_z.click()

    def click_name_z_a(self) -> None:
        """Click on the sorting drop-down and on the 'Name (Z - A)' option.

        :return: None
        """
        self.click_drop_down()
        self._name_z_a.click()

    def click_price_low_high(self) -> None:
        """Click on the sorting drop-down and on the 'Price (Low > High)' option.

        :return: None
        """
        self.click_drop_down()
        self._price_low_high.click()

    def click_price_high_low(self) -> None:
        """Click on the sorting drop-down and on the 'Price (High > Low)' option.

        :return: None
        """
        self.click_drop_down()
        self._price_high_low.click()

    def click_rating_highest(self) -> None:
        """Click on the sorting drop-down and on the 'Rating (Highest)' option.

        :return: None
        """
        self.click_drop_down()
        self._rating_highest.click()

    def click_rating_lowest(self) -> None:
        """Click on the sorting drop-down and on the 'Rating (Lowest)' option.

        :return: None
        """
        self.click_drop_down()
        self._rating_lowest.click()

    def click_model_a_z(self) -> None:
        """Click on the sorting drop-down and on the 'Model (A - Z)' option.

        :return: None
        """
        self.click_drop_down()
        self._model_a_z.click()

    def click_model_z_a(self) -> None:
        """Click on the sorting drop-down and on the 'Model (Z - A)' option.

        :return: None
        """
        self.click_drop_down()
        self._model_z_a.click()


class ShowNumberProductsDropdownComponent:
    """A drop-down list with number of displayed products options."""

    def __init__(self, driver) -> None:
        """All options in a drop-down list.

        :param driver: Driver.
        """
        self._driver = driver
        self._drop_down = driver.find_element(*LocatorShowNumberProducts.DROP_DOWN)
        self._fifteen = driver.find_element(*LocatorShowNumberProducts.FIFTEEN)
        self._twenty_five = driver.find_element(*LocatorShowNumberProducts.TWENTY_FIVE)
        self._fifty = driver.find_element(*LocatorShowNumberProducts.FIFTY)
        self._seventy_five = driver.find_element(*LocatorShowNumberProducts.SEVENTY_FIVE)
        self._hundred = driver.find_element(*LocatorShowNumberProducts.HUNDRED)

    def click_drop_down(self) -> None:
        """Click on the drop-down.

        :return: None
        """
        self._drop_down.click()

    def click_fifteen(self) -> None:
        """Click on the sorting drop-down and on the '15' option.

        :return: None
        """
        self.click_drop_down()
        self._fifteen.click()

    def click_twenty_five(self) -> None:
        """Click on the sorting drop-down and on the '25' option.

        :return: None
        """
        self.click_drop_down()
        self._twenty_five.click()

    def click_fifty(self) -> None:
        """Click on the sorting drop-down and on the '50' option.

        :return: None
        """
        self.click_drop_down()
        self._fifty.click()

    def click_seventy_five(self) -> None:
        """Click on the sorting drop-down and on the '75' option.

        :return: None
        """
        self.click_drop_down()
        self._seventy_five.click()

    def click_hundred(self) -> None:
        """Click on the sorting drop-down and on the '100' option.

        :return: None
        """
        self.click_drop_down()
        self._hundred.click()


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

        :return: None
        """
        self._product_compare_link.click()


class ListViewComponent:
    """A button to switch on the list view."""

    def __init__(self, driver) -> None:
        """Initialise the button.

        :param driver: Driver.
        """
        self._driver = driver
        self._list_view = driver.find_element(*LocatorListViewButton.BUTTON)

    def click_list_view(self) -> None:
        """Click on the 'List' button.

        :return: None
        """
        self._list_view.click()


class GridViewComponent:
    """A button to switch on the list view."""

    def __init__(self, driver) -> None:
        """Initialise the button.

        :param driver: Driver.
        """
        self._driver = driver
        self._grid_view = driver.find_element(*LocatorGridViewButton.BUTTON)

    def click_grid_view(self) -> None:
        """Click on the 'Grid' button.

        :return: None
        """
        self._grid_view.click()
