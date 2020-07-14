from selenium.webdriver import Chrome, ChromeOptions, Remote
import time
from selenium.webdriver.chrome.options import Options
from dp189.pages.wishlist_page import WishListPage

CHROME_DRIVER = 'driver/chromedriver'
LOGIN_URl = 'http://34.71.14.206/index.php?route=account/login'
email = 'test@gmail.com'
password = 'test'


if __name__ == '__main__':
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = Chrome(CHROME_DRIVER, options=options)
    driver.maximize_window()
    driver.get(LOGIN_URl)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/div[1]/input').send_keys(email)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/input').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/input').click()
    driver.find_element_by_xpath("//a[@id='wishlist-total']").click()
    wishlist = WishListPage(driver)
    wishlist.get_list_items()
    wishlist.add_to_cart_button('MacBook')
    time.sleep(8)