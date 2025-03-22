import asyncio
from playwright.async_api import async_playwright
from pages.LoginPage import LoginPage
from pages.AddToCart import AddToCart
from pages.LogoutPage import LogoutPage

URL = "https://www.saucedemo.com/"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL, wait_until='domcontentloaded')

        login = LoginPage(page)
        await login.Login()

        add_cart = AddToCart(page)
        await add_cart.Cart()

        logout = LogoutPage(page)
        await logout.Logout()

        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())





