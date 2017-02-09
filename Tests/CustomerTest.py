import unittest
import sys
sys.path.append("../")
from Models.Customers import Customer

class TestCustomer(unittest.TestCase):
	"""
	customer should have a:
	name
	street address, city, state, zipcode
	phone #
	"""
	@classmethod
	def setUpClass(self):
		self.me = Customer("Me", "500 interstate blvd", "TN", "11111", "666-6666")

	def test_customer_is_instance(self):
		self.assertIsInstance(self.me, Customer)

	def test_customer_has_attribute(self):
		self.assertEqual("Me", self.me.name)
		self.assertEqual("500 interstate blvd", self.me.address)
		self.assertEqual('TN', self.me.state)
		self.assertEqual("11111", self.me.postal)
		self.assertEqual("666-6666", self.me.phone)



if __name__ == "__main__":
	unittest.main()