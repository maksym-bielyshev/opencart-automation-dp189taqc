from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.components import ProductsViewModeComponent, ProductCompareLinkComponent, \
    ProductWidgetsListComponent, DropdownComponent
from dp189.locators import LocatorCategoryTitle, LocatorSortByDropdown, LocatorShowNumberProductsDropdown


class CategoryPage(BasePage):
    """Category page class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize object to work with this page.

        :param driver: Remote
        :return: None
        """
        super().__init__(driver)
        self.category_title = driver.find_element(*LocatorCategoryTitle.CATEGORY_TITLE)
        self.products_view_button = ProductsViewModeComponent(self._driver)
        self.product_compare_link = ProductCompareLinkComponent(self._driver)
        self.sort_by_dropdown = DropdownComponent(self._driver, LocatorSortByDropdown.SORT_BY)
        self.show_number_products_dropdown = DropdownComponent(self._driver,
                                                               LocatorShowNumberProductsDropdown.SHOW_NUMBER_PRODUCTS)
        self.product_compare_link = ProductCompareLinkComponent(self._driver)
        self.product_widget_list = ProductWidgetsListComponent(self._driver)
