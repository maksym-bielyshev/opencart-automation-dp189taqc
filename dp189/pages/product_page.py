"""
This module describes the operation of all the page methods of a specific product page.
Each field or button of the product page can be called using a separate method.
"""
from selenium.webdriver.common.by import By
from dp189.pages.base_page import BasePage
from dp189.locators import LocatorsProductPage, LocatorsAvailableOptions, LocatorsShoppingCartButton
from selenium.webdriver import Remote
import re
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage(BasePage):
    """Description of the basic methods of working with the Product Page and
    the ability to select a separate product tab, such as Description Tab,
    Specification Tab and Reviews Tab.
    """

    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self.review_tab = ReviewTab(driver)
        self.available_options = AvailableOptions(driver)

    def click_description_tab(self) -> None:
        """Go to the Description tab on the specific product page."""
        self._driver.find_element(*LocatorsProductPage.DESCRIPTION_TAB).click()

    def click_specification_tab(self) -> None:
        """Go to the Specification tab on the specific product page."""
        self._driver.find_element(*LocatorsProductPage.SPECIFICATION_TAB).click()

    def click_reviews_tab(self) -> None:
        """Go to the Reviews tab on the specific product page."""
        self._driver.find_element(*LocatorsProductPage.REVIEW_TAB).click()

    def click_product_photo(self) -> None:
        """Click the main product photo."""
        self._driver.find_element(*LocatorsProductPage.PHOTO).click()

    def switch_to_next_photo(self) -> None:
        """Switch to the next product photo."""
        self._driver.find_element(*LocatorsProductPage.NEXT_PHOTO).click()

    def switch_to_previous_photo(self) -> None:
        """Switch to the previous product photo."""
        self._driver.find_element(*LocatorsProductPage.PREVIOUS_PHOTO).click()

    def click_add_to_wish_list_button(self) -> None:
        """Add specific product to Wish List."""
        self._driver.find_element(*LocatorsProductPage.ADD_TO_WISH_LIST).click()

    def click_compare_this_product_button(self) -> None:
        """Add product to the list of products for comparison."""
        self._driver.find_element(*LocatorsProductPage.COMPARE_THIS_PRODUCT).click()

    def get_product_cost_without_options(self) -> float:
        cost_path = WebDriverWait(self._driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, "//ul//li[contains(.,'Ex Tax')]/../li/h2")))
        cost_value = re.findall(r"\d+\.\d+", cost_path.text)
        return float("".join(cost_value))

    def get_product_total_cost(self) -> float:
        """Get total cost of specific product including all added available options."""
        total_cost_path = self._driver.find_element(*LocatorsShoppingCartButton.SHOP_CART_BUTTON)
        total_cost_value = re.findall(r"\d+\.\d+", total_cost_path.text)
        return float("".join(total_cost_value))


class AvailableOptions:
    """This class describes the methods of the right block of the product page.
    In this block there are methods to fill all the fields and buttons for
    adding specific product to the Shopping Cart.
    """

    def __init__(self, driver: Remote):
        self._driver = driver
        self._all_options = driver.find_element(*LocatorsAvailableOptions.ALL_OPTIONS)
        self.data_options = dict()

    def choose_radio_button(self, radio_option: str) -> dict:
        """
        Choose the radio button of specific product.
        There are following acceptable radio buttons for choosing:
        Small, Medium, Large
        """
        radio = self._driver.find_element(By.XPATH, f"//*[text()[contains(.,'{radio_option}')]]")
        radio.click()
        radio_name = radio.text.split()[0]
        self.data_options[radio_name] = float("".join(re.findall(r"\d+\.\d+", radio.text)))
        return self.data_options

    def choose_checkbox(self, checkbox_number: int) -> dict:
        """
        Choose the number of checkbox.
        There are following acceptable numbers for choosing: 1, 2, 3, 4.
        """
        checkboxes = self._driver.find_element(*LocatorsAvailableOptions.CHECKBOX_GROUP)
        checkbox = checkboxes.find_element(By.XPATH, f'./../div[{checkbox_number}]/label')
        checkbox.click()
        checkbox_name = str(checkbox.text.split()[0] + " " + checkbox.text.split()[1])
        self.data_options[checkbox_name] = float("".join(re.findall(r"\d+\.\d+", checkbox.text)))
        return self.data_options

    def fill_text_field(self, user_input: str) -> None:
        """Fill 'text' field in the available options."""
        self._driver.find_element(*LocatorsAvailableOptions.TEXT_FIELD).clear()
        self._driver.find_element(*LocatorsAvailableOptions.TEXT_FIELD).send_keys(user_input)

    def choose_color_in_drop_down_list(self, input_data: str) -> dict:
        """
        Choose the color of specific product after clicking
        'Please Select' button in the drop down menu.
        There are following acceptable colors for choosing:
        Green, Yellow, Blue, Red
        """
        self._all_options.find_elements(By.TAG_NAME, 'select')[0].click()
        color = self._driver.find_element(By.XPATH, f"//*[text()[contains(.,'{input_data}')]]")
        color.click()
        color_name = color.text.split()[0]
        self.data_options[color_name] = float("".join(re.findall(r"\d+\.\d+", color.text)))
        return self.data_options

    def fill_text_area_field(self, user_input: str) -> None:
        """Fill 'text area' field in the available options."""
        self._all_options.find_elements(By.TAG_NAME, "textarea")[0].send_keys(user_input)

    def upload_file(self):
        """Upload file before adding product to cart."""
        upload = self._driver.find_element(*LocatorsAvailableOptions.UPLOAD_FILE)
        upload.send_keys("D:\\Maksim\\test.txt")

    def fill_date_field(self, input_date: str) -> None:
        """
        Fill <date> field in the available options in the following format:
        <YYYY-MM-DD>
        For example: '2020-07-10'
        """
        self._driver.find_element(*LocatorsAvailableOptions.DATE).clear()
        self._driver.find_element(*LocatorsAvailableOptions.DATE).send_keys(input_date)

    def fill_time_field(self, input_time: str) -> None:
        """
        Fill <time> field in the available options in the following format:
        <HH:mm>
        For example: '22:59'
        """
        self._driver.find_element(*LocatorsAvailableOptions.TIME).clear()
        self._driver.find_element(*LocatorsAvailableOptions.TIME).send_keys(input_time)

    def fill_date_and_time_field(self, input_date_and_time: str) -> None:
        """
        Fill <date> and <time> field in the available options in the following format:
        <YYYY-MM-DD HH:mm>
        For example: '2020-07-10 22:35'
        """
        self._driver.find_element(*LocatorsAvailableOptions.DATE_AND_TIME).clear()
        self._driver.find_element(*LocatorsAvailableOptions.DATE_AND_TIME).send_keys(input_date_and_time)

    def fill_quantity_field(self, user_input: int) -> None:
        """Fill <quantity> field entering an integer value in the available options."""
        self._driver.find_element(*LocatorsAvailableOptions.QUANTITY).clear()
        self._driver.find_element(*LocatorsAvailableOptions.QUANTITY).send_keys(user_input)

    def click_add_to_cart(self) -> None:
        """Add specific product to Shopping Cart."""
        self._driver.find_element(*LocatorsAvailableOptions.ADD_TO_CART).click()


class ReviewTab:
    """
    This class describes the methods of the Reviews Tab of the Product page.
    User fills in the fields required information to send review about
     specific product and puts the rating on the product.
    """

    def __init__(self, driver):
        self._driver = driver

    def fill_your_name_field(self, user_input: str) -> None:
        """Fill 'Your Name' field in the Reviews Tab."""
        self._driver.find_element(*LocatorsProductPage.YOUR_NAME).clear()
        self._driver.find_element(*LocatorsProductPage.YOUR_NAME).send_keys(user_input)

    def fill_your_review_field(self, review_input: str) -> None:
        """Fill 'Your Review' field in the Reviews Tab."""
        self._driver.find_element(*LocatorsProductPage.YOUR_REVIEW).send_keys(review_input)

    def choose_review_rating(self, rating: int) -> None:
        """Choose review rating about product by clicking the button."""
        self._driver.find_element(By.XPATH, f".//input [@name='rating'][@value='{rating}']").click()

    def click_review_continue_button(self) -> None:
        """Click 'Continue' button in Reviews Tab"""
        self._driver.find_element(*LocatorsProductPage.CONTINUE).click()
