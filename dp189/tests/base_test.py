import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    """Prepare initial state before tests run and perform cleanup after tests complete."""

    def setup(self):
        pass

    def teardown(self):
        """Close driver after test completed."""
        self.driver.close()
