import os

import pytest
from base.BrowserLaunch import browser_launch
from base.util import read_json_file


@pytest.fixture
def set_up_for_test():
    browser_name = read_json_file(os.getcwd() + "/Data.json", "browserName")
    print(f'browser_name is {browser_name}')

    browser, page, playwright = browser_launch(browser_name)
    yield browser, page, playwright
    browser.close()
    playwright.stop()
