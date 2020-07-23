from selenium.webdriver.common.by import By


class ComparePageConstants:
    BASE_URL = 'http://34.71.14.206/index.php?route=common/home'
    MACBOOK = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[3]')
    IPHONE = (By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[3]/button[3]')
    CINEMA = (By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[3]/button[3]')
    GO_TO_COMPARE_PAGE = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]/a[2]')
    TEST_ITEM1 = 'MacBook'
    TEST_ITEM2 = f'Apple Cinema 30"'
    MESSAGE = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')
    RESULT = f'Success: You have added iPhone to your shopping cart!\n×'
    RESULT2 = 'Apple Cinema 30'
    RESULT3 = f'Success: You have modified your product comparison!\n×'
