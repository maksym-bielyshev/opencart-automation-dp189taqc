"""Category page."""

from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.components import ProductsViewModeComponent, ProductWidgetComponent, ProductCompareLinkComponent, \
    ProductWidgetsListComponent, DropdownComponent
from dp189.locators import LocatorCategoryTitle, LocatorSortByDropdown, LocatorShowNumberProductsDropdown


class CategoryPage(BasePage):
    """Category page class."""

    def __init__(self, driver: Remote) -> None:
        """All objects on the category page.

        :param driver: Remote driver.
        """
        super().__init__(driver)
        self.category_title = driver.find_element(*LocatorCategoryTitle.CATEGORY_TITLE)
        self.products_view_button = ProductsViewModeComponent(driver)
        self.product_compare_link = ProductCompareLinkComponent(driver)
        self.sort_by_dropdown = DropdownComponent(driver, LocatorSortByDropdown.SORT_BY)
        self.show_number_products_dropdown = DropdownComponent(driver,
                                                               LocatorShowNumberProductsDropdown.SHOW_NUMBER_PRODUCTS)
        self.product_compare_link = ProductCompareLinkComponent(driver)
        self.product_widget_list = ProductWidgetsListComponent(driver)
