class ShoppingCart():

    def __init__(self, user):
        self.user = user
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)

    def get_cart(self):
        return self.products         
        

