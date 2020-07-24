# Import 'logging' lib.
import logging

# Declare logger with name of module (name of current log is 'dp189.tests.logging_sample')
__log = logging.getLogger(__name__)


def debug_function_example():
    # Create log points with message level and string info.
    __log.debug("Start function.")
    print("Function flow.")
    __log.debug("End function.")

# Run this function in main.py module and go to the 'dp189/tests/logs/logging_sample.log' for information.
