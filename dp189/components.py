from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from dp189.locators import LocatorsSearch, LocatorsNavBar, RightMenuLocators, LocatorsShoppingCartButton, \
    LocatorSortBy, LocatorShowNumberProducts, LocatorsLeftCategoryMenu


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
    def __init__(self, driver):
        pass


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
    def __init__(self, driver) -> None:
        self._driver = driver

    def click_desktops(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.DESKTOPS).click()

    def click_pc(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.PC).click()

    def click_mac(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.MAC).click()

    def click_laptops_and_notebooks(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.LAPTOPS_AND_NOTEBOOKS).click()

    def click_macs(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.MACS).click()

    def click_windows(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.WINDOWS).click()

    def click_components(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.COMPONENTS).click()

    def click_mice_and_trackballs(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.MICE_AND_TRACKBALLS).click()

    def click_monitors(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.MONITORS).click()

    def click_printers(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.PRINTERS).click()

    def click_scanners(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.SCANNERS).click()

    def click_web_cameras(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.WEB_CAMERAS).click()

    def click_tablets(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.TABLETS).click()

    def click_software(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.SOFTWARE).click()

    def click_phones_and_pdas(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.PHONES_AND_PDAS).click()

    def click_cameras(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.CAMERAS).click()

    def click_mp3_players(self):
        self._driver.find_element(*LocatorsLeftCategoryMenu.MP3_PLAYERS).click()


class CategoryProductWidgetComponent:
    def __init__(self, driver, product_title):
        self.driver = driver

        self.product_title = f"//*[contains(@class, 'product-thumb')]//a[(text()='{product_title}')]"

        self.shopping_cart_button = driver.find_element(By.XPATH, f"{self.product_title}/../../../div[2]/button[1]")
        self.wish_list_button = driver.find_element(By.XPATH, f"{self.product_title}/../../../div[2]/button[2]")
        self.compare_button = driver.find_element(By.XPATH, f"{self.product_title}/../../../div[2]/button[3]")

    def add_to_shopping_cart(self):
        self.shopping_cart_button.click()

    def add_to_wish_list(self):
        self.wish_list_button.click()

    def add_to_compare_button(self):
        self.compare_button.click()


class SortByDropdownComponent:
    def __init__(self, driver) -> None:
        self._driver = driver
        self._drop_down = driver.find_element(*LocatorSortBy.DROP_DOWN)

    def click_drop_down(self):
        self._drop_down.click()


class ShowNumberProductsDropdownComponent:
    def __init__(self, driver) -> None:
        self._driver = driver
        self.show_number_products = driver.find_element(*LocatorShowNumberProducts.DROP_DOWN)
