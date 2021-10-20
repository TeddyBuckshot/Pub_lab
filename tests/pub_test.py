import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer = Customer ("Sam",300)
        self.drink = Drink ("vodka",20)
        drinks = []
        drinks.append(self.drink)
        self.pub = Pub ("Black Bull",1000,drinks)


    def test_pub_has_name(self):
        self.assertEqual("Black Bull", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(1000, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual([self.drink],self.pub.drinks)

    def test_till_has_increased(self):
        self.customer.buy_drink(self.pub.drinks[0],self.pub)
        self.assertEqual(1020, self.pub.till)

        

