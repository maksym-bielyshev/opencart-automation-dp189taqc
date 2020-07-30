from dp189.components import RegisterPageRightMenuComponent, InputFieldComponent, LoginComponent
from dp189.locators import LocatorsLoginPage
from dp189.pages.base_page import BasePage
from dp189.pages.forgot_password_page import ForgotPasswordPage
from selenium.webdriver import Remote
from dp189.pages.register_page import RegisterPage


class LoginPage(BasePage):
    """This class describes methods that we need to work with 'Login' page."""
    def __init__(self, driver: Remote):
        """Initialize driver and objects to works with 'Login' page.

        :param driver: Remote
        """
        super().__init__(driver)
        self.right_menu = RegisterPageRightMenuComponent(self._driver)
        self.login_form = LoginComponent(self._driver)

    def click_forgotten_password_button(self) -> object:
        """Click 'Forgotten password' button

        :return: ForgotPasswordPage object
        """
        self._driver.find_element(*LocatorsLoginPage.FORGOTTEN_PASSWORD_BUTTON).click()
        return ForgotPasswordPage(self._driver)

    def click_login_button(self) -> None:
        """Click 'Login' button

        :return: None
        """
        self._driver.find_element(*LocatorsLoginPage.LOGIN_BUTTON).click()

    def click_register_button(self) -> object:
        """Click 'Register' button

        :return: RegisterPage object
        """
        self._driver.find_element(*LocatorsLoginPage.REGISTER_PAGE_BUTTON).click()
        return RegisterPage(self._driver)
