from src.pub import Pub
from src.drink import Drink

class Customer:
    def __init__(self,name,wallet,age,drunkeness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness

    def buy_drink(self,drink,pub):
        if pub.check_age(self) == True:
            if pub.check_drunk(self) == True:
                self.decrease_wallet(drink.price)
                pub.increase_money(drink.price)
                self.drunkeness += drink.alcohol_level
    

    def decrease_wallet(self,amount):
        self.wallet -= amount 

