

class Order():
    #User facing properties
    #   Menu: menu (dictionary)
    

    def __init__(self, menu):
        # Parameters:
        #   menu: instance of a menu
        #   current_order: dictionary of dishes and number of items
        #   order_place: bool
        # Returns nothing
        # Side effects:
        #   Adds the diary entry to the list of dairy entries
        self.menu = menu
        self.current_order = {}
        self.order_price = 0

    def see_menu(self):
        # Returns:
        #   List of items and prices
        if self.menu.dishes == {}:
            return "Nothing on the menu :("
        current_menu = "Menu!\n\n"
        for item in self.menu.dishes:
            current_menu += f"{item}: £{self.menu.dishes[item]}\n"
        return current_menu[:-1]
    
    def add_to_order(self, item, quantity):
        # Parameters:
        #   item: string
        # Returns: nothing
        # Side effects:
        #   adds items to order 
        self.current_order[item] = self.current_order.get(item, 0) + quantity
        self.order_price += quantity * self.menu.dishes[item]

    def remove_from_order(self, item, quantity):
        if item not in self.current_order:
            raise Exception("item not on the order")
        elif self.current_order[item] == 1:
            del self.current_order[item]
        else:
            self.current_order[item] -= 1

    def verify_order(self):
        # Returns:
        #   formatted string showing number of items, cost and total cost
        if self.current_order == {}: 
            return "Nothing added to order"
        
        order_details = "Order Details!\n\n"
        for item, quantity in self.current_order.items():
            order_details += f"{quantity} x {item}: £{quantity * self.menu.dishes[item]}\n"

        order_details += f"Total: £{self.order_price}"
        return order_details