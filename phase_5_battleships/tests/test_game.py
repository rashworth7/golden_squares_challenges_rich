from lib.game import Game
import pytest

"""
Initialises with a length and width of 10
"""
def test_initialises_with_a_length_and_width_of_10():
    game = Game()
    assert game.rows == 10
    assert game.cols == 10

"""
Initialises with five ships of length 2, 3, 3, 4, 5
"""
def test_initialises_with_five_ships_of_right_length():
    game = Game()
    unplaced_ships = game.unplaced_ships
    assert len(unplaced_ships) == 5
    assert unplaced_ships[0].length == 2
    assert unplaced_ships[1].length == 3
    assert unplaced_ships[2].length == 3
    assert unplaced_ships[3].length == 4
    assert unplaced_ships[4].length == 5

"""
Initialises with a totally empty board
"""
def test_initialises_with_a_totally_empty_board():
    game = Game()
    for row in range(1, 11):
        for col in range(1, 11):
            assert not game.ship_at(row, col)

"""
When we place a ship
Then its place on the board is marked out
"""
def test_when_we_place_a_ship_then_its_place_on_the_board_is_marked_out():
    game = Game()
    game.place_ship(length=2, orientation="vertical", row=3, col=2)
    assert game.ship_at(3, 2)
    assert game.ship_at(4, 2)
    assert not game.ship_at(3, 3)
    assert not game.ship_at(4, 3)
    assert not game.ship_at(3, 1)
    assert not game.ship_at(4, 1)

"""
Ship placement off board returns error
"""

def test_ship_not_on_board_returns_error():
    game = Game()
    result = game.place_ship(5, orientation="vertical", row=15, col=15) 
    assert result == """Error, you can't place your ship here. The board has 10 rows and 10 columns. Please try again!"""


"""
Ship placement on board but end is off board, verticle
"""

def test_ship_starts_on_board_finishes_off_verticle():
    game = Game()
    result = game.place_ship(5, orientation="vertical", row=9, col=9) 
    assert result == "Error, your ship is off the board, please start no higher than row 5"

"""
Ship placement on board but end is off board, horizontal
"""
def test_ship_starts_on_board_finishes_of_hor():
    game = Game()
    result = game.place_ship(5, orientation="horizontal", row=9, col=9)
    assert result == "Error, your ship is off the board, please start no lower than column 5"

"""
Ship placement over another ship
"""
def test_ship_on_another_ship():
    game = Game()
    game.place_ship(3, orientation="horizontal", row=3, col=3) #(3,3) (3,4) (3,5)
    result = game.place_ship(3, orientation="vertical", row=1, col=3) #(1,3) (2,3) (3,3)
    assert result == "Error, your ship is placed on another ship. Please try again"

"""
Trying to place an already placed ship returns error
"""
def test_ship_already_placed():
    game = Game()
    game.place_ship(2, orientation="horizontal", row=3, col=3) #(3,3) (3,4) (3,5)
    result = game.place_ship(2, orientation="vertical", row=1, col=3) #(1,3) (2,3) (3,3)
    assert result == "Error, you've already placed that ship!"

