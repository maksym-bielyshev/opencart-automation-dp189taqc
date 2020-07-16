"""
This module describes the work of all page methods of a specific product page.
Each field or button of the product page can be called using a separate method.
"""

from selenium.webdriver.common.by import By
from dp189.pages.base_page import BasePage
from dp189.locators import LocatorsProductPage, LocatorsReviewsTab, LocatorsAvailableOptions, LocatorsShoppingCartButton
from dp189.components import InputFieldComponent, RadioComponent, CheckboxComponent, SelectComponent
from selenium.webdriver import Remote
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    """Description of the basic methods of working with the Product Page.
    Select a separate product tab, such as Description Tab,
    Specification Tab and Reviews Tab.
    """

    def __init__(self, driver: Remote):
        """Initialize objects to work with this page.

        :param driver: Remote
        """
        super().__init__(driver)
        self.reviews_tab = ReviewsTab(driver)
        self.available_options = AvailableOptions(driver)

    def click_description_tab(self) -> None:
        """Go to the Description tab on the specific product page.

        :return: None
        """
        self._driver.find_element(*LocatorsProductPage.DESCRIPTION_TAB).click()

    def click_specification_tab(self) -> None:
        """Go to the Specification tab on the specific product page.

        :return: None
        """
        self._driver.find_element(*LocatorsProductPage.SPECIFICATION_TAB).click()

    def click_reviews_tab(self) -> None:
        """Go to the Reviews tab on the specific product page.

        :return: None
        """
        self._driver.find_element(*LocatorsProductPage.REVIEWS_TAB).click()

    def click_product_photo(self) -> None:
        """Click the main product photo.

        :return: None
        """
        self._driver.find_element(*LocatorsProductPage.PHOTO).click()

    def close_product_photo(self) -> None:
        """Close the product photo.

        :return: None
        """
        self._driver.find_element(*LocatorsProductPage.CLOSE_PHOTO).click()

    def switch_to_next_photo(self) -> None:
        """Switch to the next product photo.

        :return: None
        """
        self._driver.find_element(*LocatorsProductPage.NEXT_PHOTO).click()

    def switch_to_previous_photo(self) -> None:
        """Switch to the previous product photo.

        :return: None
        """
        self._driver.find_element(*LocatorsProductPage.PREVIOUS_PHOTO).click()

    def click_add_to_wish_list_button(self) -> None:
        """Add specific product to Wish List.

        :return: None
        """
        self._driver.find_element(*LocatorsProductPage.ADD_TO_WISH_LIST).click()

    def click_compare_this_product_button(self) -> None:
        """Add product to the list of products for comparison.

        :return: None
        """
        self._driver.find_element(*LocatorsProductPage.COMPARE_THIS_PRODUCT).click()

    def get_product_cost_without_options(self) -> float:
        """Get basic product cost.

        :return: float
        """
        cost_path = self._driver.find_element(*LocatorsProductPage.EX_TAX)
        cost_value = re.findall(r'\d+\.\d+', cost_path.text)
        return float(''.join(cost_value))

    def get_product_total_cost(self) -> float:
        """Get product total cost including all added available options.

        :return: float
        """
        total_cost_path = self._driver.find_element(*LocatorsShoppingCartButton.SHOP_CART_BUTTON)
        total_cost_value = re.findall(r'\d+\.\d+', total_cost_path.text)
        return float(''.join(total_cost_value))


class AvailableOptions:
    """This class describes the methods of the right block of the product page.
    In this block there are methods to fill all the fields and buttons for
    adding specific product to the Shopping Cart.
    """

    def __init__(self, driver: Remote):
        """Initialize methods to work with available options.

        :param driver: Remote
        """
        self._driver = driver
        self._all_options = driver.find_element(*LocatorsAvailableOptions.ALL_OPTIONS)
        self.text_field = InputFieldComponent(self._driver, LocatorsAvailableOptions.TEXT_FIELD)
        self.text_area_field = InputFieldComponent(self._driver, LocatorsAvailableOptions.TEXT_AREA)
        self.data_field = InputFieldComponent(self._driver, LocatorsAvailableOptions.DATE)
        self.time = InputFieldComponent(self._driver, LocatorsAvailableOptions.TIME)
        self.date_and_time = InputFieldComponent(self._driver, LocatorsAvailableOptions.DATE_AND_TIME)
        self.quantity = InputFieldComponent(self._driver, LocatorsAvailableOptions.QUANTITY)
        self.radio = RadioComponent(self._driver, LocatorsAvailableOptions.RADIO_CONTAINER)
        self.checkbox = CheckboxComponent(self._driver, LocatorsAvailableOptions.CHECKBOX_CONTAINER)
        self.select = SelectComponent(self._driver, LocatorsAvailableOptions.SELECT_CONTAINER)

    def click_add_to_cart_button(self) -> None:
        """Add specific product to Shopping Cart.

        :return: None
        """
        self._driver.find_element(*LocatorsAvailableOptions.ADD_TO_CART).click()


class ReviewsTab:
    """This class describes the methods of the Reviews Tab of the Product page.
    User fills in the fields required information to send review about
    specific product and puts the rating on the product.
    """

    def __init__(self, driver):
        """Initialise a driver in Reviews Tab.

        :param driver: Remote
        """
        self._driver = driver

    def fill_your_name_field(self, input_your_name: str) -> None:
        """Fill 'Your Name' field in Reviews Tab.

        :param input_your_name: str
        :return: None
        """
        self._driver.find_element(*LocatorsReviewsTab.YOUR_NAME).clear()
        self._driver.find_element(*LocatorsReviewsTab.YOUR_NAME).send_keys(input_your_name)

    def fill_your_review_field(self, input_your_review: str) -> None:
        """Fill 'Your Review' field in Reviews Tab.

        :param input_your_review: str
        :return: None
        """
        self._driver.find_element(*LocatorsReviewsTab.YOUR_REVIEW).send_keys(input_your_review)

    def choose_review_rating(self, rating: int) -> None:
        """Choose review rating about product by clicking the button.

        :param rating: int
        :return: None
        """
        self._driver.find_element(By.XPATH, f'.//input [@name="rating"][@value="{rating}"]').click()

    def get_error_message_in_review_tab(self) -> str:
        """Get error message for review input fields if it were incorrect data.

        :return: str
        """
        error_message = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(LocatorsReviewsTab.REVIEW_ERROR_MESSAGE))
        return error_message.text

    def click_review_continue_button(self) -> None:
        """Click 'Continue' button in Reviews Tab.

        :return: None
        """
        self._driver.find_element(*LocatorsReviewsTab.CONTINUE).click()
