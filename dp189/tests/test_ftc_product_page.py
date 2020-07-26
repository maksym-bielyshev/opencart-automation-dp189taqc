from dp189.tests.base_test import *
from dp189.pages.product_page import ProductPage


class TestAvailableOptions(BaseTest):
    """Tests for Available Options menu on product page."""

    def setup(self):
        """Create initial state of driver on ProductPage."""
        self.driver.get('http://34.71.14.206/index.php?route=product/product&path=20&product_id=62')
        self.driver.maximize_window()
        self.product_page = ProductPage(self.driver)

    def test_add_product_to_cart_button_with_all_selected_options(self):
        """Check correct work of clicking on 'Add to Cart' button by filling all required fields."""

        self.product_page.available_options.radio.choose_radio_button_option('Medium')
        self.product_page.available_options.checkbox.choose_checkbox_option('Checkbox 2')
        self.product_page.available_options.text_field.clear_and_fill_input_field('test')
        self.product_page.available_options.select.choose_dropdown_option('Blue (+$3.00)')
        self.product_page.available_options.text_area_field.clear_and_fill_input_field('Test text')
        self.product_page.available_options.data_field.clear_and_fill_input_field('2020-07-19')
        self.product_page.available_options.time.clear_and_fill_input_field('23:23')

        self.product_page.available_options.click_add_to_cart_button()

        success_message = 'Success: You have added Apple Cinema 24 to your shopping cart!'
        assert success_message in self.product_page.catch_info_message.get_info_message()

    def test_choose_radio_option(self):
        """Check correct work of clicking on specific option of radio button."""

        self.product_page.available_options.radio.choose_radio_button_option('Medium')

        radio = 'Medium (+$20.00)'

        assert radio == self.product_page.available_options.radio.which_option_is_chosen()


class TestReviewsTab(BaseTest):
    """Tests for Reviews Tab on Product page."""

    def setup(self):
        """Create initial state of driver on ProductPage."""
        self.driver.get('http://34.71.14.206/index.php?route=product/product&path=20&product_id=62')
        self.driver.maximize_window()
        self.product_page = ProductPage(self.driver)

    def test_add_review_to_product(self):
        """Fill all required fields for adding review on product page."""
        self.product_page.click_reviews_tab()
        self.product_page.reviews_tab.your_name.clear_and_fill_input_field('Maksym')
        self.product_page.reviews_tab.your_review.clear_and_fill_input_field('Some text for review field.')
        self.product_page.reviews_tab.choose_review_rating(5)
        self.product_page.reviews_tab.click_review_continue_button()

        info_message = 'Thank you for your review. It has been submitted to the webmaster for approval.'

        assert info_message == self.product_page.catch_info_message.get_info_message()


class TestProductPageButtons(BaseTest):
    """Tests for checking correct work of buttons on product page."""

    def setup(self):
        """Create initial state of driver on ProductPage."""
        self.driver.get('http://34.71.14.206/index.php?route=product/product&path=20&product_id=62')
        self.driver.maximize_window()
        self.product_page = ProductPage(self.driver)

    def test_click_compare_button(self):
        """Check correct work of clicking on 'Compare this product' button."""
        self.product_page.click_compare_this_product_button()

        info_message = 'Success: You have added Apple Cinema 24 to your product comparison!'

        assert info_message in self.product_page.catch_info_message.get_info_message()

    def test_click_add_to_wish_list_as_not_logged_user(self):
        """Check correct work of clicking 'Add to Wish List' button."""
        self.product_page.click_add_to_wish_list_button()

        info_message = 'You must login or create an account to save Apple Cinema 24 to your wish list!'

        assert info_message in self.product_page.catch_info_message.get_info_message()
