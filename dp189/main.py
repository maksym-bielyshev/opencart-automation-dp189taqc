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
    product.available_options.click_add_to_cart_button()
