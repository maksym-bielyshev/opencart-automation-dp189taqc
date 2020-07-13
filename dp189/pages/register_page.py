from .base_page import BasePage
from ..components import YourPersonalDetailsComponent, YourPasswordComponent, NewsletterComponent
from ..locators import LocatorsRegisterPage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.your_personal_details_form = YourPersonalDetailsComponent(self._driver)
        self.your_password_form = YourPasswordComponent(self._driver)
        # self.subscribe_radio_buttons = driver.find_element(*LocatorsRegisterPage.SUBSCRIBE_RADIO_BUTTONS)
        self.subscribe_radio_buttons = NewsletterComponent(self._driver)

    def click_continue_button(self):
        self.continue_button = self._driver.find_element(*LocatorsRegisterPage.CONTINUE_BUTTON)
        self.continue_button.click()
        return RegisterPage(self._driver)

    def click_checkbox_privacy_policy(self):
        self.checkbox_privacy_policy = self._driver.find_element(*LocatorsRegisterPage.CHECKBOX_PRIVACY_POLICY)
        self.checkbox_privacy_policy.click()

