import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from dp189.pages.register_page import RegisterPage
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('headless')


class TestYourPersonalDetails:
    """Tests for YourPersonalDetails component which consists four input field: First Name, Last Name, E-Mail, Telephone."""

    def setup(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get('http://34.71.14.206/index.php?route=account/register')
        self.register_page = RegisterPage(self.driver)

    @pytest.mark.parametrize('first_name, expected_result',
                             [
                                 ('W', 'selenium.common.exceptions.TimeoutException: Message:'),
                                 ('Wolfeschlegelste', 'selenium.common.exceptions.TimeoutException: Message:'),
                                 ('Wolfeschlegelsteinhausenbergerdo',
                                  'selenium.common.exceptions.TimeoutException: Message:')
                             ]
                             )
    def test_first_name_field_valid_number_characters(self, first_name, expected_result):
        with pytest.raises(TimeoutException) as error:
            self.register_page.your_personal_details_form.first_name_field.clear_and_fill_input_field(first_name)
            self.register_page.click_continue_button()
            self.register_page.your_personal_details_form.first_name_field.error_message.get_error_message()
        assert str(TimeoutException) in str(error.type)

    @pytest.mark.parametrize('last_name, expected_result',
                             [
                                 ('E', 'selenium.common.exceptions.TimeoutException: Message:'),
                                 ('Enraejakavarapa', 'selenium.common.exceptions.TimeoutException: Message:'),
                                 ('Enraejakavarapantiyacuppiramaniy',
                                  'selenium.common.exceptions.TimeoutException: Message:')
                             ]
                             )
    def test_last_name_field_valid_number_characters(self, last_name, expected_result):
        with pytest.raises(TimeoutException) as error:
            self.register_page.your_personal_details_form.last_name_field.clear_and_fill_input_field(last_name)
            self.register_page.click_continue_button()
            self.register_page.your_personal_details_form.last_name_field.error_message.get_error_message()
        assert str(TimeoutException) in str(error.type)

    @pytest.mark.parametrize('email, expected_result',
                             [
                                 ('y@i.ua', 'selenium.common.exceptions.TimeoutException: Message:'),
                                 ('test@email.ua', 'selenium.common.exceptions.TimeoutException: Message:'),
                                 ('testtesttesttesttesttesttesttes@email.ua',
                                  'selenium.common.exceptions.TimeoutException: Message:')
                             ]
                             )
    def test_email_field_valid_number_characters(self, email, expected_result):
        with pytest.raises(TimeoutException) as error:
            self.register_page.your_personal_details_form.email_field.clear_and_fill_input_field(email)
            self.register_page.click_continue_button()
            self.register_page.your_personal_details_form.email_field.error_message.get_error_message()
        assert str(TimeoutException) in str(error.type)

    @pytest.mark.parametrize('telephone, expected_result',
                             [
                                 ('123', 'selenium.common.exceptions.TimeoutException: Message:'),
                                 ('1234567890987654', 'selenium.common.exceptions.TimeoutException: Message:'),
                                 ('12345678909876543212345678909876',
                                  'selenium.common.exceptions.TimeoutException: Message:')
                             ]
                             )
    def test_telephone_field_valid_number_characters(self, telephone, expected_result):
        with pytest.raises(TimeoutException) as error:
            self.register_page.your_personal_details_form.telephone_field.clear_and_fill_input_field(telephone)
            self.register_page.click_continue_button()
            self.register_page.your_personal_details_form.telephone_field.error_message.get_error_message()
        assert str(TimeoutException) in str(error.type)

    @pytest.mark.parametrize('first_name, expected_result',
                             [
                                 ('', 'First Name must be between 1 and 32 characters!'),
                                 (
                                 'Wolfeschlegelsteinhausenbergerdoq', 'First Name must be between 1 and 32 characters!')
                             ]
                             )
    def test_first_name_field_invalid_number_characters(self, first_name, expected_result):
        self.register_page.your_personal_details_form.first_name_field.clear_and_fill_input_field(first_name)
        self.register_page.click_continue_button()
        assert self.register_page.your_personal_details_form.first_name_field.error_message.get_error_message() == \
               expected_result

    @pytest.mark.parametrize('last_name, expected_result',
                             [
                                 ('', 'Last Name must be between 1 and 32 characters!'),
                                 ('Enraejakavarapantiyacuppiramaniyw', 'Last Name must be between 1 and 32 characters!')
                             ]
                             )
    def test_last_name_field_invalid_number_characters(self, last_name, expected_result):
        self.register_page.your_personal_details_form.last_name_field.clear_and_fill_input_field(last_name)
        self.register_page.click_continue_button()
        assert self.register_page.your_personal_details_form.last_name_field.error_message.get_error_message() == \
               expected_result

    @pytest.mark.parametrize('email, expected_result',
                             [
                                 ('', 'E-Mail Address does not appear to be valid!')
                             ]
                             )
    def test_email_field_invalid_number_characters(self, email, expected_result):
        pass

    @pytest.mark.parametrize('telephone, expected_result',
                             [
                                 ('12', 'Telephone must be between 3 and 32 characters!'),
                                 ('123456789098765432123456789098765', 'Telephone must be between 3 and 32 characters!')
                             ]
                             )
    def test_telephone_field_invalid_number_characters(self, telephone, expected_result):
        self.register_page.your_personal_details_form.telephone_field.clear_and_fill_input_field(telephone)
        self.register_page.click_continue_button()
        assert self.register_page.your_personal_details_form.telephone_field.error_message.get_error_message() == \
               expected_result

    def teardown(self):
        self.driver.close()