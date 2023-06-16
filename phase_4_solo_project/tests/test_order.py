from unittest.mock import Mock
from lib.order import *

"""
Given Order
empty menu given
check that see menu returns a empty menu
"""
def test_empty_menu_returns_string_nothing_on_menu():

    mock_menu = Mock()
    mock_menu.dishes = {}
    
    order = Order(mock_menu) #Mock menu needed here
    assert order.see_menu() == "Nothing on the menu :("

"""
Given Order
check that see menu returns a list of items and prices
"""
def test_menu_returns_string_menu():

    mock_menu = Mock()
    mock_menu.dishes = {"Fish and chips": 15, "Burger": 13, "Pasta": 10}

    order = Order(mock_menu) #Mock menu needed here
    assert order.see_menu() == "Menu!\n\nFish and chips: £15\nBurger: £13\nPasta: £10"

"""
Given Order
check that add_to_order() adds 2 different items to the order
"""
def test_add_two_items_displays_current_order():

    mock_menu = Mock()
    mock_menu.dishes = {"Fish and chips": 15, "Burger": 13, "Pasta": 10}
    order = Order(mock_menu) #Mock menu needed here
    order.add_to_order("Fish and chips", 1)
    order.add_to_order("Burger", 1)
    assert order.current_order == {"Fish and chips": 1, "Burger": 1}

"""
Given Order
check that add_to_order() adds 2 different items to the order over 1 of each
"""
def test_add_two_items_each_with_over_1():

    mock_menu = Mock()
    mock_menu.dishes = {"Fish and chips": 15, "Burger": 13, "Pasta": 10}
    order = Order(mock_menu) #Mock menu needed here
    order.add_to_order("Fish and chips", 3)
    order.add_to_order("Burger", 2)
    assert order.current_order == {"Fish and chips": 3, "Burger": 2}


"""
Given Order
adds 2 different items to the order over 1 of each
Check verify order formats the correct reciept
"""
def test_verify_order_with_no_items():

    mock_menu = Mock()
    order = Order(mock_menu) #Mock menu needed here
    assert order.verify_order() == "Nothing added to order"

"""
Given Order
adds 2 different items to the order over 1 of each
Check verify order formats the correct reciept
"""
def test_verify_order_with_multiple_items():
    mock_menu = Mock()
    mock_menu.dishes = {"Fish and chips": 15, "Burger": 13, "Pasta": 10}
    order = Order(mock_menu) #Mock menu needed here
    order.add_to_order("Fish and chips", 3)
    order.add_to_order("Pasta", 2)
    assert order.verify_order() == "Order Details!\n\n3 x Fish and chips: £45\n2 x Pasta: £20\nTotal: £65"

