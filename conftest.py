import pytest
from CalculatorNet.config.config import get_config as get_calculatornet_config
from CalculatorNet.pages.financial.repayment_calculator_page import RepaymentCalculatorPage

# Browser configurationS
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "args": [
            "--start-maximized",
            "--window-size=1920,1080",
        ],
        "ignore_default_args": ["--enable-automation"],
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": None,
        "ignore_https_errors": True,
    }

@pytest.fixture(scope="session")
def calculatornet_config():
    return get_calculatornet_config()

@pytest.fixture
def repayment_page(page, calculatornet_config) -> RepaymentCalculatorPage:
    return RepaymentCalculatorPage(page, calculatornet_config.base_url)