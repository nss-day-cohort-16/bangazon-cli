import unittest
import sys
sys.path.append("../")
from Models.Product import Product
from DB.ProductData import ProductData



class TestProduct(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.shampoo  = Product("Coconut Oil Shampoo", "7.99", "silky smoothe hair treatment shampoo")

    def test_product_has_all_the_attributes(self):
        self.assertIsNotNone(self.shampoo.price)
        self.assertIsNotNone(self.shampoo.name)
        self.assertIsNotNone(self.shampoo.description)



    def test_product_can_be_saved(self):
        productData = ProductData() 
        productData.save_product(self.shampoo)
        data = productData.get_product(self.shampoo)

        self.assertIsInstance(data, tuple)




if __name__ =='__main__':
     unittest.main()