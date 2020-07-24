PROTOCOL = 'http:'
DOMAIN = '//34.71.14.206'
ROUTE_PRODUCT = '/index.php?route=product'
ROUTE_CHECKOUT = '/index.php?route=checkout'
ROUTE_ACCOUNT = '/index.php?route=account'

HOME_PAGE = PROTOCOL + DOMAIN + '/index.php?route=common/home'

CART = PROTOCOL + DOMAIN + ROUTE_CHECKOUT + '/cart'
CHECKOUT = PROTOCOL + DOMAIN + ROUTE_CHECKOUT + '/checkout'

WISH_LIST = PROTOCOL + DOMAIN + ROUTE_ACCOUNT + '/wishlist'
REGISTER = PROTOCOL + DOMAIN + ROUTE_ACCOUNT + '/register'
LOGIN = PROTOCOL + DOMAIN + ROUTE_ACCOUNT + '/login'
ACCOUNT = PROTOCOL + DOMAIN + ROUTE_ACCOUNT + '/account'
EDIT_ACCOUNT = PROTOCOL + DOMAIN + ROUTE_ACCOUNT + '/edit'
PASSWORD = PROTOCOL + DOMAIN + ROUTE_ACCOUNT + '/password'
ADDRESS = PROTOCOL + DOMAIN + ROUTE_ACCOUNT + '/address'
ADDRESS_ADD = PROTOCOL + DOMAIN + ROUTE_ACCOUNT + '/address/add'
ORDER_HISTORY = PROTOCOL + DOMAIN + ROUTE_ACCOUNT + '/order'
LOGOUT = PROTOCOL + DOMAIN + ROUTE_ACCOUNT + '/logout'
GIFT_CERTIFICATE = PROTOCOL + DOMAIN + ROUTE_ACCOUNT + '/voucher'


def get_product_url(product_id):
    return PROTOCOL + DOMAIN + ROUTE_PRODUCT + f'/product&product_id={product_id}'


def get_search_page_url(search_query):
    return PROTOCOL + DOMAIN + ROUTE_PRODUCT + f'/search&search={search_query}'


def get_category_url(category_id):
    return PROTOCOL + DOMAIN + ROUTE_PRODUCT + f'/category&path={category_id}'


def get_edit_address_url(address_id):
    return ADDRESS + f'/edit&address_id={address_id}'