from selenium.webdriver.common.by import By

class LocatorsSearch:
    SEARCH_FIELD = (By.CLASS_NAME, 'input-lg')
    SEARCH_BUTTON = (By.CLASS_NAME, 'input-group-btn')


class LocatorsNavBar:
    # Absolute
    NAVBAR = (By.CLASS_NAME, 'list-inline')
    MY_ACCOUNT = (By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]')
    CURRENCY = (By.CLASS_NAME, 'btn-group')
    USD = (By.XPATH,'.//ul/li[3]/button')
    POUND = (By.XPATH, './/ul/li[2]/button')
    EUR = (By.XPATH, './/ul/li[1]/button')


    # Relative
    CONTACT_US = (By.XPATH, './/li[1]/a')
    #MY_ACCOUNT = (By.XPATH, './/li[2]/a')
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


class LocatorsYourPersonalDetailsComponent:
    FIRST_NAME_FIELD = (By.ID, 'input-firstname')
    LAST_NAME_FIELD = (By.ID, 'input-lastname')
    EMAIL_FIELD = (By.ID, 'input-email')
    TELEPHONE_FIELD = (By.ID, 'input-telephone')


class LocatorsYourPasswordComponent:
    PASSWORD_FIELD = (By.ID, 'input-password')
    PASSWORD_CONFIRM_FIELD = (By.ID, 'input-confirm')


class LocatorsRegisterPage:
    CHECKBOX_PRIVACY_POLICY = (By.NAME, 'agree')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')


class LocatorsNewsletterComponent:
    SUBSCRIBE_RADIO_BUTTONS = (By.NAME, 'newsletter')


class LocatorsAddAddressComponent:
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="input-firstname"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@id="input-lastname"]')
    COMPANY_INPUT = (By.XPATH, '//input[@id="input-company"]')
    ADDRESS_1_INPUT = (By.XPATH, '//input[@id="input-address-1"]')
    ADDRESS_2_INPUT = (By.XPATH, '//input[@id="input-address-2"]')
    CITY_INPUT = (By.XPATH, '//input[@id="input-city"]')
    POST_CODE_INPUT = (By.XPATH, '//input[@id="input-postcode"]')
    COUNTRY_SELECTOR = (By.XPATH, '//select[@id="input-country"]')
    REGION_SELECTOR = (By.XPATH, '//select[@id="input-zone"]')
    DEFAULT_ADDRESS_RADIO_CONTAINER = (By.XPATH, '//label[@class="radio-inline"]/..')

class LocatorsAddAddressPage:
    BACK_BUTTON = (By.XPATH, '//a[text()="Back"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@value="Continue"]')