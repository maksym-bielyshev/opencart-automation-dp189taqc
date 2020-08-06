from selenium.webdriver.common.by import By


class LocatorBasePageSearch:
    """Locator for search field on base page"""

    SEARCH_FIELD = (By.CLASS_NAME, 'input-lg')


class LocatorsBasePageNavBar:
    """Locators for top navbar links on base page"""

    NAVBAR = (By.CLASS_NAME, 'list-inline')
    MY_ACCOUNT = (By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]')
    CURRENCY = (By.XPATH, '//span[text()="Currency"]/../..')
    USD = (By.XPATH, './/ul/li[3]/button')
    POUND = (By.XPATH, './/ul/li[2]/button')
    EUR = (By.XPATH, './/ul/li[1]/button')
    CONTACT_US = (By.XPATH, './/li[1]/a')
    LOGIN = (By.XPATH, './/ul/li[2]/a')
    REGISTER = (By.XPATH, './/ul/li[1]/a')
    WISH_LIST = (By.XPATH, './/li[3]/a')
    SHOPPING_CART = (By.XPATH, './/li[4]/a')
    CHECKOUT = (By.XPATH, './/li[5]/a')


class LocatorsBasePageMainMenu:
    """Locators for main menu on base page"""

    DESKTOPS = (By.XPATH, '//a[text()="Desktops"]')
    LAPTOPS_NOTEBOOKS = (By.XPATH, '//a[text()="Laptops & Notebooks"]')
    COMPONENTS = (By.XPATH, '//a[text()="Components"]')
    TABLETS = (By.XPATH, '//a[text()="Tablets"]')
    SOFTWARE = (By.XPATH, '//a[text()="Software"]')
    PHONES_PDAS = (By.XPATH, '//a[text()="Phones & PDAs"]')
    CAMERAS = (By.XPATH, '//a[text()="Cameras"]')
    MP3_PLAYERS = (By.XPATH, '//a[text()="MP3 Players"]')


class LocatorsRightMenuRegisterPage:
    """"Locators for right menu on Register and Login pages"""

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
    """Locators for a black shop cart button."""

    SHOP_CART_BUTTON = (By.XPATH, '/html/body/header/div/div/div[3]/div/button')
    CART_ITEMS = (By.XPATH, '/html/body/header/div/div/div[3]/div/ul/li[1]/table')
    VIEW_CART = (By.XPATH, '//ul[@class="dropdown-menu pull-right"]//li[2]//div//p//a[1]')
    CHECKOUT = (By.XPATH, '//ul[@class="dropdown-menu pull-right"]//li[2]//div//p//a[2]')


class LocatorYourStoreLink:
    YOUR_STORE = (By.XPATH, '/html/body/header/div/div/div[1]/div/h1/a')


class LocatorsHomePage:
    FEATURED_PRODUCT = (By.CLASS_NAME, 'product-layout')
    CAPTION = (By.XPATH, './/div/div[2]/h4/a')
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[3]/button[1]')


class LocatorProductCompareLink:
    """Locator for a 'Product Compare' link."""

    PRODUCT_COMPARE = (By.ID, 'compare-total')


class LocatorsViewModeButton:
    """Locator for a different view buttons."""

    LIST_VIEW_BUTTON = (By.ID, 'list-view')
    GRID_VIEW_BUTTON = (By.ID, 'grid-view')


class LocatorProductWidget:
    """Locator for a widget of the product."""

    PRODUCT_WIDGET = (By.CLASS_NAME, 'product-thumb')


class LocatorCategoryTitle:
    """Category title text."""

    CATEGORY_TITLE = (By.XPATH, '//*[@id="content"]/h2')


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
    CHECKBOX_LABEL = (By.XPATH, '//div[@class="checkbox"]/label')
    RADIO_CONTAINER = (By.XPATH, '//div[@class="radio"]/..')
    RADIO_BUTTON_LABEL = (By.XPATH, '//div[@class="radio"]/label')
    SELECT_CONTAINER = (By.XPATH, '//div/select[contains(.,"--- Please Select ---")]')


class LocatorsYourPersonalDetailsComponent:
    """Locators fot the 'Your Personal Details' component."""

    FIRST_NAME_FIELD = (By.XPATH, './/input[@name="firstname"]')
    LAST_NAME_FIELD = (By.XPATH, './/input[@name="lastname"]')
    EMAIL_FIELD = (By.XPATH, './/input[@name="email"]')
    TELEPHONE_FIELD = (By.XPATH, './/input[@name="telephone"]')


class LocatorsYourPasswordComponent:
    """Locators fot the 'Your Password' component."""

    PASSWORD_FIELD = (By.XPATH, './/*[@name="password"]')
    PASSWORD_CONFIRM_FIELD = (By.XPATH, './/*[@name="confirm"]')


class LocatorsRegisterPage:
    """Locators fot the 'Register' page."""

    YOUR_PERSONAL_DETAILS_PARENT = (By.XPATH, '//*[@id="content"]')
    CHECKBOX_PRIVACY_POLICY = (By.NAME, 'agree')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')


class LocatorsNewsletterComponent:
    """Locators fot the 'Newsletter' component."""

    SUBSCRIBE_RADIO_BUTTONS = (By.XPATH, '//label[@class="radio-inline"]')


class LocatorsPrivacyPolicyComponent:
    """Locators fot the 'Privacy Policy' component."""

    PRIVACY_POLICY_CHECKBOX = (By.XPATH, '//input[@name="agree"]')


class LocatorsForgotPasswordPage:
    """Locators for the 'Forgot password' page."""

    EMAIL_FIELD = (By.ID, 'input-email')

    BACK_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@class="btn btn-primary"]')


class LocatorsChangePasswordPage:
    """Locators for the 'Change password' page."""

    BACK_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@class="btn btn-primary"]')


class LocatorSortByDropdown:
    SORT_BY = (By.XPATH, '//select[@id="input-sort"]')


class LocatorShowNumberProductsDropdown:
    SHOW_NUMBER_PRODUCTS = (By.XPATH, '//select[@id="input-limit"]')


class LocatorsAddAddressComponent:
    """Locators fot the 'Add Address' component."""
    FIRST_NAME_INPUT = (By.XPATH, './/input[@name="firstname"]')
    LAST_NAME_INPUT = (By.XPATH, './/input[@name="lastname"]')
    EMAIL_INPUT = (By.XPATH, ".//input[@name='email']")
    EMAIL_INPUT_PAYMENT = (By.XPATH, ".//input[@id='input-payment-email']")
    TELEPHONE_INPUT = (By.XPATH, ".//input[@name='telephone']")
    COMPANY_INPUT = (By.XPATH, './/input[@name="company"]')
    ADDRESS_1_INPUT = (By.XPATH, './/input[@name="address_1"]')
    ADDRESS_2_INPUT = (By.XPATH, './/input[@name="address_2"]')
    CITY_INPUT = (By.XPATH, './/input[@name="city"]')
    POST_CODE_INPUT = (By.XPATH, './/input[@name="postcode"]')
    COUNTRY_SELECTOR = (By.XPATH, './/select[@name="country_id"]')
    REGION_SELECTOR = (By.XPATH, './/select[@name="zone_id"]')


class LocatorsAddAddressPage:
    """Locators fot the 'Add Address' page."""
    ADDRESS_CONTENT = (By.ID, 'content')

    DEFAULT_ADDRESS_RADIO_CONTAINER = (By.XPATH, '//label[@class="radio-inline"]/..')
    BACK_BUTTON = (By.XPATH, '//a[text()="Back"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@value="Continue"]')


class LocatorsWishListPage:
    """Locators for the 'Wish List' page"""
    ITEMS = (By.XPATH, '//div/table/tbody/tr/td[@class="text-left"]//a')
    PRODUCT_NAME = (By.XPATH, '//td[@class="text-left"]//a')
    ADD_PRODUCT_TO_CARD = (By.XPATH, '../../td[@class="text-right"]/button[@class="btn btn-primary"]')
    DELETE_PRODUCT_FROM_CARD = (By.XPATH, '../../td[@class="text-right"]/a[@class="btn btn-danger"]')
    CONTINUE_BUTTON = (By.XPATH, '//div[@class="pull-right"]//a[@class="btn btn-primary"]')


class LocatorsGiftCertificatePage:
    """Locators for the 'Gift Certificate' page"""
    RECEPIENT_NAME = (By.XPATH, '//div[@class="col-sm-10"]//input[@name="to_name"]')
    RECEPIENT_EMAIL = (By.XPATH, '//div[@class="col-sm-10"]//input[@name="to_email"]')
    YOUR_NAME = (By.XPATH, '//div[@class="col-sm-10"]//input[@name="from_name"]')
    YOUR_EMAIL = (By.XPATH, '//div[@class="col-sm-10"]//input[@name="from_email"]')
    GIFT_CERTIFICATE_THEME = (By.XPATH, '//div[@class="radio"]//label')
    MESSAGE = (By.XPATH, '//div[@class="col-sm-10"]//textarea[@name="message"]')
    AMOUNT = (By.XPATH, '//div[@class="col-sm-10"]//input[@name="amount"]')
    AGREE = (By.XPATH, '//div[@class="pull-right"]//input[@name="agree"]')
    CONTINUE_BUTTON = (By.XPATH, '//div[@class="pull-right"]//input[@type="submit"]')


class LocatorsComparePage:
    """Locators for the 'Compare' page"""
    ITEMS = (By.XPATH, '//table[@class="table table-bordered"]/tbody/tr/td/a/strong')
    TABLE_ROW = (By.XPATH, '//table/tbody/tr')
    TABLE_COLUMN = (By.XPATH, 'td')
    ADD_BUTTONS = (By.CLASS_NAME, 'btn-primary')
    REMOVE_BUTTONS = (By.CLASS_NAME, 'btn-danger')


class LocatorsInfoMessages:
    """Locators to various messages on pages, for CatchMessageComponent."""
    ALERT_INFO_MESSAGE = (By.XPATH, '//div[@class="alert alert-info"]')
    ALERT_SUCCESS_MESSAGE = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')
    ALERT_DANGER_MESSAGE = (By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]')


class LocatorsShoppingCartPage:
    """Locators for 'Shopping Cart' page"""
    COUPON_FIELD = (By.ID, 'input-coupon')
    COUPON_APPLY_BUTTON = (By.ID, 'button-coupon')

    COUNTRY_SELECTOR = (By.ID, 'input-country')
    REGION_SELECTOR = (By.ID, 'input-zone')
    POST_CODE_FIELD = (By.ID, 'input-postcode')
    GET_QUOTES_BUTTON = (By.ID, 'button-quote')
    MODAL_SHIPPING_APPlY_BUTTON = (By.ID, 'button-shipping')

    CERTIFICATE_FIELD = (By.ID, 'input-voucher')
    CERTIFICATE_APPLY_BUTTON = (By.ID, 'button-voucher')

    PRODUCT_LINES = (By.XPATH, '//h1/following-sibling::form//tbody/tr')

    PRODUCT_NAME = (By.XPATH, './/td[2]/a')
    PRODUCT_MODEL = (By.XPATH, './/td[3]')
    PRODUCT_UNIT_PRICE = (By.XPATH, './/td[5]')
    PRODUCT_TOTAL_PRICE = (By.XPATH, './/td[6]')
    PRODUCT_QUANTITY = (By.XPATH, './/input')
    PRODUCT_UPDATE_QUANTITY_BUTTON = (By.XPATH, './/button[@data-original-title="Update"]')
    PRODUCT_REMOVE_BUTTON = (By.XPATH, './/button[@data-original-title="Remove"]')

    COUPON_PANEL = (By.XPATH, '//a[text() = "Use Coupon Code "]')
    ESTIMATE_SHIPPING_PANEL = (By.XPATH, '//a[text() = "Estimate Shipping & Taxes "]')
    GIFT_CERTIFICATE_PANEL = (By.XPATH, '//a[text() = "Use Gift Certificate "]')

    MODAL_SHIPPING_CANCEL_BUTTON = (By.XPATH, '//*[@id="modal-shipping"]//button[text()="Cancel"]')
    MODAL_SHIPPING_RADIO = (By.XPATH, '//div[@id="modal-shipping"]//div[@class="radio"]')

    CONTINUE_SHIPPING_BUTTON = (By.XPATH, '//a[text()="Continue Shopping"]')
    CHECKOUT_BUTTON = (By.XPATH, '//a[text()="Checkout"]')

    FLAT_SHIPPING_RATE = (By.XPATH, '//td/strong[text()="Flat Shipping Rate:"]/../following-sibling::td')
    COUPON_SUM = (By.XPATH, '//div[@id="checkout-cart"]//strong[starts-with(text(), "Coupon")]'
                            '/../following-sibling::td')
    GIFT_CERTIFICATE_SUM = (By.XPATH, '//div[@id="checkout-cart"]//strong[starts-with(text(), "Gift Certificate")]'
                                      '/../following-sibling::td')
    SUB_TOTAL_ORDER_SUM = (By.XPATH, '//td/strong[text()="Sub-Total:"]/../following-sibling::td')
    TOTAL_ORDER_SUM = (By.XPATH, '//td/strong[text()="Total:"]/../following-sibling::td')

    CONTENT_EMPTY_CART = (By.XPATH, '//div[@id="content"]/p[text()="Your shopping cart is empty!"]')


class LocatorsLoginComponent:
    """Locators for Login Component."""

    EMAIL_INPUT = (By.XPATH, '//input[@id="input-email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="input-password"]')
    FORGOTTEN_PASSWORD_BUTTON = (By.XPATH, '//a[text()="Forgotten Password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@type="submit"]')


class LocatorsCheckoutPage:
    """Locators for the 'Checkout' page."""
    BILLING_DETAILS_FORM = (By.ID, 'collapse-payment-address')

    REGISTER_CHECKOUT_RADIO_BUTTON = \
        (By.XPATH, "//div[@id='collapse-checkout-option']//div[@class='col-sm-6']//div[1]//label[1]//input[1]")
    GUEST_CHECKOUT_RADIO_BUTTON = (By.XPATH, "//div[@id='collapse-checkout-option']//div[2]//label[1]//input[1]")
    CHECKOUT_OPTIONS_CONTINUE_BUTTON = (By.XPATH, "//input[@id='button-account']")

    RETURNING_CUSTOMER_EMAIL_FIELD = (By.XPATH, '//input[@id="input-email"]')
    RETURNING_CUSTOMER_PASSWORD_FIELD = (By.XPATH, '//input[@id="input-password"]')
    FORGOTTEN_PASSWORD_LINK = (By.XPATH, '//a[contains(text(),"Forgotten Password")]')
    LOGIN_BUTTON = (By.XPATH, '//input[@id="button-login"]')

    ADD_ADDRESS_BILLING_DETAILS_PARENT = (By.ID, "address")
    BILLING_DETAILS_CONTINUE_BUTTON = (By.XPATH, "//input[@id='button-guest']")

    DELIVERY_AND_BILLING_ADDRESSES_CHECKBOX = (By.XPATH, '//input[@name="shipping_address"]')
    YOUR_ADDRESS_ACCOUNT_AND_BILLING_DETAILS_PARENT = (By.XPATH, '//*[@id="collapse-payment-address"]')
    NEWSLETTER_CHECKBOX = (By.XPATH, '//input[@id="newsletter"]')
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, '//div[@class="buttons clearfix"]//input[@name="agree"]')
    ACCOUNT_AND_BILLING_DETAILS_CONTINUE_BUTTON = (By.XPATH, '//input[@id="button-register"]')

    DELIVERY_DETAILS_PARENT = (By.ID, "collapse-shipping-address")

    DELIVERY_DETAILS_CONTINUE_BUTTON = (By.XPATH, '//*[@id="collapse-shipping-address"]//input[@value="Continue"]')

    DELIVERY_METHOD_TEXT_AREA = (By.XPATH, '//textarea[@name="comment"]')
    DELIVERY_METHOD_CONTINUE_BUTTON = (By.XPATH, '//input[@id="button-shipping-method"]')

    PAYMENT_METHOD_TEXT_AREA = (By.XPATH, '//div[@id="collapse-payment-method"]//textarea[@name="comment"]')
    TERMS_AND_CONDITIONS_CHECKBOX = (By.XPATH, '//input[@name="agree"]')
    PAYMENT_METHOD_CONTINUE_BUTTON = (By.XPATH, '//input[@id="button-payment-method"]')

    CONFIRM_ORDER_BUTTON = (By.XPATH, '//input[@id="button-confirm"]')


class LocatorsComparePageTest:
    MACBOOK = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[3]')
    IPHONE = (By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[3]/button[3]')
    CINEMA = (By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[3]/button[3]')
    MESSAGE = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')


class LocatorsShoppingCartPageTest:
    IPHONE = (By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[3]/button[1]')
    QUANTITY = (By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input')


class LocatorsLoginPage:
    FORGOTTEN_PASSWORD_BUTTON = (By.XPATH, '//div[@id="content"]//a[text()="Forgotten Password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@value="Login"]')
    REGISTER_PAGE_BUTTON = (By.XPATH, '//a[text()="Continue"]')