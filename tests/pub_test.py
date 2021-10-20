import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer = Customer ("Sam",300.00,18,11)
        self.customer1 = Customer ("James",300.00,21,4)
        self.customer2 = Customer ("Alex",500.00,16,0)
        # self.drink = Drink ("vodka",20.00,5, 10)
        # self.drink2 = Drink ("tequila",15.50,15, 30)
        # drinks = {}
        # drinks[self.drink] = 10
        self.pub = Pub ("Black Bull", 1000.00, self.return_drinks_dict())

    def test_pub_has_name(self):
        self.assertEqual("Black Bull", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(1000.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual({self.drink:10},self.pub.drinks)

    def test_till_has_increased(self):
        self.customer1.buy_drink(self.drink,self.pub)
        self.assertEqual(1020.00, self.pub.till)

    def test_pub_check_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer))
    
    def test_pub_check_age2(self):
        self.assertEqual(False, self.pub.check_age(self.customer2))

    def test_pub_check_drunkeness(self):
        self.assertEqual(False, self.pub.check_drunk(self.customer))
    
    def test_pub_check_drunkeness2(self):
        self.assertEqual(True, self.pub.check_drunk(self.customer2))

    def test_decrease_stock(self):
        self.customer1.buy_drink(self.drink,self.pub)
        self.assertEqual(9, self.pub.drinks[self.drink])

    def test_stock_value(self):
        self.assertEqual(200, self.pub.stock_value())