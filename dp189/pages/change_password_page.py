from selenium.webdriver import Remote
from dp189.components import YourPasswordComponent
from dp189.locators import LocatorsChangePasswordPage
from dp189.pages.base_page import BasePage


class ChangePasswordPage(BasePage):
    """Change password page class."""

    def __init__(self, driver: Remote) -> None:
        """Initialize object to work with this page.

        :param driver: Remote
        :return: None
        """
        super().__init__(driver)
        self.your_password_container = self._driver.find_element(*LocatorsChangePasswordPage.YOUR_PASSWORD_PARENT)
        self.your_password_form = YourPasswordComponent(self._driver, self.your_password_container)

    def click_continue_button(self) -> None:
        """Click continue button to change password for user.

        :return: None
        """
        continue_button = self._driver.find_element(*LocatorsChangePasswordPage.CONTINUE_BUTTON)
        continue_button.click()

    def click_back_button(self) -> None:
        """Click back button to return user to the previous page.

        :return: None
        """
        back_button = self._driver.find_element(*LocatorsChangePasswordPage.BACK_BUTTON)
        back_button.click()
