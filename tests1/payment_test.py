import unittest
import sys
sys.path.append("../")
from Models.payment import *

class TestPayment(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.juan_payment = Payment("Visa", "12345678", "Juan Gnecco")

    def test_user_payment_is_a_user_payment(self):
        self.assertIsInstance(self.juan_payment, Payment)

    def test_user_can_enter_payment_credentials(self):
        self.assertEqual(self.juan_payment.get_full_name(), "Juan Gnecco")
        self.assertEqual(self.juan_payment.get_payment_type(), "Visa")
        self.assertEqual(self.juan_payment.get_account_number(), "12345678")

if __name__ == "__main__":
    unittest.main()



