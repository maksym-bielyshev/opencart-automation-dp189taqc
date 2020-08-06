#!/bin/bash

# Run Selenium Standalone-Chrome.
bash /opt/bin/entry_point.sh &

# Run tests.
cd /var/opencart-automation/dp189/tests \
    && sudo pytest -v --alluredir=/var/opencart-automation/dp189/reports
