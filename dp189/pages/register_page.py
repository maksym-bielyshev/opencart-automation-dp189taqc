from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.components import YourPersonalDetailsComponent, YourPasswordComponent, NewsletterComponent
from dp189.locators import LocatorsRegisterPage


class RegisterPage(BasePage):
    """Register page class."""
    def __init__(self, driver:Remote) -> None:
        """Initialize objects to work with this page.

        :param driver: Remote
        :return: None
        """
        super().__init__(driver)
        self.your_personal_details_form = YourPersonalDetailsComponent(self._driver)
        self.your_password_form = YourPasswordComponent(self._driver)
        self.subscribe_radio_buttons = NewsletterComponent(self._driver)

    def click_continue_button(self):
        """Click continue button to submit all data to register a new user.

        :return: RegisterPage
        """
        self.continue_button = self._driver.find_element(*LocatorsRegisterPage.CONTINUE_BUTTON)
        self.continue_button.click()
        return RegisterPage(self._driver)

    def click_checkbox_privacy_policy(self) -> None:
        """Click checkbox Privacy Policy to agree with it.

        :return: None
        """
        self.checkbox_privacy_policy = self._driver.find_element(*LocatorsRegisterPage.CHECKBOX_PRIVACY_POLICY)
        self.checkbox_privacy_policy.click()

