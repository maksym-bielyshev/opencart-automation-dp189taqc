from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Remote
# from locators import LocatorsSearch, LocatorsNavBar, RightMenuLocators, LocatorsShoppingCartButton
from locators import *


class SearchArea:
    """"This class describes the search area common in all pages. It consists or search field and search button"""
    def __init__(self, driver):
        self._driver = driver
        self._search_field = driver.find_element(*LocatorsSearch.SEARCH_FIELD)
        self._search_button = driver.find_element(*LocatorsSearch.SEARCH_BUTTON)

    def fill_search_field_and_press_enter(self, item: str):
        self._search_field.clear().send_keys(item).send_keys(Keys.RETURN)
        #return SearchPage(self._driver)

    def fill_search_field_and_click(self, item: str):
        self._search_field.clear().send_keys(item)
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
    def __init__(self, driver):
        self._driver = driver
        self._form_currency = driver.find_element(*LocatorsNavBar.CURRENCY)
        self._nav_bar = driver.find_element(*LocatorsNavBar.NAVBAR)

    def click_currency_euro(self):
        select_euro = Select(self._form_currency)
        select_euro.select_by_visible_text("Euro")

    def click_currency_pound(self):
        select_pound = Select(self._form_currency)
        select_pound.select_by_visible_text("Pound Sterling")

    def click_currency_usd(self):
        select_usd = Select(self._form_currency)
        select_usd.select_by_visible_text("US Dollar")

    def click_contact_us(self):
        self._nav_bar.find_element(*LocatorsNavBar.CONTACT_US).click()
        #return ContactUsPage(self._driver)

    def click_wishlist(self):
        self._nav_bar.find_element(*LocatorsNavBar.WISH_LIST).click()
        #return WishListPage(self._driver)

    def click_shopping_cart(self):
        self._nav_bar.find_element(*LocatorsNavBar.SHOPPING_CART).click()
        #return ShoppingCartPage(self._driver)


class NavBarNotLoggedIn(BaseNavBar):
    """This class describes navbar when user has not signed in"""
    def __init__(self, driver):
        BaseNavBar.__init__(self, driver)

    def click_my_account_register(self):
        select_register = Select(self._nav_bar.find_element(*LocatorsNavBar.MY_ACCOUNT))
        select_register.select_by_visible_text("Register")
        #return RegisterPage(self._driver)

    def click_my_account_login(self):
        select_login = Select(self._nav_bar.find_element(*LocatorsNavBar.MY_ACCOUNT))
        select_login.select_by_visible_text("Login")
        #return LoginPage(self._driver)


class NavBarLoggedIn(BaseNavBar):
    """This class describes navbar when user signed in"""
    def __init__(self, driver):
        BaseNavBar.__init__(self, driver)

    def click_my_account(self):
        select_my_account = Select(self._nav_bar.find_element(*LocatorsNavBar.MY_ACCOUNT))
        select_my_account.select_by_visible_text("My Account")
        #return MyAccountPage(self._driver)

    def click_order_history(self):
        select_order_history = Select(self._nav_bar.find_element(*LocatorsNavBar.MY_ACCOUNT))
        select_order_history.select_by_visible_text("Order History")
        #return OrderHistoryPage(self._driver)

    def click_transactions(self):
        select_register = Select(self._nav_bar.find_element(*LocatorsNavBar.MY_ACCOUNT))
        select_register.select_by_visible_text("Transactions")
        #return TransactionsPage(self._driver)

    def click_downloads(self):
        select_downloads = Select(self._nav_bar.find_element(*LocatorsNavBar.MY_ACCOUNT))
        select_downloads.select_by_visible_text("Downloads")
        #return Downloads(self._page)

    def click_logout(self):
        select_logout = Select(self._nav_bar.find_element(*LocatorsNavBar.MY_ACCOUNT))
        select_logout.select_by_visible_text("Logout")
        #return Logout(self._driver)


class BaseRightMenu:
    def __init__(self, driver) -> None:
        self._driver = driver
        self._right_menu = driver.find_element_by_class_name('list-group')

    def click_my_account(self):
        self._right_menu.find_element(*RightMenuLocators.MY_ACCOUNT).click()
        #return MyAccount(self._driver)

    def click_address_book(self):
        self._right_menu.find_element(*RightMenuLocators.ADDRESS_BOOK).click()
        #return AddressBookPage(self._driver)

    def click_wish_list(self):
        self._right_menu.find_element(*RightMenuLocators.WISH_LIST).click()
        #return WishListPage(self._driver)

    def click_order_history(self):
        self._right_menu.find_element(*RightMenuLocators.ORDER_HISTORY).click()
        #return OrderHistory(self._page)

    def click_downloads(self):
        self._right_menu.find_element(*RightMenuLocators.DOWNLOADS).click()
        #return DownloadsPage(self._driver)

    def click_recurring_payments(self):
        self._right_menu.find_element(*RightMenuLocators.RECURRING_PAYMENTS).click()
        #return RecurringPaymentsPage(self._driver)

    def click_reward_points(self):
        self._right_menu.find_element(*RightMenuLocators.REWARD_POINTS).click()
        #return RewardPointsPage(self._driver)

    def click_returns(self):
        self._right_menu.find_element(*RightMenuLocators.RETURNS).click()
        #return ReturnsPage(self._driver)

    def click_transactions(self):
        self._right_menu.find_element(*RightMenuLocators.TRANSACTIONS).click()
        #return TransactionsPage(self._driver)

    def click_newsletter(self):
        self._right_menu.find_element(*RightMenuLocators.NEWSLETTER).click()
        #return NewsletterPage(self._driver)


class RightMenuNotLoggedIn(BaseRightMenu):
    def __init__(self, driver) -> None:
        BaseRightMenu.__init__(self, driver)

    def click_login(self):
        self._right_menu.find_element(*RightMenuLocators.LOGIN).click()
        #return LoginPage(self._driver)

    def click_register(self):
        self._right_menu.find_element(*RightMenuLocators.REGISTER).click()
        #return LoginPage(self._driver)

    def click_forgotten_password(self):
        self._right_menu.find_element(*RightMenuLocators.FORGOTTEN_PASSWORD).click()
        #return ForgottenPasswordPage(self._driver)


class RightMenuLoggedIn(BaseRightMenu):
    def __init__(self, driver) -> None:
        BaseRightMenu.__init__(self, driver)

    def click_edit_account(self):
        self._right_menu.find_element(*RightMenuLocators.EDIT_ACCOUNT).click()
        #return EditAccountPage(self._driver)

    def click_password(self):
        self._right_menu.find_element(*RightMenuLocators.PASSWORD).click()
        #return PasswordPage(self._driver)

    def click_logout(self):
        self._right_menu.find_element(*RightMenuLocators.LOGOUT).click()
        #return LogoutPage(self._driver)
