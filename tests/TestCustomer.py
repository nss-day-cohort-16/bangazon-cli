import unittest 
import sys
sys.path.append("../")
from models import customer

class TestCustomer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.joey = customer.Customer('Joey', '461 East Silver St', 'Lebanon', 'Ohio', '45036', '5137033755')
        
    def test_customer_acct_can_be_created(self):
        self.assertIsInstance(self.joey, customer.Customer)

    def test_customer_has_correct_attributes(self):
        self.assertIsNotNone(self.joey.customer_name)
        self.assertIsNotNone(self.joey.street_address)
        self.assertIsNotNone(self.joey.city)
        self.assertIsNotNone(self.joey.state)
        self.assertIsNotNone(self.joey.postal_code)
        self.assertIsNotNone(self.joey.phone_number)

#run in test dir
#python -m unittest discover -s . -p "Test*.py" -v