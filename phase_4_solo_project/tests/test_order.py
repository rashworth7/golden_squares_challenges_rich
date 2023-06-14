from unittest.mock import Mock
from order import *

# """
# Given Order
# empty menu given
# check that see menu returns a empty menu
# """
# order = Order() #Mock menu needed here
# order.see_menu # => ""

# """
# Given Order
# check that see menu returns a list of items and prices
# """
# order = Order() #Mock menu needed here
# order.see_menu # => "Menu!\n\nFish and chips: £15\nBurger: £13\nPasta: £10"

# """
# Given Order
# check that add_to_order() adds 2 different items to the order
# """
# order = Order() #Mock menu needed here
# order.add_to_order("Fish and chips", 1)
# order.add_to_order("Buger", 1)
# order.current_order# => {"Fish and Chips": 1, "Burger": 1}

# """
# Given Order
# check that add_to_order() adds 2 different items to the order over 1 of each
# """
# order = Order() #Mock menu needed here
# order.add_to_order("Fish and chips", 3)
# order.add_to_order("Buger", 2)
# order.current_order# => {"Fish and Chips": 3, "Burger": 2}

# """
# Given Order
# adds 2 different items to the order over 1 of each
# Check verify order formats the correct reciept
# """
# order = Order() #Mock menu needed here
# order.verify_order() # => "Nothing added to order"

# """
# Given Order
# adds 2 different items to the order over 1 of each
# Check verify order formats the correct reciept
# """
# order = Order() #Mock menu needed here
# order.add_to_order("Fish and chips", 3)
# order.add_to_order("Pasta", 2)
# order.verify_order() # => "Order Details!\n\n3 x Fish and Chips: £30\n2 x Pasta: £20\nTotal: £50"