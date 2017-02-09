class ShoppingCart():

    def __init__(self, user):
        self.user = user
        self.products = "No products have been added yet"
        self.price_total = 0

    def add_to_cart(self, product):
        self.products = []
        self.products.append(product)

    def get_cart(self):
        return self.products

    def cart_total_price(self):
        for product in products:
          self.price_total + product.self

    def get_total_price(self):
        return self.price_total
