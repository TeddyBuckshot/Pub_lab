from src.drink import Drink

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

    def stock_decrease(self,drink,pub):
        pub.drinks[drink] -= 1
     
    def stock_value(self):
        total = 0 
        for key, value in self.drinks.items():
            total += (key.price * value)
        return total


    # experiment
    def return_drinks_dict(self):
        drink1 = Drink("vodka", 20.00, 5, 10)
        drink2 = Drink("tequila", 7.05, 8, 35)
        drink3 = Drink("wine", 25.50, 2, 15)
        list_of_drink_objects = []
        list_of_drink_objects.append(drink1)
        list_of_drink_objects.append(drink2)
        list_of_drink_objects.append(drink3)
        list_of_stock_values = [10, 35, 15]
        drinks = dict(zip(list_of_drink_objects, list_of_stock_values))
        print(drinks)
        return drinks
