import pytest

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, page: "Page"):
        self.page = page