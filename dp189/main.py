from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from dp189.pages.shopping_cart_page import ShoppingCartPage
from selenium.webdriver.common.by import By


if __name__ == '__main__':

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    # driver = Chrome('C:/Users/Home/Downloads/chromedriver_win32/chromedriver.exe', options=options)
    driver = Chrome(options=options)
    driver.implicitly_wait(30)
    # driver.maximize_window()

from dp189.locators import LocatorsYourPersonalDetailsComponent
from dp189.pages.home_page import HomePage
from dp189.pages.register_page import RegisterPage

if __name__ == '__main__':
    options = Options()
    options.add_argument('--ignore-certificate-errors')

    with Chrome(options=options) as driver:
        driver.maximize_window()
        driver.get('http://34.71.14.206/index.php?route=account/register')

    driver.get('http://34.71.14.206/index.php?route=product/product&product_id=40')
    driver.find_element(By.ID, 'button-cart').click()
    driver.get('http://34.71.14.206/index.php?route=product/product&path=20&product_id=48')
    driver.find_element(By.ID, 'button-cart').click()
    driver.get('http://34.71.14.206/index.php?route=checkout/cart')
        register_page = RegisterPage(driver)
        register_page.your_personal_details_form.first_name_field.clear_and_fill_input_field(
            '111111111111111111111111111111111111111111111')
        register_page = register_page.click_continue_button()
        print(register_page.your_personal_details_form.first_name_field.get_error_message_for_input_field())

    cart = ShoppingCartPage(driver)

    cart.get_products_list()
    # cart.change_product_quantity('iPod Classic', 5)
    # driver.implicitly_wait(15)
    # print(cart.get_product_quantity('iPod Classic'))
    # print(cart.products_list)

    # cart.get_product_total_price(48)

    # txt = "http://34.71.14.206/index.php?route=product/product&product_id=42"
    # x = txt.rsplit("product_id=")
    # print(x[1])

        print(register_page.subscribe_radio_buttons.is_subscribed())
        register_page.subscribe_radio_buttons.subscribe_to_newsletter()
        print(register_page.subscribe_radio_buttons.is_subscribed())