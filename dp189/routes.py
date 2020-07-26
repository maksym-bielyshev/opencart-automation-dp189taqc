PROTOCOL = 'http:'
DOMAIN = '//34.71.14.206'
ROUTE_PRODUCT = '/index.php?route=product'
ROUTE_CHECKOUT = '/index.php?route=checkout'
ROUTE_ACCOUNT = '/index.php?route=account'

HOME_PAGE_URL = f'{PROTOCOL}{DOMAIN}/index.php?route=common/home'

CART_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_CHECKOUT}/cart'
CHECKOUT_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_CHECKOUT}/checkout'

REGISTER_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_ACCOUNT}/register'
LOGIN_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_ACCOUNT}/login'
ACCOUNT_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_ACCOUNT}/account'
EDIT_ACCOUNT_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_ACCOUNT}/edit'
CHANGE_PASSWORD_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_ACCOUNT}/password'
ADDRESS_BOOK_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_ACCOUNT}/address'
ADDRESS_ADD_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_ACCOUNT}/address/add'
WISH_LIST_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_ACCOUNT}/wishlist'
ORDER_HISTORY_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_ACCOUNT}/order'
LOGOUT_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_ACCOUNT}/logout'
GIFT_CERTIFICATE_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_ACCOUNT}/voucher'

COMPARE_PAGE_URL = f'{PROTOCOL}{DOMAIN}{ROUTE_PRODUCT}/compare'


def get_product_url(product_id: str) -> str:
    return f'{PROTOCOL}{DOMAIN}{ROUTE_PRODUCT}/product&product_id={product_id}'


def get_search_page_url(search_query: str) -> str:
    return f'{PROTOCOL}{DOMAIN}{ROUTE_PRODUCT}/search&search={search_query}'


def get_category_url(category_id: str) -> str:
    return f'{PROTOCOL}{DOMAIN}{ROUTE_PRODUCT}/category&path={category_id}'


def get_edit_address_url(address_id: str) -> str:
    return f'{ADDRESS_BOOK_PAGE_URL}/edit&address_id={address_id}'
