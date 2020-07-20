from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dp189.pages.register_page import RegisterPage
options = Options()
options.add_argument('--ignore-certificate-errors')


class TestAddUser:

    def setup(self):
        self.my_driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe', options=options)
        self.my_driver.maximize_window()
        self.my_driver.get('https://34.71.14.206/index.php?route=account/register')
        self.page = RegisterPage(self.my_driver)

    def test_input_valid_data(self):
        self.page.your_personal_details_form.first_name_field.clear_and_fill_input_field('Maksym')
        self.page.your_personal_details_form.last_name_field.clear_and_fill_input_field('Statham')
        self.page.your_personal_details_form.email_field.clear_and_fill_input_field('test10@test.com.ua')
        self.page.your_personal_details_form.telephone_field.clear_and_fill_input_field('777')
        self.page.your_password_form.password_field.clear_and_fill_input_field('1111')
        self.page.your_password_form.password_confirm_field.clear_and_fill_input_field('1111')

        self.page.click_checkbox_privacy_policy()
        self.page.click_continue_button()

        assert self.my_driver.title == 'Your Account Has Been Created!'

    def teardown(self):
        self.my_driver.close()
