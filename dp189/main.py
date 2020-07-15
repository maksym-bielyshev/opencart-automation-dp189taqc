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
        register_page.your_personal_details_form.first_name_field.clear_and_fill_input_field(
            '111111111111111111111111111111111111111111111')
        register_page = register_page.click_continue_button()
        print(register_page.your_personal_details_form.first_name_field.get_error_message_for_input_field())

        print(register_page.subscribe_radio_buttons.is_subscribed())
        register_page.subscribe_radio_buttons.subscribe_to_newsletter()
        print(register_page.subscribe_radio_buttons.is_subscribed())