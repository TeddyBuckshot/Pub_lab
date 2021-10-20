from src.pub import Pub

class Customer:
    def __init__(self,name,wallet):
        self.name = name
        self.wallet = wallet


    def buy_drink(self,drink,pub):
        self.decrease_wallet(drink.price)
        pub.increase_money(drink.price)
    

    def decrease_wallet(self,amount):
        self.wallet -= amount 

    