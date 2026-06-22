import re
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")

    def navigate(self, path: str = "") -> None:
        url = f"{self.base_url}/{path.lstrip('/')}" if path else self.base_url
        self.page.goto(url, wait_until="domcontentloaded")

    @staticmethod
    def parse_currency(text: str) -> float:
        cleaned = re.sub(r"[^0-9.]", "", text)
        return float(cleaned)