from dp189.components import InputFieldComponent, BaseRightMenu, AddAddressComponent
from dp189.locators import LocatorsAddAddressPage
from dp189.pages.base_page import BasePage
from selenium.webdriver import Remote


class AddAddressPage(BasePage):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.right_menu = BaseRightMenu(driver)
        self.add_address = AddAddressComponent(driver)

    def click_back_button(self):
        '''

        :return: None
        '''
        self._driver.find_element(*LocatorsAddAddressPage.BACK_BUTTON).click()
        # return AddressBookPage()

    def click_continue_button(self):
        self._driver.find_element(*LocatorsAddAddressPage.CONTINUE_BUTTON).click()