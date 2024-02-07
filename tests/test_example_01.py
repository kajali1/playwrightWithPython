import os
import sys

import pytest
from playwright.sync_api import expect
from page_objects.shop_page import ShopPage
from base.util import read_json_file


@pytest.mark.sanity
def test_validate_title(set_up_for_test):
    browser, page, playwright = set_up_for_test
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    page.wait_for_load_state()
    expect(page).to_have_title("GreenKart - veg and fruits kart")


@pytest.mark.sanity1
def test_validate_search(set_up_for_test):
    print(sys.platform)
    browser, page, playwright = set_up_for_test
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    page.wait_for_load_state()
    shop_page = ShopPage(page)
    shop_page.searchText.fill(read_json_file(os.getcwd() + "/Data.json", "searchText2"))
    page.wait_for_selector("css=.search-button")
    shop_page.searchBtn.click()
    page.wait_for_selector("css=.product-name:visible")
    expect(shop_page.searchedProducts).to_have_count(4)
    expect(shop_page.searchedProducts).to_have_text(
        ['Cauliflower - 1 Kg', 'Carrot - 1 Kg', 'Capsicum', 'Cashews - 1 Kg'])


def test_add_to_cart(set_up_for_test):
    browser, page, playwright = set_up_for_test
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    page.wait_for_load_state()
    # other actions...
    shop_page = ShopPage(page)
    shop_page.searchText.fill(read_json_file(os.getcwd() + "/Data.json", "searchText1"))
    page.wait_for_selector("css=.search-button")
    shop_page.searchBtn.click()
    #    expect(shop_page.searchedProduct).to_have_text("Tomato - 1 Kg")
    page.wait_for_selector("text='ADD TO CART'")
    page.wait_for_timeout(3000)
    shop_page.addToCartBtn.click()
    shop_page.cartIcon.click()
    page.wait_for_selector("text='PROCEED TO CHECKOUT'")
    shop_page.proceedToCheckout.click()
    page.wait_for_selector("text='No. of Items     : '")
    expect(shop_page.NoOfItems).to_have_text('No. of Items     : ')
    expect(shop_page.totalAmount).to_have_text("16")
