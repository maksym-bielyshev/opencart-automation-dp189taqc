from selenium.webdriver.common.by import By


class ComparePageConstants:
    TEST_ITEM1 = 'iPhone'
    TEST_ITEM2 = f'Apple Cinema 30"'
    RESULT = f'Success: You have added iPhone to your shopping cart!\n×'
    RESULT2 = 'Apple Cinema 30'
    RESULT3 = f'Success: You have modified your product comparison!\n×'


class ShoppingCartPageConstants:
    TEST_ITEM1 = 'iPhone'
    RESULT = 'Success: You have modified your shopping cart!'
    RESULT2 = 202.0
    TITLE = 'Your Store'
