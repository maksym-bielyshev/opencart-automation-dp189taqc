import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from dp189.locators import LocatorsYourPersonalDetailsComponent
from dp189.pages.home_page import HomePage
from dp189.pages.register_page import RegisterPage

if __name__ == '__main__':
    options = Options()
    options.add_argument('--ignore-certificate-errors')

    with Chrome(options=options) as driver:
        driver.maximize_window()
        driver.get('http://34.71.14.206/index.php?route=account/register')

        register_page = RegisterPage(driver)
        register_page.your_personal_details_form.first_name_field.fill_field(
            '111111111111111111111111111111111111111111111')
        register_page = register_page.click_continue_button()
        print(register_page.your_personal_details_form.first_name_field.get_error_message_for_input_field())
        register_page.your_personal_details_form.first_name_field.clear_field()

        register_page.your_personal_details_form.last_name_field.fill_field(
            '1111111111111111111111111111111111111111111111')
        register_page = register_page.click_continue_button()
        print(register_page.your_personal_details_form.last_name_field.get_error_message_for_input_field())
        register_page.your_personal_details_form.last_name_field.clear_field()

        register_page.your_personal_details_form.email_field.fill_field('')
        register_page = register_page.click_continue_button()
        print(register_page.your_personal_details_form.email_field.get_error_message_for_input_field())
        register_page.your_personal_details_form.email_field.clear_field()

        register_page.your_personal_details_form.telephone_field.fill_field('11')
        register_page = register_page.click_continue_button()
        print(register_page.your_personal_details_form.telephone_field.get_error_message_for_input_field())
        register_page.your_personal_details_form.telephone_field.clear_field()

        register_page.your_password_form.password_field.fill_field('123')
        register_page = register_page.click_continue_button()
        print(register_page.your_password_form.password_field.get_error_message_for_input_field())
        register_page.your_password_form.password_field.clear_field()

        register_page.your_password_form.password_confirm_field.fill_field('321')
        register_page = register_page.click_continue_button()
        print(register_page.your_password_form.password_confirm_field.get_error_message_for_input_field())
        register_page.your_password_form.password_confirm_field.clear_field()

        register_page.subscribe_radio_buttons.get_status_for_radio_buttons()
        register_page.subscribe_radio_buttons.subscribe_to_newsletter()
        time.sleep(5)