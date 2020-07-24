from selenium.webdriver.chrome.options import Options
import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def setup(self):
        options = Options()
        options.add_argument('--ignore-certificate-errors')

    def teardown(self):
        self.driver.close()
