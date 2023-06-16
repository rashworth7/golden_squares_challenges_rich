from unittest.mock import Mock
from lib.text import TextConfirmation
from lib.order import Order
from lib.menu import Menu


"""
3 items added
4 items chosen for order
test sending text from twillio if order has been placed
"""
def test_send_text_from_twillio_if_order_placed():
    menu = Menu()
    menu.add_dish("Fish and Chips", 15)
    menu.add_dish("Burger", 13)
    menu.add_dish("Pasta", 10)
    order = Order(menu)
    order.add_to_order("Fish and Chips", 2)
    order.add_to_order("Burger", 2)
    text_confirmation = TextConfirmation(order)
    final = text_confirmation.send_text("+447525093691")
    print(final)
    # assert text_confirmation.send_text(message, "+447525093691") == "Message sent successfully"


# ## Order - Menu integrated tests ###





# """
# test nothing added to menu
# returns "Nothing on the menu"
# """
# menu = Menu()
# order = Order(menu)
# order.menu == {}

# """
# Given 3 items added to menu
# Test see_menu display correct menu
# """
# menu = Menu()
# menu.add("Fish and Chips", 15)
# menu.add("Burger", 13)
# menu.add("Pasta", 10)
# order = Order(menu)
# order.see_menu # == "Menu!\n\nFish and chips: £15\nBurger: £13\nPasta: £10"

# """
# Given 3 items added to menu
# add 2 of each item to the order
# verify order dsiplay correct items and amounts
# """
# menu = Menu()
# menu.add("Fish and Chips", 15)
# menu.add("Burger", 13)
# menu.add("Pasta", 10)
# order = Order(menu)
# order.add_to_order("Fish and Chips", 2)
# order.add_to_order("Burger", 2)
# order.verify_order # == "Order Details!\n\n2 x Fish and Chips: £30\n2 x Burger: £26\nTotal: £56"