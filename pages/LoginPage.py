import asyncio
from playwright.async_api import Page
from playwright.async_api import async_playwright

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.LoginButton = page.locator("#login-button")

    async def Login(self):
        await self.username.fill("standard_user")
        await self.password.fill("secret_sauce")
        await self.LoginButton.click()
        await asyncio.sleep(1)