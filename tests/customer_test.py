import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer ("Sam",300)
    
    def test_customer_has_name(self):
        self.assertEqual("Sam",self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(300,self.customer.wallet)