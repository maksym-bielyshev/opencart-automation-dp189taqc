from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dp189.pages.product_page import ProductPage


options = Options()
options.add_argument('--ignore-certificate-errors')


class TestAddProductToCart:

    def setup(self):
        self.my_driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe', options=options)
        self.my_driver.maximize_window()
        self.my_driver.get('http://34.71.14.206/index.php?route=product/product&path=20&product_id=62')
        self.apple = ProductPage(self.my_driver)

    def test_add_product_to_cart_with_all_selected_options(self):
        self.apple.available_options.radio.choose_radio_button_option('Medium')
        self.apple.available_options.checkbox.choose_checkbox_option('Checkbox 2')
        self.apple.available_options.text_field.clear_and_fill_input_field('test')
        self.apple.available_options.select.choose_dropdown_option('Blue (+$3.00)')
        self.apple.available_options.text_area_field.clear_and_fill_input_field('Test text')
        self.apple.available_options.data_field.clear_and_fill_input_field('2020-07-19')
        self.apple.available_options.time.clear_and_fill_input_field('23:23')

        self.apple.available_options.click_add_to_cart_button()

        success_message = 'Success: You have added Apple Cinema 24 to your shopping cart!'
        assert success_message in self.apple.catch_info_message.get_info_message()

    def test_add_product_to_cart_with_selected_option_color(self):
        self.apple.available_options.select.choose_dropdown_option('Blue (+$3.00)')

        self.apple.available_options.select.option_is_checked('Blue (+$3.00)')
        assert True

    def teardown(self):
        self.my_driver.close()
