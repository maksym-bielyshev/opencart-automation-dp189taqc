from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.components import YourPersonalDetailsComponent, YourPasswordComponent, NewsletterComponent, \
    PrivacyPolicyComponent
from dp189.locators import LocatorsRegisterPage


class RegisterPage(BasePage):
    """Register page class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize objects to work with this page.

        :param driver: Remote
        :return: None
        """
        super().__init__(driver)
        self.register_account_container = self._driver.find_element(*LocatorsRegisterPage.YOUR_PERSONAL_DETAILS_PARENT)
        self.your_personal_details_form = YourPersonalDetailsComponent(self._driver, self.register_account_container)
        self.your_password_form = YourPasswordComponent(self._driver, self.register_account_container)
        self.subscribe_radio_buttons = NewsletterComponent(self._driver)
        self.privacy_policy_checkbox = PrivacyPolicyComponent(self._driver)

    def click_continue_button(self) -> None:
        """Click continue button to submit all data to register a new user.

        :return: None
        """
        self.continue_button = self._driver.find_element(*LocatorsRegisterPage.CONTINUE_BUTTON)
        self.continue_button.click()
