#!/bin/bash

# Run Selenium Standalone-Chrome.
bash /opt/bin/entry_point.sh &

# Run tests.
cd /var/opencart-automation/dp189/tests \
    && sudo pytest -v test_ftc_checkout_page.py, test_ftc_product_page.py --alluredir=/var/opencart-automation/dp189/reports
