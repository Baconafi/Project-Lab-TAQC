import asyncio
from playwright.async_api import Page
from playwright.async_api import async_playwright

class AddToCart:
    def __init__(self, page: Page):
        self.page = page
        self.product = page.locator("#item_3_title_link")
        self.cart_button = page.locator("#add-to-cart")
        self.cart_page = page.locator(".shopping_cart_link")

    async def Cart(self):
        await self.product.click()
        await self.cart_button.click()
        await self.cart_page.click()
        await asyncio.sleep(1)