import pytest
from selenium import webdriver

CHROME_DRIVER = '../driver/chromedriver.exe'
CHROME_DRIVER_LINUX64 = '../driver/chromedriver'


@pytest.fixture(scope="function")
def init_driver(request):
    driver = webdriver.Chrome(CHROME_DRIVER_LINUX64)
    request.cls.driver = driver

    yield driver
