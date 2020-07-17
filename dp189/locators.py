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


class LocatorsProductPage:
    """Main locators for Product page."""
    ADD_TO_WISH_LIST = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
    COMPARE_THIS_PRODUCT = (By.CSS_SELECTOR, '[data-original-title="Compare this Product"]')
    PHOTO = (By.XPATH, "//*[@id='content']/div[1]/div[1]/ul[1]/li[1]/a")
    CLOSE_PHOTO = (By.XPATH, '//button[@title="Close (Esc)"]')
    NEXT_PHOTO = (By.XPATH, "//button[@title='Next (Right arrow key)']")
    PREVIOUS_PHOTO = (By.XPATH, "//button[@title='Previous (Left arrow key)']")
    EX_TAX = (By.XPATH, "//ul//li[contains(.,'Ex Tax')]/../li/h2")
    DESCRIPTION_TAB = (By.XPATH, '//*[@id="content"]/div[1]/div[1]/ul[2]/li[1]/a')
    SPECIFICATION_TAB = (By.XPATH, '//*[@id="content"]/div[1]/div[1]/ul[2]/li[2]/a')
    REVIEWS_TAB = (By.XPATH, '//*[@id="content"]/div[1]/div[1]/ul[2]/li[3]/a')


class LocatorsReviewsTab:
    """Locators for Reviews Tab on Product page. """
    CONTINUE = (By.ID, 'button-review')
    YOUR_NAME = (By.XPATH, '//input[@id="input-name"]')
    YOUR_REVIEW = (By.XPATH, '//textarea[@id="input-review"]')
    REVIEW_ERROR_MESSAGE = (
        By.XPATH, '//div[@id="review"]/following-sibling::div[@class="alert alert-danger alert-dismissible"]')


class LocatorsAvailableOptions:
    """Locators for Available options on Product page."""
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
    """Locators fot the 'Your Personal Details' component."""

    FIRST_NAME_FIELD = (By.XPATH, '//*[@id="input-firstname"]')
    LAST_NAME_FIELD = (By.XPATH, '//*[@id="input-lastname"]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="input-email"]')
    TELEPHONE_FIELD = (By.XPATH, '//*[@id="input-telephone"]')


class LocatorsYourPasswordComponent:
    """Locators fot the 'Your Password' component."""

    PASSWORD_FIELD = (By.XPATH, '//*[@id="input-password"]')
    PASSWORD_CONFIRM_FIELD = (By.XPATH, '//*[@id="input-confirm"]')


class LocatorsRegisterPage:
    """Locators fot the 'Register' page."""

    CHECKBOX_PRIVACY_POLICY = (By.NAME, 'agree')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')


class LocatorsNewsletterComponent:
    """Locators fot the 'Newsletter' component."""

    SUBSCRIBE_RADIO_BUTTONS = (By.NAME, 'newsletter')


class LocatorsForgotPasswordPage:
    """Locators for the 'Forgot password' page."""

    EMAIL_FIELD = (By.ID, "input-email")
    BACK_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@class='btn btn-primary']")



class LocatorsWishListPage:
    # TODO correct xpathes
    ITEMS = (By.XPATH, "//div/table/tbody/tr/td[@class='text-left']//a")
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
    ITEMS = (By.XPATH, "//table[@class='table table-bordered']/tbody/tr/td/a/strong")
    ADD_BUTTONS = (By.XPATH, "//table/tbody/tr/td/input[@class='btn btn-primary btn-block']")
    REMOVE_BUTTONS = (By.XPATH, "//table/tbody/tr/td/a[@class='btn btn-danger btn-block']")


