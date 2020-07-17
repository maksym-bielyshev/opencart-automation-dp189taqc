from dp189.components import BaseRightMenu, AddAddressComponent, RadioButtonComponent
from dp189.locators import LocatorsAddAddressPage
from dp189.pages.base_page import BasePage
from selenium.webdriver import Remote


class AddAddressPage(BasePage):
    """Description of the basic methods of working with 'Add Address' Page."""
    def __init__(self, driver: Remote):
        super().__init__(driver)
        """Initialize objects to work with this page.
        
        :param driver: Remote
        """
        self.right_menu = BaseRightMenu(driver)
        self.address_content = self._driver.find_element(*LocatorsAddAddressPage.ADDRESS_CONTENT)
        self.add_address = AddAddressComponent(self._driver, self.address_content)
        self.default_address_rediobutton = RadioButtonComponent(self._driver,
                                                                LocatorsAddAddressPage.DEFAULT_ADDRESS_RADIO_CONTAINER)

    def click_back_button(self) -> object:
        """Click 'Back' button to return to 'Address Book' page.

        :return: AddressBookPage
        """
        self._driver.find_element(*LocatorsAddAddressPage.BACK_BUTTON).click()
        # return AddressBookPage(self._driver)

    def click_continue_button(self) -> None:
        """Click 'Continue' button to return to 'Address Book' page if all filled data is valid or return to
        'Add Address Page' if some filled data is invalid.

        :return: None
        """
        self._driver.find_element(*LocatorsAddAddressPage.CONTINUE_BUTTON).click()