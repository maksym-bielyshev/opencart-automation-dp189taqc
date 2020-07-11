"""Category page."""

from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.components import LeftCategoryMenuComponent, SortByDropdownComponent, ShowNumberProductsDropdownComponent, \
    ListViewComponent, GridViewComponent, CategoryProductWidgetComponent, ProductCompareLinkComponent


class CategoryPage(BasePage):
    """Category page class."""

    def __init__(self, driver: Remote) -> None:
        """All objects on product page.

        :param driver: Remote
        """
        super().__init__(driver)
        self.category_title = driver.find_element_by_id("content")
        self.left_category_menu = LeftCategoryMenuComponent(driver)
        self.list_view = ListViewComponent(driver)
        self.grid_view = GridViewComponent(driver)
        self.product_compare_link = ProductCompareLinkComponent(driver)
        self.sort_by = SortByDropdownComponent(driver)
        self.show_number_products = ShowNumberProductsDropdownComponent(driver)
        self.product = CategoryProductWidgetComponent(driver, None)
