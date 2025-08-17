from playwright.sync_api import Page, expect
from typing import Pattern

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url, wait_until='networkidle')

    def reload(self):
        self.page.reload(wait_until='domcontentloaded')

    def pause(self):
        self.page.pause()

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)