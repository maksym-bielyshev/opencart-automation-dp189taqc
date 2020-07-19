from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
        self._product_generator = (product for product in driver.find_elements_by_class_name('product-thumb'))
    
    def info(self):
        print(self._product_generator)
    
    def add_product_to_cart(self, item: str):
        for product in self._product_generator:
            if product.find_element_by_xpath('.//div[2]/h4/a').text == item:
                product.find_element_by_xpath('div[3]/button/i').click()
                if item == 'Apple Cinema 30"' or item == 'Canon EOS 5D':
                    pass
                    #return ProductPage(self._driver)
                else:
                    pass
                    #return self._driver
        #return 'No product found'
