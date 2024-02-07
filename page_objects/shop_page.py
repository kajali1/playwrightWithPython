class ShopPage:

    def __init__(self, page):
        # self.checkoutBtn= page.locator("xpath=//a[@class='nav-link btn btn-primary']")
        self.searchText = page.locator("css=.search-keyword")
        self.searchBtn = page.locator("css=.search-button")
        self.searchedProduct = page.locator("css=.product-name:visible")
        self.addToCartBtn = page.locator("text='ADD TO CART'")
        self.cartIcon = page.locator(".cart-icon")
        self.proceedToCheckout = page.locator("text='PROCEED TO CHECKOUT'")
        self.NoOfItems = page.locator("text='No. of Items     : '")
        self.totalAmount = page.locator("css=.totAmt")
        # self.searchedProducts = page.locator("css=.product-name:visible")
        self.searchedProducts = page.get_by_role("heading")
