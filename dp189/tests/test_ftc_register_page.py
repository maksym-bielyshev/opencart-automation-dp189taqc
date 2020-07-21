import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dp189.pages.register_page import RegisterPage
options = Options()
options.add_argument('--ignore-certificate-errors')


class TestAddUser:

    def setup(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get('https://34.71.14.206/index.php?route=account/register')
        self.register_page = RegisterPage(self.driver)

    @pytest.mark.parametrize('first_name, expected_result',
                             [
                                 ('', 'First Name must be between 1 and 32 characters!'),
                                 ('111111111111111111111111111111111', 'First Name must be between 1 and 32 characters!')
                             ]
                             )
    def test_first_name_field_wrong_number_characters(self, first_name, expected_result):
        self.register_page.your_personal_details_form.first_name_field.clear_and_fill_input_field(first_name)
        self.register_page.click_continue_button()
        assert self.register_page.your_personal_details_form.first_name_field.error_message.get_error_message() == \
               expected_result

    @pytest.mark.parametrize('last_name, expected_result',
                             [
                                 ('', 'Last Name must be between 1 and 32 characters!'),
                                 ('111111111111111111111111111111111', 'Last Name must be between 1 and 32 characters!')
                             ]
                             )
    def test_last_name_field_wrong_number_characters(self, last_name, expected_result):
        self.register_page.your_personal_details_form.last_name_field.clear_and_fill_input_field(last_name)
        self.register_page.click_continue_button()
        assert self.register_page.your_personal_details_form.last_name_field.error_message.get_error_message() == \
               expected_result

    @pytest.mark.parametrize('email, expected_result',
                             [
                                 ('', 'E-Mail Address does not appear to be valid!')
                             ]
                             )
    def test_email_field_wrong_number_characters(self, email, expected_result):
        self.register_page.your_personal_details_form.email_field.clear_and_fill_input_field(email)
        self.register_page.click_continue_button()
        assert self.register_page.your_personal_details_form.email_field.error_message.get_error_message() == \
               expected_result

    @pytest.mark.parametrize('telephone, expected_result',
                             [
                                 ('12', 'Telephone must be between 3 and 32 characters!'),
                                 ('111111111111111111111111111111111', 'Telephone must be between 3 and 32 characters!')
                             ]
                             )
    def test_telephone_field_wrong_number_characters(self, telephone, expected_result):
        self.register_page.your_personal_details_form.telephone_field.clear_and_fill_input_field(telephone)
        self.register_page.click_continue_button()
        assert self.register_page.your_personal_details_form.telephone_field.error_message.get_error_message() == \
               expected_result

    # def test_input_valid_data(self):
    #     self.register_page.your_personal_details_form.first_name_field.clear_and_fill_input_field('Maksym')
    #     self.register_page.your_personal_details_form.last_name_field.clear_and_fill_input_field('Statham')
    #     self.register_page.your_personal_details_form.email_field.clear_and_fill_input_field('test10@test.com.ua')
    #     self.register_page.your_personal_details_form.telephone_field.clear_and_fill_input_field('777')
    #
    #     self.register_page.your_password_form.password_field.clear_and_fill_input_field('1111')
    #     self.register_page.your_password_form.password_confirm_field.clear_and_fill_input_field('1111')
    #
    #     self.register_page.subscribe_radio_buttons.subscribe_to_newsletter()
    #     self.register_page.privacy_policy_checkbox.agree_with_privacy_policy()
    #
    #     self.register_page.click_continue_button()
    #
    #     assert self.driver.title == 'Register Account'

    def teardown(self):
        self.driver.close()