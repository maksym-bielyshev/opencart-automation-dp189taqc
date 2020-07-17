from selenium.webdriver import Remote
from selenium.webdriver import Chrome, ChromeOptions
from dp189.locators import LocatorsGiftCertificatePage
from dp189.pages.base_page import BasePage
from dp189.components import InputFieldComponent
import time


class GiftCertificatePage(BasePage):
    """Gift Certificate page class"""

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.recepient_name = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.RECEPIENT_NAME)
        self.recepient_email = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.RECEPIENT_EMAIL)
        self.your_name = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.YOUR_NAME)
        self.your_email = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.YOUR_EMAIL)
        self.message = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.MESSAGE)
        self.amount = InputFieldComponent(self._driver, LocatorsGiftCertificatePage.AMOUNT)

    def fill_recepient_name(self, recepient_name: str):
        """Method which fill field Recipient's Name on page"""
        self.recepient_name.clear_and_fill_input_field(recepient_name)

    def fill_recepient_email(self, recepient_email: str):
        """Method which fill field Recipient's Email on page"""
        self.recepient_email.clear_and_fill_input_field(recepient_email)

    def fill_your_name(self, your_name: str):
        """Method which fill field Name on page"""
        self.your_name.clear_and_fill_input_field(your_name)

    def fill_your_email(self, your_email: str):
        """Method which fill field Email on page"""
        self.your_email.clear_and_fill_input_field(your_email)

    def choose_gift_certificate_theme(self, choose_theme: str):
        """Method which fill click on theme on page"""
        for item in self._driver.find_elements(*LocatorsGiftCertificatePage.GIFT_CERTIFICATE_THEME):
            # print(item.text)
            if item.text == choose_theme: item.click()

    def fill_message(self, text_message: str):
        """Method which fill field Message on page"""
        self.message.clear_and_fill_input_field(text_message)

    def fill_amount(self, amount_items: str):
        """Method which fill field Amount on page"""
        self.amount.clear_and_fill_input_field(amount_items)

    def click_checkbox(self):
        """Method which click on Agree with agreement"""
        self._driver.find_element(*LocatorsGiftCertificatePage.AGREE).click()

    def click_button_continue(self):
        """Method which click on button Continue"""
        self._driver.find_element(*LocatorsGiftCertificatePage.CONTINUE_BUTTON).click()

    def fill_form_fields(self, recepient_name, recepient_email, your_name, your_email, choose_theme, text_message,
                         amount_items):
        self.fill_recepient_name(recepient_name)
        self.fill_recepient_email(recepient_email)
        self.fill_your_name(your_name)
        self.fill_your_email(your_email)
        self.choose_gift_certificate_theme(choose_theme)
        self.fill_message(text_message)
        self.fill_amount(amount_items)
        self.click_checkbox()
        self.click_button_continue()
