from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from dp189.pages.home_page import HomePage
from dp189.components import ProductWidgetComponent

options = Options()
options.add_argument('--ignore-certificate-errors')

# driver = Chrome(options=options)
with Chrome(options=options) as driver:

    driver.maximize_window()

    driver.get('http://34.71.14.206/index.php?route=common/home')

    macbook = ProductWidgetComponent(driver, 'MacBook')
    macbook.add_to_shopping_cart()

    iphone = ProductWidgetComponent(driver, 'iPhone')
    iphone.add_to_wish_list()

    apple_cinema = ProductWidgetComponent(driver, 'Apple Cinema 30"')
    apple_cinema.add_to_compare_button()

    # driver.implicitly_wait(15)

    # page = HomePage(driver)
    # page.add_product_to_cart('iPhone')
    # login_page = page.click_account_and_go_to_login()
    # login_page.login('smith@mail.com','12345')


