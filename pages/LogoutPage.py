import asyncio
from playwright.async_api import Page
from playwright.async_api import async_playwright

class LogoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu = page.locator("#react-burger-menu-btn")
        self.logoutbutton = page.locator("#logout_sidebar_link")

    async def Logout(self):
        await self.menu.click()
        await self.logoutbutton.click()
        await asyncio.sleep(1)