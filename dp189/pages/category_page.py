from dp189.pages.base_page import BasePage
from dp189.components import LeftCategoryMenuComponent, SortByDropdownComponent, ShowNumberProductsDropdownComponent
from dp189.locators import LocatorCategoryProducts


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.category_title = driver.find_element_by_id("content")
        self.list_view = driver.find_element_by_id("list-view")
        self.grid_view = driver.find_element_by_id("grid-view")

        self.left_category_menu = LeftCategoryMenuComponent
        self.sort_by = SortByDropdownComponent
        self.show_number_products = ShowNumberProductsDropdownComponent
        self.list_of_products = LocatorCategoryProducts

    def click_list_view(self):
        self.list_view.click()

    def click_grid_view(self):
        self.grid_view.click()

    def click_click_left_menu_category_title(self):
        pass

    def click_sort_by(self):
        pass

    def click_show_number_products(self):
        pass

    def get_list_of_products(self):
        pass
