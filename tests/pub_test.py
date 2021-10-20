import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer = Customer ("Sam",300.00,18,11)
        self.customer1 = Customer ("James",300.00,21,4)
        self.customer2 = Customer ("Alex",500.00,16,0)
        self.drink = Drink ("vodka",20.00,5)
        drinks = []
        drinks.append(self.drink)
        self.pub = Pub ("Black Bull",1000.00,drinks)

    def test_pub_has_name(self):
        self.assertEqual("Black Bull", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(1000.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual([self.drink],self.pub.drinks)

    def test_till_has_increased(self):
        self.customer1.buy_drink(self.pub.drinks[0],self.pub)
        self.assertEqual(1020.00, self.pub.till)

    def test_pub_check_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer))
    
    def test_pub_check_age2(self):
        self.assertEqual(False, self.pub.check_age(self.customer2))

    def test_pub_check_drunkeness(self):
        self.assertEqual(False, self.pub.check_drunk(self.customer))
    
    def test_pub_check_drunkeness2(self):
        self.assertEqual(True, self.pub.check_drunk(self.customer2))