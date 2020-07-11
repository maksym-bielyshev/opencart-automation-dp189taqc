from selenium.webdriver.common.by import By


class LocatorsSearch:
    SEARCH_FIELD = (By.CLASS_NAME, 'input-lg')
    SEARCH_BUTTON = (By.CLASS_NAME, 'input-group-btn')


class LocatorsNavBar:
    # Absolute
    NAVBAR = (By.CLASS_NAME, 'list-inline')
    MY_ACCOUNT = (By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]')
    CURRENCY = (By.CLASS_NAME, 'btn-group')
    USD = (By.XPATH, './/ul/li[3]/button')
    POUND = (By.XPATH, './/ul/li[2]/button')
    EUR = (By.XPATH, './/ul/li[1]/button')

    # Relative
    CONTACT_US = (By.XPATH, './/li[1]/a')
    # MY_ACCOUNT = (By.XPATH, './/li[2]/a')
    LOGIN = (By.XPATH, './/ul/li[2]/a')
    REGISTER = (By.XPATH, './/ul/li[1]/a')
    WISH_LIST = (By.XPATH, './/li[3]/a')
    SHOPPING_CART = (By.XPATH, './/li[4]/a')
    CHECKOUT = (By.XPATH, './/li[5]/a')


class RightMenuLocators:
    RIGHT_MENU = (By.CLASS_NAME, 'list-group')
    LOGIN = (By.XPATH, './/a[text()="Login"]')
    REGISTER = (By.XPATH, './/a[text()="Register"]')
    FORGOTTEN_PASSWORD = (By.XPATH, './/a[text()="Forgotten Password"]')
    MY_ACCOUNT = (By.XPATH, './/a[text()="My Account"]')
    EDIT_ACCOUNT = (By.XPATH, './/a[text()="Edit Account"]')
    PASSWORD = (By.XPATH, './/a[text()="Password"]')
    ADDRESS_BOOK = (By.XPATH, './/a[text()="Address Book"]')
    WISH_LIST = (By.XPATH, './/a[text()="Wish List"]')
    ORDER_HISTORY = (By.XPATH, './/a[text()="Order History"]')
    DOWNLOADS = (By.XPATH, './/a[text()="Downloads"]')
    RECURRING_PAYMENTS = (By.XPATH, './/a[text()="Recurring payments"]')
    REWARD_POINTS = (By.XPATH, './/a[text()="Reward Points"]')
    RETURNS = (By.XPATH, './/a[text()="Returns"]')
    TRANSACTIONS = (By.XPATH, './/a[text()="Transactions"]')
    NEWSLETTER = (By.XPATH, './/a[text()="Newsletter"]')
    LOGOUT = (By.XPATH, './/a[text()="Logout"]')


class LocatorsShoppingCartButton:
    SHOP_CART_BUTTON = (By.XPATH, '/html/body/header/div/div/div[3]/div/button')
    CART_ITEMS = (By.XPATH, '/html/body/header/div/div/div[3]/div/ul/li[1]/table')


class LocatorYourStoreLink:
    YOUR_STORE = (By.XPATH, '/html/body/header/div/div/div[1]/div/h1/a')


class LocatorsHomePage:
    # TODO correct xpathes
    FEATURED_PRODUCT = (By.CLASS_NAME, 'product-layout')
    CAPTION = (By.XPATH, './/div/div[2]/h4/a')
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[3]/button[1]')


class LocatorsLeftCategoryMenu:
    """Locators for a left menu in category page."""

    LEFT_CATEGORY_MENU = (By.ID, 'column-left')

    DESKTOPS = (By.XPATH, "//a[contains(text(),'Desktops (')]")
    PC = (By.XPATH, "//a[contains(text(),'PC (')]")
    MAC = (By.XPATH, "//a[contains(text(),'PC (')]")
    LAPTOPS_AND_NOTEBOOKS = (By.XPATH, "//a[contains(text(),'Laptops & Notebooks (')]")
    MACS = (By.XPATH, "//a[contains(text(),'Macs (')]")
    WINDOWS = (By.XPATH, "//a[contains(text(),'Windows (')]")
    COMPONENTS = (By.XPATH, "//a[contains(text(),'Components (')]")
    MICE_AND_TRACKBALLS = (By.XPATH, "//a[contains(text(),'Mice and Trackballs (')]")
    MONITORS = (By.XPATH, "//a[contains(text(),'Monitors (')]")
    PRINTERS = (By.XPATH, "//a[contains(text(),'Printers (')]")
    SCANNERS = (By.XPATH, "//a[contains(text(),'Scanners (')]")
    WEB_CAMERAS = (By.XPATH, "//a[contains(text(),'Web Cameras (')]")
    TABLETS = (By.XPATH, "//a[contains(text(),'Tablets (')]")
    SOFTWARE = (By.XPATH, "//a[contains(text(),'Software (')]")
    PHONES_AND_PDAS = (By.XPATH, "//a[contains(text(),'Phones & PDAs (')]")
    CAMERAS = (By.XPATH, "//a[contains(text(),'Cameras (')]")
    MP3_PLAYERS = (By.XPATH, "//a[contains(text(),'MP3 Players (')]")


class LocatorSortBy:
    """Locators for a 'Sort By' drop-down."""

    DROP_DOWN = (By.ID, "input-sort")

    DEFAULT = (By.XPATH, '//*[@id="input-sort"]/option[1]')
    NAME_A_Z = (By.XPATH, '//*[@id="input-sort"]/option[2]')
    NAME_Z_A = (By.XPATH, '//*[@id="input-sort"]/option[3]')
    PRICE_LOW_HIGH = (By.XPATH, '//*[@id="input-sort"]/option[4]')
    PRICE_HIGH_LOW = (By.XPATH, '//*[@id="input-sort"]/option[5]')
    RATING_HIGHEST = (By.XPATH, '//*[@id="input-sort"]/option[6]')
    RATING_LOWEST = (By.XPATH, '//*[@id="input-sort"]/option[7]')
    MODEL_A_Z = (By.XPATH, '//*[@id="input-sort"]/option[8]')
    MODEL_Z_A = (By.XPATH, '//*[@id="input-sort"]/option[9]')


class LocatorShowNumberProducts:
    """Locator for a 'Show' (number of products) drop-down."""

    DROP_DOWN = (By.ID, "input-limit")

    FIFTEEN = (By.XPATH, '//*[@id="input-limit"]/option[1]')
    TWENTY_FIVE = (By.XPATH, '//*[@id="input-limit"]/option[2]')
    FIFTY = (By.XPATH, '//*[@id="input-limit"]/option[3]')
    SEVENTY_FIVE = (By.XPATH, '//*[@id="input-limit"]/option[4]')
    HUNDRED = (By.XPATH, '//*[@id="input-limit"]/option[5]')


class LocatorProductCompareLink:
    """Locator for a 'Product Compare' link."""

    PRODUCT_COMPARE = (By.ID, 'compare-total')


class LocatorListViewButton:
    """Locator for a 'List' (view) button."""

    BUTTON = (By.ID, 'list-view')


class LocatorGridViewButton:
    """Locator for a 'Grid' (view) button."""

    BUTTON = (By.ID, 'grid-view')
