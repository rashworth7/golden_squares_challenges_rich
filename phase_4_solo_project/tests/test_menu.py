from unittest.mock import Mock
from lib.menu import *


"""
Given Menu
Check empty dishes
"""
def test_no_dishes_returns_empty_dict():
    menu = Menu()
    assert menu.dishes == {}

"""
Given Menu
Check add adds multiple dishes to the menu
"""
def test_add_dishes_to_menu():
    menu = Menu()
    menu.add_dish("Fish and Chips", 15)
    menu.add_dish("Burger", 13)
    menu.add_dish("Pasta", 10)
    assert menu.dishes == {"Fish and Chips": 15, "Burger": 13, "Pasta": 10}

"""
Given Menu
Check display menu display nothing if nothing added to menu
"""
def test_dsiplay_menu_with_nothing_on_menu():
    menu = Menu()
    assert menu.display_menu() == "Nothing on the menu"

"""
Given menu
Check display_menu displays the menu in the correct format
"""
def test_display_menu_with_items_on_menu():
    menu = Menu()
    menu.add_dish("Fish and Chips", 15)
    menu.add_dish("Burger", 13)
    menu.add_dish("Pasta", 10)
    assert menu.display_menu() == "Menu!\n\nFish and Chips: £15\nBurger: £13\nPasta: £10"