class Pub:
    def __init__(self,name,till,drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_money(self,amount):
        self.till += amount

    def check_age(self,customer):
        if customer.age >= 18:
            return True
        else:
            return False

    def check_drunk(self,customer):
        if customer.drunkeness < 10:
            return True
        else:
            return False