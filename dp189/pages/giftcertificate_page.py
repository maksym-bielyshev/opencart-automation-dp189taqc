from selenium.webdriver import Remote
from dp189.locators import LocatorsGiftCertificatePage
from dp189.pages.base_page import BasePage
from dp189.components import InputFieldComponent, RadioButtonComponent


class GiftCertificatePage(BasePage):
    """Gift Certificate page class"""

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.recepient_name = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.RECEPIENT_NAME)
        self.recepient_email = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.RECEPIENT_EMAIL)
        self.your_name = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.YOUR_NAME)
        self.your_email = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.YOUR_EMAIL)
        self.gift_certificate_theme = RadioButtonComponent(self._driver,
                                                           LocatorsGiftCertificatePage.GIFT_CERTIFICATE_THEME)
        self.message = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.MESSAGE)
        self.amount = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.AMOUNT)

    def click_checkbox(self):
        """Method which click on Agree with agreement.

        :return:None
        """
        self._driver.find_element(*LocatorsGiftCertificatePage.AGREE).click()

    def click_button_continue(self):
        """Method which click on button Continue.

        :return:None
        """
        self._driver.find_element(*LocatorsGiftCertificatePage.CONTINUE_BUTTON).click()
