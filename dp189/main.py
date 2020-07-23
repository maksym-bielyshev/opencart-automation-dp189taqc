from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dp189.pages.product_page import ProductPage


if __name__ == '__main__':
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    my_driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe', options=options)
    my_driver.get('http://34.71.14.206/index.php?route=product/product&path=20&product_id=62')
    my_driver.maximize_window()

    product = ProductPage(my_driver)
    product.available_options.radio.choose_radio_button_option('Medium')
    product.available_options.checkbox.choose_checkbox_option('Checkbox 3')
    product.available_options.select.choose_dropdown_option('Blue (+$3.00)')
    print(product.available_options.radio.which_option_is_chosen())
    print(product.available_options.checkbox.which_option_is_chosen())
    print(product.available_options.select.which_option_is_chosen())
