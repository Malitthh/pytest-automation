from playwright.sync_api import Page
import pytest

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page 
        yield
        page.context.clear_cookies()