from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def teardown(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        allure.attach(self.driver.get_screenshot_as_png(), f'screenshot-{now}.png', attachment_type=AttachmentType.PNG)
        self.driver.close()