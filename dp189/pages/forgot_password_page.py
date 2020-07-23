"""Forgot password page."""

from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.components import InputFieldComponent, BaseRightMenu
from dp189.locators import LocatorsForgotPasswordPage


class ForgotPasswordPage(BasePage):
    """Page to recover password."""

    def __init__(self, driver: Remote) -> None:
        """Initialise input fields, buttons and account menu.

        :param driver: Remote driver.
        """
        super().__init__(driver)
        self.email_address_field = InputFieldComponent(driver, LocatorsForgotPasswordPage.EMAIL_FIELD)
        self.back_button = driver.find_element(*LocatorsForgotPasswordPage.BACK_BUTTON)
        self.continue_button = driver.find_element(*LocatorsForgotPasswordPage.CONTINUE_BUTTON)
        self.right_navigation_menu = BaseRightMenu(driver)

    def click_back_button(self) -> None:
        """Click on the 'Back' button.

        :return: None.
        """
        self.back_button.click()

    def click_continue_button(self) -> None:
        """Click on the 'Continue' button.

        :return: None.
        """
        self.continue_button.click()
