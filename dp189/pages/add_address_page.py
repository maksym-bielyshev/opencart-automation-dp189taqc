from dp189.components import InputFieldComponent, BaseRightMenu, AddAddressComponent
from dp189.locators import LocatorsAddAddressPage
from dp189.pages.base_page import BasePage
from selenium.webdriver import Remote


class AddAddressPage(BasePage):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.right_menu = BaseRightMenu(driver)
        self.address_content = self._driver.find_element(*LocatorsAddAddressPage.ADDRESS_CONTENT)
        self.add_address = AddAddressComponent(self._driver, self.address_content)
        self.default_address = InputFieldComponent(self._driver,
                                                   LocatorsAddAddressPage.DEFAULT_ADDRESS_RADIO_CONTAINER)

    def click_back_button(self):
        '''

        :return: None
        '''
        self._driver.find_element(*LocatorsAddAddressPage.BACK_BUTTON).click()
        # return AddressBookPage(self._driver)

    def click_continue_button(self):
        self._driver.find_element(*LocatorsAddAddressPage.CONTINUE_BUTTON).click()