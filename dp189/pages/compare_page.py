from dp189.pages.base_page import BasePage
from selenium.webdriver import Remote
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.remote.webelement import WebElement
from dp189.locators import LocatorsComparePage
import time

CHROME_DRIVER = '../driver/chromedriver'


class ComparePage(BasePage):
    """Compare page class."""

    def __init__(self, driver: Remote) -> None:
        super().__init__(driver)
        self.table_rows = []

    def get_rows_in_table(self) -> list:
        """Method which returns list of WebElements(table_row) on Compare Page.

        :return: list
        """
        rows = self._driver.find_elements(*LocatorsComparePage.TABLE_ROW)
        for row in rows:
            self.table_rows.append(PropertyOfProduct(row))
        return self.table_rows

    def get_products(self) -> dict:
        """Method which returns dictionary with name of product.

        :return: dict
        """
        dict_names = {}
        names = PropertyOfProduct.get_name(self.table_rows[0])
        print(names)
        dict_names[names[0].text] = list()
        for i in range(1, len(names)):
            dict_names[names[0].text].append(names[i].text)
        return dict_names

    def get_prices(self) -> dict:
        """Method which returns dictionary with price of product.

        :return: dict
        """
        dict_prices = {}
        prices = PropertyOfProduct.get_price(self.table_rows[2])
        dict_prices[prices[0].text] = list()
        for i in range(1, len(prices)):
            dict_prices[prices[0].text].append(prices[i].text)
        return dict_prices

    def get_list_add_buttons(self) -> list:
        """Method which returns list with WebElements(add to cart button) on Compare Page.

        :return: dict
        """
        list_add_buttons = []
        add_buttons = PropertyOfProduct.get_add_button(self.table_rows[12])
        for button in add_buttons:
            list_add_buttons.append(button)
        return list_add_buttons

    def get_list_remove_buttons(self) -> list:
        """Method which returns list with WebElements(remove button) on Compare Page.

        :return: dict
        """
        list_remove_buttons = []
        remove_buttons = PropertyOfProduct.get_remove_button(self.table_rows[12])
        for button in remove_buttons:
            list_remove_buttons.append(button)
        return list_remove_buttons

    def click_add_to_cart_button(self, item) -> None:
        """Method which add appointed item to the cart.

        :return: None
        """
        button = self.get_list_add_buttons()
        product = self.get_products()
        for element in product['Product']:
            if element == item:
                index = product['Product'].index(item)
                button[index].click()

    def click_remove_button(self, item: str) -> object:
        """Method which remove appointed item on compare page.

        :return: object
        """
        button = self.get_list_remove_buttons()
        product = self.get_products()
        print(product['Product'])
        for element in product['Product']:
            if element == item:
                index = product['Product'].index(item)
                button[index].click()
        return ComparePage(self._driver)


class PropertyOfProduct:
    def __init__(self, property: WebElement) -> None:
        self._property = property

    def get_name(self) -> list:
        """Method which returns list of WebElements in table.

        :return: list
        """
        return self._property.find_elements(*LocatorsComparePage.TABLE_COLUMN)

    def get_price(self):
        """Method which returns list of WebElements in table.

        :return: list
        """
        return self._property.find_elements(*LocatorsComparePage.TABLE_COLUMN)

    def get_brand(self):
        """Method which returns list of WebElements in table.

        :return: list
        """
        return self._property.find_elements(*LocatorsComparePage.TABLE_COLUMN)

    def get_add_button(self):
        """Method which returns list of WebElements in table.

        :return: list
        """
        return self._property.find_elements(*LocatorsComparePage.ADD_BUTTONS)

    def get_remove_button(self):
        """Method which returns list of WebElements in table.

        :return: list
        """
        return self._property.find_elements(*LocatorsComparePage.REMOVE_BUTTONS)


if __name__ == '__main__':
    options = ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = Chrome(CHROME_DRIVER, options=options)
    driver.maximize_window()
    driver.get("http://34.71.14.206/index.php?route=common/home")
    driver.find_element_by_xpath(f'//*[@id="content"]/div[2]/div[1]/div/div[3]/button[3]').click()
    time.sleep(3)
    driver.find_element_by_xpath(f'//*[@id="content"]/div[2]/div[2]/div/div[3]/button[3]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="common-home"]/div[1]/a[2]').click()
    time.sleep(3)
    comparepage = ComparePage(driver)
    print(comparepage.get_rows_in_table())
    print(comparepage.get_products())
    print(comparepage.get_prices())
    comparepage.click_add_to_cart_button("ds")
