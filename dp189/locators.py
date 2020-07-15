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


class LocatorsForgotPasswordPage:
    """Locators fot the 'Forgot password' page."""

    EMAIL_FIELD = (By.ID, "input-email")
    BACK_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@class='btn btn-primary']")



class LocatorsWishListPage:
    # TODO correct xpathes
    PRODUCT_NAME = (By.XPATH, "//td[@class='text-left']//a")
    ADD_PRODUCT_TO_CARD = (By.XPATH, "../../td[@class='text-right']/button[@class='btn btn-primary']")
    DELETE_PRODUCT_FROM_CARD = (By.XPATH, "../../td[@class='text-right']/a[@class='btn btn-danger']")
    CONTINUE_BUTTON = (By.XPATH, "//div[@class='pull-right']//a[@class='btn btn-primary']")


class LocatorsGiftCertificatePage:
    # TODO correct xpathes
    RECEPIENT_NAME = (By.XPATH, "//div[@class='col-sm-10']//input[@name='to_name']")
    RECEPIENT_EMAIL = (By.XPATH, "//div[@class='col-sm-10']//input[@name='to_email']")
    YOUR_NAME = (By.XPATH, "//div[@class='col-sm-10']//input[@name='from_name']")
    YOUR_EMAIL = (By.XPATH, "//div[@class='col-sm-10']//input[@name='from_email']")
    GIFT_CERTIFICATE_THEME = (By.XPATH, "//div[@class='radio']//label")
    MESSAGE = (By.XPATH, "//div[@class='col-sm-10']//textarea[@name='message']")
    AMOUNT = (By.XPATH, "//div[@class='col-sm-10']//input[@name='amount']")
    AGREE = (By.XPATH, "//div[@class='pull-right']//input[@name='agree']")
    CONTINUE_BUTTON = (By.XPATH, "//div[@class='pull-right']//input[@type='submit']")

class LocatorsComparePage:
    # TODO correct xpathes
    ITEM = (By.PARTIAL_LINK_TEXT, "//table[@class='table table-bordered']/tbody/tr/td/a/strong")

