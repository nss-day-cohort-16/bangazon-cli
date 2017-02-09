import unittest
import sys
sys.path.append("../")
from models import payment_options


#this is the class for creating all the tests under payment_options
class TestPaymentOptions(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.payment = payment_options.PaymentType("Trent", "Hand", "visa", "1234")

    def test_user_can_register_payment_option(self):
        self.assertIsInstance(self.payment, payment_options.PaymentType)

    def test_payment_option_has_correct_attributes(self):
        self.assertIsNotNone(self.payment.first_name)
        self.assertIsNotNone(self.payment.last_name)
        self.assertIsNotNone(self.payment.payment_type)
        self.assertIsNotNone(self.payment.account_number)

#run tests in the tests directory
#python -m unittest discover -s . -p "Test*.py" -v
