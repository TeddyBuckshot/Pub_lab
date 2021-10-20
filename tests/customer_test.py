import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer ("Sam",300.00,18,1)
        self.customer2 = Customer ("Alex",500.00,16,0)
        self.drink = Drink ("vodka",20.00,5)
        drinks = []
        drinks.append(self.drink)
        self.pub = Pub ("Black Bull",1000.00,drinks)
    
    def test_customer_has_name(self):
        self.assertEqual("Sam",self.customer.name)
    
    def test_customer_has_age(self):
        self.assertEqual(18,self.customer.age)
    
    def test_customer_has_drunkeness(self):
        self.assertEqual(1,self.customer.drunkeness)

    def test_customer_has_wallet(self):
        self.assertEqual(300.00,self.customer.wallet)

    def test_customer_wallet_reduce(self):
        self.customer.buy_drink(self.pub.drinks[0],self.pub)
        self.assertEqual(280.00, self.customer.wallet)

    def test_drunkeness_increases(self):
        self.customer.buy_drink(self.pub.drinks[0],self.pub)
        self.assertEqual(6, self.customer.drunkeness)

    