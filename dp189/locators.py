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


class LocatorsShoppingCartPage:
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
    # PRODUCT_LINES = (By.CSS_SELECTOR, 'h1 ~ form tbody tr')

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

    CONTINUE_SHIPPING_BUTTON = (By.XPATH, '//a[text()="Continue Shopping"]')
    CHECKOUT_BUTTON = (By.XPATH, '//a[text()="Checkout"]')

    FLAT_SHIPPING_RATE = (By.XPATH, '//td/strong[text()="Flat Shipping Rate:"]/../following-sibling::td')
    COUPON_SUM = (By.XPATH, '//div[@id="checkout-cart"]//strong[starts-with(text(), "Coupon")]'
                            '/../following-sibling::td')
    SUB_TOTAL_ORDER_SUM = (By.XPATH, '//td/strong[text()="Sub-Total:"]/../following-sibling::td')
    TOTAL_ORDER_SUM = (By.XPATH, '//td/strong[text()="Total:"]/../following-sibling::td')