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


class LocatorsProductPage:
    ADD_TO_WISH_LIST = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
    COMPARE_THIS_PRODUCT = (By.CSS_SELECTOR, '[data-original-title="Compare this Product"]')
    PHOTO = (By.XPATH, "//*[@id='content']/div[1]/div[1]/ul[1]/li[1]/a")
    NEXT_PHOTO = (By.XPATH, "//button[@title='Next (Right arrow key)']")
    PREVIOUS_PHOTO = (By.XPATH, "//button[@title='Previous (Left arrow key)']")
    EX_TAX = (By.XPATH, "//ul//li[contains(.,'Ex Tax')]/../li/h2")
    DESCRIPTION_TAB = (By.XPATH, '//*[@id="content"]/div[1]/div[1]/ul[2]/li[1]/a')
    SPECIFICATION_TAB = (By.XPATH, '//*[@id="content"]/div[1]/div[1]/ul[2]/li[2]/a')
    REVIEWS_TAB = (By.XPATH, '//*[@id="content"]/div[1]/div[1]/ul[2]/li[3]/a')


class LocatorsReviewsTab:
    YOUR_NAME = (By.ID, 'input-name')
    YOUR_REVIEW = (By.ID, 'input-review')
    CONTINUE = (By.ID, 'button-review')
    REVIEW_ERROR_MESSAGE = (
        By.XPATH, '//div[@id="review"]/following-sibling::div[@class="alert alert-danger alert-dismissible"]')


class LocatorsAvailableOptions:
    QUANTITY = (By.ID, 'input-quantity')
    ADD_TO_CART = (By.ID, 'button-cart')
    ALL_OPTIONS = (By.CSS_SELECTOR, '#product')
    TEXT_FIELD = (By.XPATH, '//input[@value="test"]')
    DATE = (By.XPATH, '//input[@data-date-format="YYYY-MM-DD"]')
    TIME = (By.XPATH, '//input[@data-date-format="HH:mm"]')
    DATE_AND_TIME = (By.XPATH, '//input[@data-date-format="YYYY-MM-DD HH:mm"]')
    TEXT_AREA = (By.XPATH, '//h3[text()="Available Options"]/..//textarea')
    CHECKBOX_CONTAINER = (By.XPATH, '//div[@class="checkbox"]/..')
    RADIO_CONTAINER = (By.XPATH, '//div[@class="radio"]/..')
    SELECT_CONTAINER = (By.XPATH, '//div/select[contains(.,"--- Please Select ---")]')


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
