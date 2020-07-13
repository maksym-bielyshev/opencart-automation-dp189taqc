import sys
print(sys.path)
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
#MacOS import
from dp189.pages.home_page import HomePage

options = Options()
options.add_argument('--ignore-certificate-errors')
driver = Chrome('/Users/olexiyusov/PycharmProjects/selenium_project/drivers/chromedriver', options=options)
driver.maximize_window()


driver.get('http://34.71.14.206/index.php?route=common/home')

#driver.implicitly_wait(15)

page = HomePage(driver)
page.add_product_to_cart('iPhone')
#login_page = page.click_account_and_go_to_login()
#login_page.login('smith@mail.com','12345')
