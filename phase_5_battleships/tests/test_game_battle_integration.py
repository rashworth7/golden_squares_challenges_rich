from lib.battle import *
from lib.game import *
from lib.ship_placement import *
import unittest
from unittest.mock import Mock
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock

"""
test shot hit updates hit on that ship
"""

def test_succesful_shot_updates_coordinates_of_ships_placed():
    player_2 = Game()
    player_2.place_ship(2, "vertical", 3, 2)
    player_2.place_ship(3, "vertical", 3, 3)
    player_2.place_ship(3, "vertical", 3, 4)
    player_2.place_ship(4, "vertical", 3, 5)
    player_2.place_ship(5, "horizontal", 2, 2)

    player_1 = Game()
    mock_io = Mock()

    battle = Battle(mock_io, player_1, player_2)
    
    battle.update_player_board_initial(player_2)
    battle.place_shot(player=player_1, attackee=player_2, row=3, col=2)

    assert player_2.ships_placed[0].hit == 1


"""
test 2 shots, two hits updates different ships
"""
def test_two_shots_hit_updates_hit_markers():
    player_2 = Game()
    player_2.place_ship(2, "vertical", 3, 2)
    player_2.place_ship(3, "vertical", 3, 3)
    player_2.place_ship(3, "vertical", 3, 4)
    player_2.place_ship(4, "vertical", 3, 5)
    player_2.place_ship(5, "horizontal", 2, 2)

    player_1 = Game()
    mock_io = Mock()

    battle = Battle(mock_io, player_1, player_2)
    
    battle.update_player_board_initial(player_2)
    battle.place_shot(player=player_1, attackee=player_2, row=3, col=2)
    battle.place_shot(player=player_1, attackee=player_2, row=2, col=4)

    assert player_2.ships_placed[0].hit == 1
    assert player_2.ships_placed[4].hit == 4


"""
if ship is sunk, increase number of ships sunk to 1
"""
def test_ships_sunk_increases_by_one_after_ship_is_sunk():
    player_2 = Game()
    player_2.place_ship(2, "vertical", 3, 2)
    player_2.place_ship(3, "vertical", 3, 3)
    player_2.place_ship(3, "vertical", 3, 4)
    player_2.place_ship(4, "vertical", 3, 5)
    player_2.place_ship(5, "horizontal", 2, 2)

    player_1 = Game()
    mock_io = Mock()

    battle = Battle(mock_io, player_1, player_2)
    
    battle.update_player_board_initial(player_2)
    battle.place_shot(player=player_1, attackee=player_2, row=3, col=2)
    battle.place_shot(player=player_1, attackee=player_2, row=4, col=2)

    assert player_2.ships_sunk == 1


"""
if two ships are sunk, increase number of ships sunk to 2
"""
def test_two_ships_sunk_increases_by_two_after_ship_is_sunk():
    player_2 = Game()
    player_2.place_ship(2, "vertical", 3, 2)
    player_2.place_ship(3, "vertical", 3, 3)
    player_2.place_ship(3, "vertical", 3, 4)
    player_2.place_ship(4, "vertical", 3, 5)
    player_2.place_ship(5, "horizontal", 2, 2)

    player_1 = Game()
    mock_io = Mock()

    battle = Battle(mock_io, player_1, player_2)
    
    battle.update_player_board_initial(player_2)
    battle.place_shot(player=player_1, attackee=player_2, row=3, col=2)
    battle.place_shot(player=player_1, attackee=player_2, row=4, col=2)
    battle.place_shot(player=player_1, attackee=player_2, row=3, col=3)
    battle.place_shot(player=player_1, attackee=player_2, row=4, col=3)
    battle.place_shot(player=player_1, attackee=player_2, row=5, col=3)

    assert player_2.ships_sunk == 2


"""
test game over if player has 5 sunk ships
"""
def test_game_over_function_returns_winner_after_sinking_all_ships():
    player_2 = Game()
    player_2.place_ship(2, "vertical", 3, 2)
    player_2.place_ship(3, "vertical", 3, 3)
    player_2.place_ship(3, "vertical", 3, 4)
    player_2.place_ship(4, "vertical", 3, 5)
    player_2.place_ship(5, "horizontal", 2, 2)

    player_1 = Game()
    mock_io = Mock()

    battle = Battle(mock_io, player_1, player_2)
    
    battle.update_player_board_initial(player_2)
    battle.place_shot(player=player_1, attackee=player_2, row=3, col=2)
    battle.place_shot(player=player_1, attackee=player_2, row=4, col=2)
    battle.place_shot(player=player_1, attackee=player_2, row=3, col=3)
    battle.place_shot(player=player_1, attackee=player_2, row=4, col=3)
    battle.place_shot(player=player_1, attackee=player_2, row=5, col=3)
    battle.place_shot(player=player_1, attackee=player_2, row=3, col=4)
    battle.place_shot(player=player_1, attackee=player_2, row=4, col=4)
    battle.place_shot(player=player_1, attackee=player_2, row=5, col=4)
    battle.place_shot(player=player_1, attackee=player_2, row=3, col=5)
    battle.place_shot(player=player_1, attackee=player_2, row=4, col=5)
    battle.place_shot(player=player_1, attackee=player_2, row=5, col=5)
    battle.place_shot(player=player_1, attackee=player_2, row=6, col=5)

    battle.place_shot(player=player_1, attackee=player_2, row=2, col=2)
    battle.place_shot(player=player_1, attackee=player_2, row=2, col=3)
    battle.place_shot(player=player_1, attackee=player_2, row=2, col=4)
    battle.place_shot(player=player_1, attackee=player_2, row=2, col=5)
    battle.place_shot(player=player_1, attackee=player_2, row=2, col=6)

    assert battle.game_over() == (True, "Game over: Player 1 wins!")


"""
take the shot, hits, return, you hit
"""

class TestUserInterface(unittest.TestCase):

    """
    test shot hit with user input
    """
    def test_user_takes_shot_returns_boards_and_message_you_hit(self):
        io = TerminalInterfaceHelperMock()
        player_1_game = Game()
        player_2_game = Game()

        player_1_game.player_board = [['🔵' for x in range(10)] for x in range(10)]
        player_2_game.player_board = [['🔵' for _ in range(10)] for _ in range(10)]

        player_1_game.opponent_board = [['🔵' for _ in range(10)] for _ in range(10)]
        player_2_game.opponent_board = [['🔵' for _ in range(10)] for _ in range(10)]

        player_2_game.place_ship(2, "vertical", 2, 2)

        battle = Battle(io, player_1_game, player_2_game)
        io.expect_print("Which row do you wish to attack?")
        io.provide("2")
        io.expect_print("Which column do you wish to attack?")
        io.provide("2")
        io.expect_print("You hit!")
        battle._prompt_for_shot_placement(player_1_game, player_2_game)

    """
    test missed shot with user input
    """
    def test_user_takes_shot_returns_boards_and_message_you_missed(self):
        io = TerminalInterfaceHelperMock()
        player_1_game = Game()
        player_2_game = Game()

        player_1_game.player_board = ["".join('🔵' for x in range(10)) for x in range(10)]
        player_2_game.player_board = ["".join('🔵' for x in range(10)) for x in range(10)]

        player_1_game.opponent_board = ["".join('🔵' for x in range(10)) for x in range(10)]
        player_2_game.opponent_board = ["".join('🔵' for x in range(10)) for x in range(10)]

        player_2_game.place_ship(2, "vertical", 2, 2)

        battle = Battle(io, player_1_game, player_2_game)
        io.expect_print("Which row do you wish to attack?")
        io.provide("2")
        io.expect_print("Which column do you wish to attack?")
        io.provide("3")
        io.expect_print("You missed!")
        battle._prompt_for_shot_placement(player_1_game, player_2_game)
        assert player_2_game.player_board == ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                              '🔵🔵⚪🔵🔵🔵🔵🔵🔵🔵',
                                              '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                              '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                              '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                              '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                              '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                              '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                              '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                              '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']
    
    def test_complete_game_played(self):
        io = TerminalInterfaceHelperMock()
        player_1_game = Game()
        player_2_game = Game()

        player_1_game.player_board = ["".join('🔵' for x in range(10)) for x in range(10)]
        player_2_game.player_board = ["".join('🔵' for x in range(10)) for x in range(10)]

        player_1_game.opponent_board = ["".join('🔵' for x in range(10)) for x in range(10)]
        player_2_game.opponent_board = ["".join('🔵' for x in range(10)) for x in range(10)]

        player_1_game.place_ship(2, "vertical", 5, 2) #(5,2) (6,2)
        player_1_game.place_ship(3, "vertical", 5, 3) #(5,3) (6,3) (7,3)
        player_1_game.place_ship(3, "vertical", 5, 4) #(5,4) (6,4) (7,4)
        player_1_game.place_ship(4, "vertical", 5, 5) #(5,5) (6,5) (7,5) (8,5)
        player_1_game.place_ship(5, "horizontal", 1, 2) #(1,2) ()

        player_2_game.place_ship(2, "vertical", 3, 2) #(3,2) (4,2)
        player_2_game.place_ship(3, "vertical", 3, 3) #(3,3) (4,3) (5,3)
        player_2_game.place_ship(3, "vertical", 3, 4) #(3,4) (4,4) (5,4)
        player_2_game.place_ship(4, "vertical", 3, 5) #(3,5) (4,5) (5,5) (6,5)
        player_2_game.place_ship(5, "horizontal", 2, 2) #(2,2) (2,3) (2,4) (2,5) (2,6)

        battle = Battle(io, player_1_game, player_2_game)

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵',
                                   '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵',
                                   '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("3")
        io.expect_print("Which column do you wish to attack?")
        io.provide("2")
        io.expect_print("You hit!")
        
        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵',
                                   '🔵💥⚫⚫⚫🔵🔵🔵🔵🔵',
                                   '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵',
                                   '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                   '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("1")
        io.expect_print("Which column do you wish to attack?")
        io.provide("2")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥⚫⚫⚫⚫🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("3")
        io.expect_print("Which column do you wish to attack?")
        io.provide("2")
        io.expect_print("You've already placed a shot there")
        io.expect_print("Which row do you wish to attack?")
        io.provide("4")
        io.expect_print("Which column do you wish to attack?")
        io.provide("2")
        io.expect_print("Hit! You sunk the ship length: 2")
        
        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥⚫⚫⚫🔵🔵🔵🔵🔵', '🔵💥⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("1")
        io.expect_print("Which column do you wish to attack?")
        io.provide("3")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥⚫⚫⚫🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("3")
        io.expect_print("Which column do you wish to attack?")
        io.provide("10")
        io.expect_print("You missed!")
        
        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥⚫⚫⚫🔵🔵🔵🔵⚪', '🔵💥⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("1")
        io.expect_print("Which column do you wish to attack?")
        io.provide("4")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥⚫⚫🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥🔵🔵🔵🔵🔵🔵🔵⚪', '🔵💥🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("3")
        io.expect_print("Which column do you wish to attack?")
        io.provide("3")
        io.expect_print("You hit!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥⚫⚫🔵🔵🔵🔵⚪', '🔵💥⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("1")
        io.expect_print("Which column do you wish to attack?")
        io.provide("5")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥⚫🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥🔵🔵🔵🔵🔵🔵⚪', '🔵💥🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("4")
        io.expect_print("Which column do you wish to attack?")
        io.provide("3")
        io.expect_print("You hit!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥⚫⚫🔵🔵🔵🔵⚪', '🔵💥💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("1")
        io.expect_print("Which column do you wish to attack?")
        io.provide("6")
        io.expect_print("Hit! You sunk the ship length: 5")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥🔵🔵🔵🔵🔵🔵⚪', '🔵💥💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("5")
        io.expect_print("Which column do you wish to attack?")
        io.provide("3")
        io.expect_print("Hit! You sunk the ship length: 3")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥⚫⚫🔵🔵🔵🔵⚪', '🔵💥💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("5")
        io.expect_print("Which column do you wish to attack?")
        io.provide("2")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥⚫⚫⚫🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥🔵🔵🔵🔵🔵🔵⚪', '🔵💥💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("3")
        io.expect_print("Which column do you wish to attack?")
        io.provide("4")
        io.expect_print("You hit!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵⚪', '🔵💥💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("6")
        io.expect_print("Which column do you wish to attack?")
        io.provide("2")
        io.expect_print("Hit! You sunk the ship length: 2")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥⚫⚫⚫🔵🔵🔵🔵🔵', '🔵💥⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵⚪', '🔵💥💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("4")
        io.expect_print("Which column do you wish to attack?")
        io.provide("4")
        io.expect_print("You hit!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵⚪', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("5")
        io.expect_print("Which column do you wish to attack?")
        io.provide("3")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥⚫⚫🔵🔵🔵🔵🔵', '🔵💥⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵⚪', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("5")
        io.expect_print("Which column do you wish to attack?")
        io.provide("4")
        io.expect_print("Hit! You sunk the ship length: 3")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵⚪', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥🔵🔵🔵🔵🔵🔵🔵', '🔵💥🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("6")
        io.expect_print("Which column do you wish to attack?")
        io.provide("3")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥⚫⚫🔵🔵🔵🔵🔵', '🔵💥💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵⚪', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("10")
        io.expect_print("Which column do you wish to attack?")
        io.provide("10")
        io.expect_print("You missed!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵⚪', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵⚪']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("7")
        io.expect_print("Which column do you wish to attack?")
        io.provide("3")
        io.expect_print("Hit! You sunk the ship length: 3")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥⚫⚫🔵🔵🔵🔵🔵', '🔵💥💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵⚪', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵⚪']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("10")
        io.expect_print("Which column do you wish to attack?")
        io.provide("9")
        io.expect_print("You missed!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵⚪', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵⚪⚪']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("5")
        io.expect_print("Which column do you wish to attack?")
        io.provide("4")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵💥💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵⚪', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵⚪⚪']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("10")
        io.expect_print("Which column do you wish to attack?")
        io.provide("8")
        io.expect_print("You missed!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵⚪', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵⚪⚪⚪']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵💥💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("6")
        io.expect_print("Which column do you wish to attack?")
        io.provide("4")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵⚪', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵⚪⚪⚪']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("10")
        io.expect_print("Which column do you wish to attack?")
        io.provide("7")
        io.expect_print("You missed!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵⚪', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵⚪⚪⚪⚪']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("7")
        io.expect_print("Which column do you wish to attack?")
        io.provide("4")
        io.expect_print("Hit! You sunk the ship length: 3")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵⚪', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵⚪⚪⚪⚪']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("10")
        io.expect_print("Which column do you wish to attack?")
        io.provide("6")
        io.expect_print("You missed!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵⚪', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵⚪⚪⚪⚪⚪']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("5")
        io.expect_print("Which column do you wish to attack?")
        io.provide("5")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥💥🔵🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵⚪', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵⚪⚪⚪⚪⚪']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("10")
        io.expect_print("Which column do you wish to attack?")
        io.provide("5")
        io.expect_print("You missed!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵⚪', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚪⚪⚪⚪⚪⚪']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥💥🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("6")
        io.expect_print("Which column do you wish to attack?")
        io.provide("5")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥💥🔵🔵🔵🔵🔵', '🔵💥💥💥💥🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵⚪', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚪⚪⚪⚪⚪⚪']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("10")
        io.expect_print("Which column do you wish to attack?")
        io.provide("4")
        io.expect_print("You missed!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵⚪', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵⚪⚪⚪⚪⚪⚪⚪']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥💥🔵🔵🔵🔵🔵', '🔵💥💥💥💥🔵🔵🔵🔵🔵', '🔵🔵💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("7")
        io.expect_print("Which column do you wish to attack?")
        io.provide("5")
        io.expect_print("You hit!")

        io.expect_print("Player 1, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥💥🔵🔵🔵🔵🔵', '🔵💥💥💥💥🔵🔵🔵🔵🔵', '🔵🔵💥💥💥🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥🔵🔵🔵🔵🔵⚪', '🔵💥💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵💥💥🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵⚪⚪⚪⚪⚪⚪⚪']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("10")
        io.expect_print("Which column do you wish to attack?")
        io.provide("3")
        io.expect_print("You missed!")

        io.expect_print("Player 2, your turn to attack")
        io.expect_print("Your Ships' board")
        io.expect_print("\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵💥💥💥⚫🔵🔵🔵🔵⚪', '🔵💥💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵💥💥⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵⚪⚪⚪⚪⚪⚪⚪⚪']))
        io.expect_print("Your attack board")
        io.expect_print("\n".join(['🔵💥💥💥💥💥🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥💥💥🔵🔵🔵🔵🔵', '🔵💥💥💥💥🔵🔵🔵🔵🔵', '🔵🔵💥💥💥🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']))
        io.expect_print("Which row do you wish to attack?")
        io.provide("8")
        io.expect_print("Which column do you wish to attack?")
        io.provide("5")
        io.expect_print("Hit! You sunk the ship length: 4")
        io.expect_print("Game over: Player 2 wins!")

        battle.run_battle_ships()




