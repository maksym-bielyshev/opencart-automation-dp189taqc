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
    # cart.get_products_list()

    # cart.estimate_shipping_panel.open_estimate_shipping_panel()
    # cart.coupon_panel.open_coupon_panel()
    # cart.coupon_panel.coupon_field.clear_and_fill_input_field("2222")
    # driver.implicitly_wait(30)
    cart.gift_certificate_panel.open_gift_certificate_panel()
    # cart.estimate_shipping_panel.region_selector.choose_dropdown_option("Kyiv")
    # cart.estimate_shipping_panel.post_code_field.clear_and_fill_input_field("1111")
    # cart.estimate_shipping_panel.click_get_quotes_button()
    # cart.estimate_shipping_panel.modal_shipping_radio_button.choose_radio_button_option("Flat Shipping Rate - $5.00")
    # cart.estimate_shipping_panel.click_modal_shipping_apply_button()
    # print(cart.get_product_total_price('iPod Classic'))
    # cart = cart.change_product_quantity('iPod Classic', 5)
    # cart.get_products_list()
    # # cart.get_products_list()
    #
    # print(cart.get_product_total_price('iPod Classic'))
    # print(cart.get_product_total_price('iPod Classic'))


