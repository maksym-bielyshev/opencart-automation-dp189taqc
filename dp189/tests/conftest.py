import csv
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

CHROME_DRIVER_WIN32 = '../driver/chromedriver.exe'
CHROME_DRIVER_LINUX64 = '../driver/chromedriver'


@pytest.fixture(scope="function")
def init_driver(request):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    # driver = webdriver.Chrome(CHROME_DRIVER_WIN32, options=options)
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome', 'version': '2', 'javascriptEnabled': True})
    request.cls.driver = driver
    driver.implicitly_wait(10)

    yield driver

    driver.close()


def get_test_data(file_name: str) -> list:
    """Converts file with test data to tuples list to use it in parameterized tests.
    :param file_name: string
    :return: test_data_list consists of tuples, where each tuple is one file row.
    """
    with open(f'../testsData/{file_name}', 'r') as file:
        reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True, delimiter='\t')
        test_data_list = []
        for row in reader:
            test_data_list.append(tuple(row[0].strip('][').split(';')))
        return test_data_list
