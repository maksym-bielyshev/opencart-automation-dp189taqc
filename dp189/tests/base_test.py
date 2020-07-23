from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

options = Options()
options.add_argument('--ignore-certificate-errors')

CHROME_DRIVER = '../driver/chromedriver.exe'


@pytest.fixture(scope="function")
def init_driver(request):

    driver = webdriver.Chrome(CHROME_DRIVER)
    driver.get("http://34.71.14.206/index.php?route=product/product&path=20&product_id=62")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def setup(self):
        pass

    def teardown(self):
        self.driver.close()
