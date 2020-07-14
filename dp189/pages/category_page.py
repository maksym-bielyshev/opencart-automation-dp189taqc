"""Category page."""

from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.components import SortByDropdownComponent, ShowNumberProductsDropdownComponent, \
    ListViewComponent, GridViewComponent, CategoryProductWidgetComponent, ProductCompareLinkComponent, \
    ListProductWidgetsComponent
from dp189.locators import LocatorCategoryTitle


class CategoryPage(BasePage):
    """Category page class."""

    def __init__(self, driver: Remote) -> None:
        """All objects on the category page.

        :param driver: Remote driver.
        """
        super().__init__(driver)
        self.category_title = driver.find_element(*LocatorCategoryTitle.CATEGORY_TITLE)
        self.list_view = ListViewComponent(driver)
        self.grid_view = GridViewComponent(driver)
        self.product_compare_link = ProductCompareLinkComponent(driver)
        self.sort_by = SortByDropdownComponent(driver)
        self.show_number_products = ShowNumberProductsDropdownComponent(driver)


if __name__ == "__main__":
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = Chrome(options=options)
    driver.maximize_window()

    driver.get('http://34.71.14.206/index.php?route=information/sitemap')

    ListProductWidgetsComponent(driver).open_category("Desktops")
    list = ListProductWidgetsComponent(driver).get_list_product_widgets()

    CategoryProductWidgetComponent(driver, "iPhone").click_add_to_shopping_cart_button()
    SortByDropdownComponent(driver).click_option("Model (Z - A)")
    ShowNumberProductsDropdownComponent(driver).click_option("100")
