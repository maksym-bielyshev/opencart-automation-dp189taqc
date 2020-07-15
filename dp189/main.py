import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from dp189.pages.shopping_cart_page import ShoppingCartPage
from selenium.webdriver.common.by import By
from dp189.locators import LocatorsYourPersonalDetailsComponent
from dp189.pages.home_page import HomePage
from dp189.pages.register_page import RegisterPage


if __name__ == '__main__':

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    # driver = Chrome('C:/Users/Home/Downloads/chromedriver_win32/chromedriver.exe', options=options)
    driver = Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()

    driver.get('http://34.71.14.206/index.php?route=product/product&product_id=40')
    driver.find_element(By.ID, 'button-cart').click()
    driver.get('http://34.71.14.206/index.php?route=product/product&path=20&product_id=48')
    driver.find_element(By.ID, 'button-cart').click()
    driver.get('http://34.71.14.206/index.php?route=checkout/cart')

    cart = ShoppingCartPage(driver)
    # cart.coupon_panel.open_coupon_panel()
    # cart.coupon_panel.coupon_field.clear_and_fill_input_field("22222222")
    # cart.coupon_panel.click_apply_coupon_button()
    cart.get_products_list()
    # driver.implicitly_wait(15)
    print(cart.get_product_total_price('iPod Classic'))
    cart = cart.change_product_quantity('iPod Classic', 5)
    cart.get_products_list()
    # cart.get_products_list()

    print(cart.get_product_total_price('iPod Classic'))
    # print(cart.get_product_total_price('iPod Classic'))


