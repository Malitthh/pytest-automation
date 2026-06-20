# Shared pytest configuration for the automation framework.

# This file contains:
# - Browser launch settings
# - Browser context settings
# - Shared fixtures used across projects

# Each project is responsible for loading its own settings (e.g. .env),
# while this file keeps the common Playwright configuration in one place.

import pytest

from CalculatorNet.config.settings import get_settings as get_calculatornet_settings
from CalculatorNet.pages.financial.repayment_calculator_page import RepaymentCalculatorPage

# Browser launch configuration
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": True,
        "args": [
            "--start-maximized",
            "--window-size=1920,1080",
        ],
        # Hide the "Chrome is being controlled by automated software" banner.
        "ignore_default_args": ["--enable-automation"],
    }

# Browser context shared by all tests
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        # Use the actual browser window size instead of a fixed viewport.
        "viewport": None,
        "ignore_https_errors": True,
    }

# CalculatorNet fixtures
@pytest.fixture(scope="session")
def calculatornet_settings():
    return get_calculatornet_settings()


@pytest.fixture
def repayment_page(page, calculatornet_settings) -> RepaymentCalculatorPage:
    """Returns a new repayment calculator page for each test."""
    return RepaymentCalculatorPage(page, calculatornet_settings.base_url)