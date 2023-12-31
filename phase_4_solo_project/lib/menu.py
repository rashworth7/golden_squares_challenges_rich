

class Menu():
    #User facing properties
    #   dishes

    def __init__(self):
        # Parameters:
        #   dishes: dictionary of dishes and prices
        self.dishes = {}

    def add_dish(self, dish, price):
        self.dishes[dish] = price

# Code below is repeated in order class
"""
    def display_menu(self):
        if self.dishes == {}:
            return "Nothing on the menu"
        menu = f"Menu!\n\n"
        for item in self.dishes:
            menu += f"{item}: £{self.dishes[item]}\n"
        return menu[:-1]
"""