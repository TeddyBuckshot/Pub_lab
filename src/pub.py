class Pub:
    def __init__(self,name,till,drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_money(self,amount):
        self.till += amount
