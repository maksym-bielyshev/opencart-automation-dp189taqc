from selenium.webdriver.common.by import By


class LocatorsSearch:
    SEARCH_FIELD = (By.CLASS_NAME, 'input-lg')
    SEARCH_BUTTON = (By.CLASS_NAME, 'input-group-btn')


class LocatorsNavBar:
    # Absolute
    NAVBAR = (By.CLASS_NAME, 'navbar-nav')
    CURRENCY = (By.ID, 'form-currency')

    # Relative
    CONTACT_US = (By.XPATH, './/li[1]/a')
    MY_ACCOUNT = (By.XPATH, './/li[2]/a')
    WISH_LIST = (By.XPATH, './/li[3]/a')
    SHOPPING_CART = (By.XPATH, './/li[4]/a')
    CHECKOUT = (By.XPATH, './/li[5]/a')


# class LocatorsFooter:
#     ABOUT_US = (By.CSS_SELECTOR, 'body > footer > div > div > div:nth-child(1) > ul > li:nth-child(1) > a')
#     # /html/body/footer/div/div/div[1]/ul/li[1]/a
#     DELIVERY_INFORMATION = (By.CSS_SELECTOR, 'body > footer > div > div > div:nth-child(1) > ul > li:nth-child(2) > a') #change text link
#     PRIVACY_POLICY = (By.CSS_SELECTOR, 'body > footer > div > div > div:nth-child(1) > ul > li:nth-child(3) > a')
#     TERMS_AND_CONDITIONS = (By.CSS_SELECTOR, 'body > footer > div > div > div:nth-child(1) > ul > li:nth-child(4) > a')
#     CONTACT_US = (By.CSS_SELECTOR, 'body > footer > div > div > div:nth-child(2) > ul > li:nth-child(1) > a')
#     RETURNS = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(2) > ul > li:nth-child(2) > a")
#     SITE_MAP = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(2) > ul > li:nth-child(3) > a")
#     BRANDS = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(3) > ul > li:nth-child(1) > a")
#     GIFT_CERTIFICATES = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(3) > ul > li:nth-child(2) > a")
#     AFFILIATE = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(3) > ul > li:nth-child(3) > a")
#     SPECIALS = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(3) > ul > li:nth-child(4) > a")
#     MY_ACCOUNT = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(4) > ul > li:nth-child(1) > a")
#     ORDER_HISTORY = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(4) > ul > li:nth-child(2) > a")
#     WISH_LIST = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(4) > ul > li:nth-child(3) > a")
#     NEWSLETTER = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(4) > ul > li:nth-child(4) > a")

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
