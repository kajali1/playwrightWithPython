
from playwright.sync_api import Playwright, sync_playwright


def browser_launch(browser_name):
    playwright = sync_playwright().start()
    if browser_name == 'chromium':
        chromium = playwright.chromium  # or "firefox" or "webkit".
        browser = chromium.launch(headless=False)

    else:
        firefox = playwright.firefox
        browser = firefox.launch(headless=False)

    page = browser.new_page()
    return browser, page, playwright


class BrowserLaunch:
    pass

# from page_objects.shop_page import shopPage
#
# with sync_playwright() as p:
#     browser= p.chromium.launch(headless=False)
#     page= browser.new_page()
#     page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
#     title = page.title()
#     print(title)
#     page.wait_for_timeout(3000)
#     shop_page = shopPage(page)
#     # page.wait_for_selector("xpath=//a[@class='nav-link btn btn-primary']")
#     # page.locator("xpath=//a[@class='nav-link btn btn-primary']").click()
#    # page.wait_for_selector(shop_page.checkoutBtn)
#     shop_page.checkoutBtn.click()
#     # browser.close()
