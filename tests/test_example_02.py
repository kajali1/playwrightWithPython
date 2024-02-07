import pytest
from playwright.sync_api import expect


@pytest.mark.sanity
def test_handling_windows(set_up_for_test):
    browser, page, playwright = set_up_for_test
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    with page.expect_popup() as new_page_info:
        page.locator("css=#opentab").click()  # Opens a new tab
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    print(new_page.title())
    expect(new_page).to_have_title("QAClick Academy - A Testing Academy to Learn, Earn and Shine")
