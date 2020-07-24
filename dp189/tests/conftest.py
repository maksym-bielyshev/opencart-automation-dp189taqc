import pytest
from selenium import webdriver

CHROME_DRIVER = 'dp189/driver/chromedriver.exe'


@pytest.fixture(scope="function")
def init_driver(request):
    driver = webdriver.Chrome(CHROME_DRIVER)
    request.cls.driver = driver

    yield driver
