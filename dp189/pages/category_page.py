"""Category page."""

from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.components import SortByDropdownComponent, ShowNumberProductsDropdownComponent, \
    ProductsViewModeComponent, ProductWidgetComponent, ProductCompareLinkComponent, ProductWidgetsListComponent
from dp189.locators import LocatorCategoryTitle


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
        self.sort_by_dropdown = SortByDropdownComponent(driver)
        self.show_number_products_dropdown = ShowNumberProductsDropdownComponent(driver)
        self.product_widget_list = ProductWidgetsListComponent(driver)
