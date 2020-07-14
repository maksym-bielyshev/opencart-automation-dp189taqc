from .base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
BASEPAGE_URl = 'http://34.71.14.206/'
LOGIN_URl = 'index.php?route=account/login'

class LoginPage(BasePage):
    def __init__(self, driver: WebDriver) -> object:
        super().__init__(driver)
        self._name = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/div[1]/input')
        self._password = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/input')
        self._login_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/input')
        self._page_url = BASEPAGE_URl+ LOGIN_URl

    def go_to_page(self):
        return self._driver.get(self._page_url)

    def login(self, email: str, password: str):
        self._name.clear()
        self._password.clear()
        self._name.send_keys(email)
        self._password.send_keys(password)
        self._login_button.click()
        # if self._driver.current_url == 'https://34.71.14.206/index.php?route=account/account':
        #     BasePage._login_flag = True