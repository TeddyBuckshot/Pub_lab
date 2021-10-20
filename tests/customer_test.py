import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer ("Sam",300)
        self.drink = Drink ("vodka",20)
        drinks = []
        drinks.append(self.drink)
        self.pub = Pub ("Black Bull",1000,drinks)
    
    def test_customer_has_name(self):
        self.assertEqual("Sam",self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(300,self.customer.wallet)

    def test_customer_wallet_reduce(self):
        self.customer.buy_drink(self.pub.drinks[0],self.pub)
        self.assertEqual(280, self.customer.wallet)