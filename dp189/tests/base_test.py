from selenium.webdriver.chrome.options import Options
import pytest
import csv

options = Options()
options.add_argument('--ignore-certificate-errors')


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def setup(self):
        pass

    def get_test_data(self, file_name) -> list:
        with open(f'../testsData/{file_name}', 'r') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True, delimiter='\t')
            test_data_list = []
            for row in reader:
                test_data_list.append(tuple(row[0].strip('][').split(';')))
            return test_data_list

    def teardown(self):
        self.driver.close()
