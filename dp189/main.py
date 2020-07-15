from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from dp189.locators import LocatorsYourPersonalDetailsComponent
from dp189.pages.add_address_page import AddAddressPage
from dp189.pages.home_page import HomePage
from dp189.pages.register_page import RegisterPage

if __name__ == '__main__':
    options = Options()
    options.add_argument('--ignore-certificate-errors')

    driver = Chrome(options=options)
    driver.maximize_window()
    driver.get('https://34.71.14.206/index.php?route=account/login')
    driver.find_element(By.ID, 'input-email').send_keys("test@test.test")
    driver.find_element(By.ID, 'input-password').send_keys("12345678")
    driver.find_element(By.XPATH, '//input[@value="Login"]').click()

    driver.get('https://34.71.14.206/index.php?route=account/address/add')

    add_address = AddAddressPage(driver)
    add_address.add_address.first_name_field.clear_and_fill_input_field("2222")

