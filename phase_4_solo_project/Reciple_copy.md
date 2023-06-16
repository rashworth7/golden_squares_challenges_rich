## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

Use the twilio-python package to implement this next one. You will need to use mocks too.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.


#Nouns
- list of dishes with prices (dict)
- itemised recipe with grand total

#Verbs
- see a list
- add to order (select dishes)
- verify order (display)
- recieve a text message


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

┌─────────────────────────────────┐
│                                 │
│ Text                            │
│                                 │
│ - send text confirmation        │
│                                 │
│                                 │
│                                 │
│                                 │
└─────────────────┬───────────────┘
                  │
                  │
                  │
                  │
                  │
                  │
                  │
 ┌────────────────▼────────────────┐
 │                                 │
 │ Order()                         │
 │                                 │
 │ - see a menu                    │
 │ - add to order(select dishes)   │
 │ - verify order                  │
 │ - place order                   │
 └────────────────┬────────────────┘
                  │
                  │
                  │
                  │
                  │
                  │
                  │
 ┌────────────────▼────────────────┐
 │                                 │
 │ Menu                            │
 │                                 │
 │ - initalise(dictionary menu)    │
 │ - add_dish(dish, price)         │
 │ - display menu                  │
 │                                 │
 │                                 │
 └─────────────────────────────────┘

_Also design the interface of each class in more detail._

```python

class TextConfirmation():

    def __init__(self, requester=requests, order):
        # Parameters:
        #   Requester - for testing
        #   order: instance of the Order class

    def format_message(self):
        # No params
        # returns:
        #   formatted message with ETA/arrive before

    def send_text(self, from_number, user_number):
        # No params
        # returns nothing
        # Side effects:
        #   formats message and sends text to the user's number if order has been placed
```
---------------------------------------------------------------------------------------------------------
```python

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
        pass

    def see_menu(self):
        # Returns:
        #   List of items and prices
        pass
    
    def add_to_order(self, item, quantity):
        # Parameters:
        #   item: string
        # Returns: nothing
        # Side effects:
        #   adds items to order 
        pass

    def verify_order(self):
        # Returns:
        #   formatted string showing number of items, cost and total cost
        pass

```
---------------------------------------------------------------------------------------------------------

```python

class Menu():
    #User facing properties
    #   dishes

    def __init__(self):
        # Parameters:
        #   dishes: dictionary of dishes and prices
        pass

    def add_dish(self, dish, price):
        # Parameters:
        #   dish: string
        #   pricer: float
        # Returns nothing
        # Side effects:
        #   the dishes to self.dishes

    def display_menu(self):
        # Returns:
        #   formatted list of dishes and prices
        # Side effects:
        #   the dishes to self.dishes



 ```   

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python


"""
3 items added
4 items chosen for order
test sending text from twillio if order has been placed

"""
menu = Menu()
menu.add("Fish and Chips": 15)
menu.add("Burger": 13)
menu.add("Pasta": 10)
order = Order(menu)
order.add_to_order("Fish and Chips", 2)
order.add_to_order("Burger", 2)
text_confirmation = TextConfirmation(order)
text_confirmation == "Message sent successfully"


```

-----------------------------------------------------------------------------


```python

## Order - Menu integrated tests ###


"""
test nothing added to menu
returns "Nothing on the menu"
"""
menu = Menu()
order = Order(menu)
order.menu == {}

"""
Given 3 items added to menu
Test see_menu display correct menu
"""
menu = Menu()
menu.add("Fish and Chips", 15)
menu.add("Burger", 13)
menu.add("Pasta", 10)
order = Order(menu)
order.see_menu # == "Menu!\n\nFish and chips: £15\nBurger: £13\nPasta: £10"

"""
Given 3 items added to menu
add 2 of each item to the order
verify order dsiplay correct items and amounts
"""
menu = Menu()
menu.add("Fish and Chips", 15)
menu.add("Burger", 13)
menu.add("Pasta", 10)
order = Order(menu)
order.add_to_order("Fish and Chips", 2)
order.add_to_order("Burger", 2)
order.verify_order # == "Order Details!\n\n2 x Fish and Chips: £30\n2 x Burger: £26\nTotal: £56"
```
-----------------------------------------------------------------------------
```python
"""
test nothing added to menu
returns "Nothing on the menu"
"""
menu = Menu()
order = Order(menu)
order.menu == {}

```
## 4. Create Examples as Unit Tests

## Unit Test TextConfirmation 

```python

"""
3 items added
4 items chosen for order
raises error when text_confirmation is called but no order is placed

"""

# create mocks here
text_confirmation = TextConfirmation(order)
text_confirmation == Exception("Error, no order was placed")

"""
Format_message formats the message correctly
"""
#Create mocks
text_confirmation = TextConfirmation(order)
assert text_confirmation.format_message() == "Thank you! Your order was placed and will be delivered before 18:52"

```

## Unit test Order()

```python

"""
Given Order
empty menu given
check that see menu returns a empty menu
"""
order = Order() #Mock menu needed here
order.see_menu # => ""

"""
Given Order
check that see menu returns a list of items and prices
"""
order = Order() #Mock menu needed here
order.see_menu # => "Menu!\n\nFish and chips: £15\nBurger: £13\nPasta: £10"

"""
Given Order
check that add_to_order() adds 2 different items to the order
"""
order = Order() #Mock menu needed here
order.add_to_order("Fish and chips", 1)
order.add_to_order("Buger", 1)
order.current_order# => {"Fish and Chips": 1, "Burger": 1}

"""
Given Order
check that add_to_order() adds 2 different items to the order over 1 of each
"""
order = Order() #Mock menu needed here
order.add_to_order("Fish and chips", 3)
order.add_to_order("Buger", 2)
order.current_order# => {"Fish and Chips": 3, "Burger": 2}

"""
Given Order
adds 2 different items to the order over 1 of each
Check verify order formats the correct reciept
"""
order = Order() #Mock menu needed here
order.verify_order() # => "Nothing added to order"

"""
Given Order
adds 2 different items to the order over 1 of each
Check verify order formats the correct reciept
"""
order = Order() #Mock menu needed here
order.add_to_order("Fish and chips", 3)
order.add_to_order("Pasta", 2)
order.verify_order() # => "Order Details!\n\n3 x Fish and Chips: £30\n2 x Pasta: £20\nTotal: £50"
```

------------------------------------------------------------------------------

## Unit test Menu

```python

"""
Given Menu
Check empty dishes
"""
menu = Menu()
assert menu.dishes == {}

"""
Given Menu
Check add_dish adds multiple dishes to the menu
"""
menu = Menu()
menu.add_dish("Fish and Chips", 15)
menu.add_dish("Burger", 13)
menu.add_dish("Pasta", 10)
menu.dishes == {"Fish and Chips": 15, "Burger": 13, "Pasta": 10}

"""
Given Menu
Check display menu display nothing if nothing added to menu
"""
menu = Menu()
menu.dsiplay_menu == "Nothing on the menu"

"""
Given menu
Check display_menu displays the menu in the correct format
"""

menu = Menu()
menu.add_dish("Fish and Chips", 15)
menu.add_dish("Burger", 13)
menu.add_dish("Pasta", 10)
menu.display_menu == "Menu!\n\nFish and Chips: £15\nBurger: £13\nPasta: 10"




```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._