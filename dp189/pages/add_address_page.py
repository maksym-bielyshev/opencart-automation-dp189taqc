from dp189.components import RegisterPageRightMenuComponent, AddAddressComponent, RadioButtonComponent
from dp189.locators import LocatorsAddAddressPage
from dp189.pages.base_page import BasePage
from selenium.webdriver import Remote


class AddAddressPage(BasePage):
    """Description of the basic methods of working with 'Add Address' Page."""
    def __init__(self, driver: Remote) -> None:
        """Initialize objects to work with this page.

        :param driver: Remote
        :return: None
        """
        super().__init__(driver)
        self.right_menu = RegisterPageRightMenuComponent(driver)
        self.address_content = self._driver.find_element(*LocatorsAddAddressPage.ADDRESS_CONTENT)
        self.address_fields = AddAddressComponent(self._driver, self.address_content)
        self.default_address_radiobutton = RadioButtonComponent(self._driver,
                                                                LocatorsAddAddressPage.DEFAULT_ADDRESS_RADIO_CONTAINER)

    def click_back_button(self) -> None:
        """Click 'Back' button to return to 'Address Book' page.

        :return: None
        """
        self._driver.find_element(*LocatorsAddAddressPage.BACK_BUTTON).click()

    def click_continue_button(self) -> None:
        """Click 'Continue' button to return to 'Address Book' page if all filled data is valid or return to
        'Add Address Page' if some filled data is invalid.

        :return: None
        """
        self._driver.find_element(*LocatorsAddAddressPage.CONTINUE_BUTTON).click()