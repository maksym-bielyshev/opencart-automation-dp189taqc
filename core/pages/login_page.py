from core.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
        self._name = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/div[1]/input')
        self._password = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/input')
        self._login_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/input')
    
    def login(self, email: str, password: str):
        self._name.clear()
        self._password.clear()
        self._name.send_keys(email)
        self._password.send_keys(password)
        self._login_button.click()
        # if self._driver.current_url == 'https://34.71.14.206/index.php?route=account/account':
        #     BasePage._login_flag = True