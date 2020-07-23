from .base_page import BasePage
from .product_page import ProductPage
from ..components import ProductWidgetComponent, ProductWidgetsListComponent


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._featured_products = ProductWidgetsListComponent(driver)
    
    def click_featured_product_title(self, product_name: str):
        for product in self._featured_products:
            if product.find_element_by_xpath('.//div[2]/h4/a').text == product_name:
                product.find_element_by_xpath('div[3]/button/i').click()
                if product_name == 'Apple Cinema 30"' or product_name == 'Canon EOS 5D':
                    return ProductPage(self._driver)
                else:
                    return self._driver
        return 'No product found'

    def add_featured_product_to_cart(self, product_name: str):
        product = ProductWidgetComponent(self._driver, product_name)
        product.click_add_to_shopping_cart_button()
        return self._driver

    def add_featured_product_to_wish_list(self, product_name: str):
        product = ProductWidgetComponent(self._driver, product_name)
        product.click_add_to_wish_list_button()
        return self._driver

    def add_featured_product_to_compare_list(self,name: str):
        product = ProductWidgetComponent(self._driver, name)
        product.click_add_to_compare_button()
        return self._driver





