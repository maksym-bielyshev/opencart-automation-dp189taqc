from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dp189.pages.product_page import ProductPage


options = Options()
options.add_argument('--ignore-certificate-errors')


class BaseTest:

    def setup(self):
        self.my_driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe', options=options)
        self.my_driver.maximize_window()
        self.my_driver.get('http://34.71.14.206/index.php?route=product/product&path=20&product_id=62')
        self.apple = ProductPage(self.my_driver)

    def teardown(self):
        self.my_driver.close()


class TestAddProductToCart(BaseTest):

    def test_add_product_to_cart_with_all_selected_options(self):
        # TODO DPOC-109
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
        # TODO Add to story Automate DPOC-94
        self.apple.available_options.select.choose_dropdown_option('Blue (+$3.00)')

        self.apple.available_options.select.option_is_checked('Blue (+$3.00)')
        assert True


class TestAddReviewToProduct(BaseTest):

    def test_add_review_to_product(self):
        # TODO Change and add to story DPOC-2
        self.apple.click_reviews_tab()
        self.apple.reviews_tab.your_name.clear_and_fill_input_field('Maksym')
        self.apple.reviews_tab.your_review.clear_and_fill_input_field('Some text for review field.')
        self.apple.reviews_tab.choose_review_rating(5)
        self.apple.reviews_tab.click_review_continue_button()

        info_message = 'Thank you for your review. It has been submitted to the webmaster for approval.'

        assert info_message == self.apple.catch_info_message.get_info_message()


class TestProductButtons(BaseTest):

    def test_click_compare_button(self):
        self.apple.click_compare_this_product_button()

        info_message = 'Success: You have added Apple Cinema 24 to your product comparison!'

        assert info_message in self.apple.catch_info_message.get_info_message()

    def test_click_add_to_wish_list_as_not_logged_user(self):
        self.apple.click_add_to_wish_list_button()

        info_message = 'You must login or create an account to save Apple Cinema 24 to your wish list!'

        assert info_message in self.apple.catch_info_message.get_info_message()

