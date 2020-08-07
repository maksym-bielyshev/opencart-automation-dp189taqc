from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.pages.product_page import ProductPage
from dp189.components import ProductWidgetComponent, ProductWidgetsListComponent
from dp189.locators import LocatorsHomePage


class HomePage(BasePage):
    """Home page class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize objects to work with this page.

        :param driver: Remote
        :return: None
        """
        super().__init__(driver)
        self.featured_products = ProductWidgetsListComponent(self._driver)
    
    def click_featured_product_title(self, product_name: str) -> object:
        """Click on featured product on Home page.

        :param product_name: str
        :return: object
        """
        for product in self.featured_products.get_list_product_widgets():
            if product.find_element(*LocatorsHomePage.PRODUCT_WIDGET_NAME).text == product_name:
                product.find_element(*LocatorsHomePage.PRODUCT_WIDGET_NAME).click()
                return ProductPage(self._driver)

    def add_featured_product_to_cart(self, product_name: str) -> None:
        """Click 'Add to Cart' button for adding featured product to Cart.

        :param product_name: str
        :return: None
        """
        product = ProductWidgetComponent(self._driver, product_name)
        product.click_add_to_shopping_cart_button()

    def add_featured_product_to_wish_list(self, product_name: str) -> None:
        """Click 'Add to Wish List' button for adding featured product to Wish List.

        :param product_name: str
        :return: None
        """
        product = ProductWidgetComponent(self._driver, product_name)
        product.click_add_to_wish_list_button()

    def add_featured_product_to_compare_list(self, product_name: str) -> None:
        """Click 'Compare this product' button for adding featured product to compare list.

        :param product_name: str
        :return: None
        """
        product = ProductWidgetComponent(self._driver, product_name)
        product.click_add_to_compare_button()
