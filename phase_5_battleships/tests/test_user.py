from lib.user import *
from lib.game import *
from unittest.mock import Mock

"""
Test format board correct formats initial player board
"""
def test_format_board_creates_correct_first_board():
    layer_game_mock = Mock()
    opponent_game_mock = Mock()


"""
show player board fully complete
"""
# def test_show_player_board_complete():
#     player_1_game_mock = Mock(rows=10, cols=10)
#     opponent_game_mock = Mock(rows=10, cols=10)
#     mock_ships_placement = [Mock(length=2, orientation="vertical", row=3, col=2), 
#                             Mock(length=3, orientation="vertical", row=3, col=3),
#                             Mock(length=3, orientation="vertical", row=3, col=4),
#                             Mock(length=4, orientation="vertical", row=3, col=5),
#                             Mock(length=5, orientation="horizontal", row=2, col=2)
#                                  ]
#     player_1_game_mock.ships_placed = mock_ships_placement
#     player_1_user = User(player_1_game_mock, opponent_game_mock)
#     player_1_user.format_player_board()
#     assert player_1_user.show_player_board() == ("\n".join([
#             "..........",
#             ".SSSSS....",
#             ".SSSS.....",
#             ".SSSS.....",
#             "..SSS.....",
#             "....S.....",
#             "..........",
#             "..........",
#             "..........",
#             ".........."
#             ]))

"""
Shows initial oppenent board as blank board
"""

def test_show_initial_opponent_board():
    player_1_game_mock = Mock(rows=10, cols=10)
    player_2_game_mock = Mock(rows=10, cols=10)
    player_1_game_mock.opponent_board = [
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
            ]
    player_1_user = User(player_1_game_mock, player_2_game_mock)
    assert player_1_user.show_opponent_board(player_1_game_mock) == "\n".join([
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
            ])
    

"""
fire inital shot, misses, marks as 0 on the board
"""
def test_mark_missed_shot_on_opponent_board():
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    player_1_game_mock.opponent_board = [
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
    ]
    player_2_game_mock.ship_at.return_value = False
    player_2_game_mock.ships_placed = [
        Mock(coords=[(1, 3), (1, 2)], hit=2),
        Mock(coords=[(3, 4), (3, 5)], hit=2)
    ]
    
    player_1_user = User(player_1_game_mock, player_2_game_mock)
    assert player_1_user.place_shot(player_1_game_mock, player_2_game_mock, 1, 1) == "You missed!"
    print(f"game board is {player_1_game_mock.opponent_board}")
    assert player_1_game_mock.opponent_board == ([
            "0.........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
    ])

"""
Fire initial shot, hits, marks as X on board
"""
def test_inital_shot_hits():
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    player_1_game_mock.opponent_board = [
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
    ]
    
    player_2_game_mock.ship_at.return_value = True
    player_2_game_mock.ships_placed = [
        Mock(coords=[(1, 1), (1, 2)], hit=2),
        Mock(coords=[(3, 4), (3, 5)], hit=2)
    ]

    player_1_user = User(player_1_game_mock, player_2_game_mock)
    assert player_1_user.place_shot(player_1_game_mock, player_2_game_mock, 1, 1) == "You hit!"
    assert player_1_game_mock.opponent_board == [
            "X.........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
    ]

"""
Fire shot, miss, fire shot, hit
"""

def test_miss_then_hit_shot():
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    player_1_game_mock.opponent_board = [
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
    ]

    player_2_game_mock.ships_placed = [
        Mock(coords=[(1, 1), (1, 2)], hit=2),
        Mock(coords=[(3, 4), (5, 5)], hit=2)
    ]
    player_2_game_mock.ship_at.return_value = False
    player_1_user = User(player_1_game_mock, player_2_game_mock)
    player_1_user.place_shot(player_1_game_mock, player_2_game_mock, 1, 1)
    player_2_game_mock.ship_at.return_value = True
    assert player_1_user.place_shot(player_1_game_mock, player_2_game_mock, 5, 5) == "You hit!"
    assert player_1_game_mock.opponent_board == [
            "0.........",
            "..........",
            "..........",
            "..........",
            "....X.....",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
    ]


"""

"""