from selenium.webdriver.chrome.options import Options
import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def setup(self):
        pass

    def teardown(self):
        self.driver.close()
