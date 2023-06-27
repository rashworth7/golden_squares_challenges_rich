from lib.battle import *
from lib.game import *
from unittest.mock import Mock, patch



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
#     battle = Battle(player_1_game_mock, opponent_game_mock)
#     battle.format_player_board()
#     assert battle.show_player_board() == ("\n".join([
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
    mock_io = Mock()
    player_1_game_mock = Mock(rows=10, cols=10)
    player_2_game_mock = Mock(rows=10, cols=10)
    player_1_game_mock.opponent_board = ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                         '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                         '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                         '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                         '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                         '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                         '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                         '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                         '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                         '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']
    battle = Battle(mock_io, player_1_game_mock, player_2_game_mock)
    assert battle.show_opponent_board(player_1_game_mock) == "\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                                                        '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                                                        '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                                                        '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                                                        '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                                                        '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                                                        '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                                                        '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                                                        '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵',
                                                                        '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵'])
    

"""
fire inital shot, misses, marks as 0 on the board
"""
@patch.object(Game, 'ship_at')
def test_mark_missed_shot_on_opponent_board(ship_at_mock):
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    mock_io = Mock()
    player_1_game_mock.opponent_board = ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']


    # ship_at_mock.side_effect = lambda row, col: (row, col) in [(1, 3), (1, 2), (3, 4), (3, 5)]

    player_2_game_mock.ship_at.return_value = False
    
    player_2_game_mock.ships_placed = [
        Mock(coords=[(1, 3), (1, 2)], hit=2, length=2),
        Mock(coords=[(3, 4), (3, 5)], hit=2, length=2)
    ]

    player_2_game_mock.player_board = [['🔵' for _ in range(10)] for _ in range(10)]
    
    battle = Battle(mock_io, player_1_game_mock, player_2_game_mock)
    assert battle.place_shot(player_1_game_mock, player_2_game_mock, 1, 1) == "You missed!"
    
    assert player_1_game_mock.opponent_board == (['⚪🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵'])

"""
Fire initial shot, hits, marks as X on board
"""
@patch.object(Game, 'ship_at')
def test_inital_shot_hits(ship_at_mock):
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    mock_io = Mock()
    player_1_game_mock.opponent_board = ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']
    
    player_2_game_mock.ships_placed
    ship_at_mock.side_effect = lambda row, col: (row, col) == (1, 1)
    player_2_game_mock.ships_placed = [
        Mock(coords=[(1, 1), (1, 2)], hit=2),
        Mock(coords=[(3, 4), (3, 5)], hit=2)
    ]

    player_2_game_mock.player_board = [['🔵' for _ in range(10)] for _ in range(10)]

    battle = Battle(mock_io, player_1_game_mock, player_2_game_mock)
    assert battle.place_shot(player_1_game_mock, player_2_game_mock, 1, 1) == "You hit!"
    assert player_1_game_mock.opponent_board == ['💥🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']

"""
Fire shot, miss, fire shot, hit
"""

def test_miss_then_hit_shot():
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    mock_io = Mock()
    player_1_game_mock.opponent_board = ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']

    player_2_game_mock.ships_placed = [
        Mock(coords=[(1, 2), (1, 2)], hit=2),
        Mock(coords=[(3, 4), (5, 5)], hit=2)
    ]

    player_2_game_mock.player_board = [['🔵' for _ in range(10)] for _ in range(10)]
    player_2_game_mock.ship_at.return_value = False
    battle = Battle(mock_io, player_1_game_mock, player_2_game_mock)
    battle.place_shot(player_1_game_mock, player_2_game_mock, 1, 1)
    player_2_game_mock.ship_at.return_value = True
    assert battle.place_shot(player_1_game_mock, player_2_game_mock, 5, 5) == "You hit!"
    assert player_1_game_mock.opponent_board == ['⚪🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵💥🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']


"""
test show empty player 1 board with ships on
"""

def test_show_empty_player_board_with_ships_on():
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    mock_io = Mock()
    player_1_game_mock.player_board = ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']
    
    player_2_game_mock.player_board = [['.' for _ in range(10)] for _ in range(10)]
    battle = Battle(mock_io, player_1_game_mock, player_2_game_mock)
    result = battle.show_player_board(player_1_game_mock)
    assert result == "\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵'])

"""
test show empty opponent board for player 1
"""
def test_show_empty_opponent_board():
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    mock_io = Mock()
    player_1_game_mock.opponent_board = ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']
    battle = Battle(mock_io, player_1_game_mock, player_2_game_mock)
    result = battle.show_opponent_board(player_1_game_mock)
    assert result == "\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵'])

"""
initialise players own board from format board
"""

def test_initiliase_players_own_board():
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    mock_io = Mock()
    player_1_game_mock.rows = 10
    player_1_game_mock.cols = 10
    player_1_game_mock.player_board = []
    player_1_game_mock.ships_placed = [
        Mock(coords=[(3, 2), (4, 2)], length=2, orientation='vertical', row=3, col=2),
        Mock(coords=[(3, 3), (4, 3), (5, 3)], length=3, orientation='vertical', row=3, col=3),
        Mock(coords=[(3, 4), (4, 4), (5, 4)], length=3, orientation='vertical', row=3, col=4),
        Mock(coords=[(3, 5), (4, 5), (5, 5), (6, 5)], length=4, orientation='vertical', row=3, col=5),
        Mock(coords=[(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)], length=5, orientation='horizontal', row=2, col=2),
    ]
    battle = Battle(mock_io, player_1_game_mock, player_2_game_mock)
    battle.update_player_board_initial(player_1_game_mock)
    assert player_1_game_mock.player_board == ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫⚫🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']


"""
test player_2 makes a shot and hits, updates player 1 player board
"""
def test_player_2_makes_shot_and_hits_player_1_plaer_board_updated():
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    mock_io = Mock()
    player_1_game_mock.rows = 10
    player_1_game_mock.cols = 10
    player_1_game_mock.player_board = []
    player_2_game_mock.opponent_board = ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']
    player_1_game_mock.ships_placed = [
        Mock(coords=[(3, 2), (4, 2)], length=2, hit=2),
        Mock(coords=[(3, 3), (4, 3), (5, 3)], length=3, hit=3),
        Mock(coords=[(3, 4), (4, 4), (5, 4)], length=3, hit=3),
        Mock(coords=[(3, 5), (4, 5), (5, 5), (6, 5)], length=4, hit=4),
        Mock(coords=[(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)], length=5, hit=5),
    ]
    battle = Battle(mock_io, player_1_game_mock, player_2_game_mock)
    battle.update_player_board_initial(player_1_game_mock)
    battle.place_shot(player_2_game_mock, player_1_game_mock, 2, 2)
    
    assert player_1_game_mock.player_board == ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥⚫⚫⚫⚫🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']


"""
test player_2 makes a shot and hits, updates player 2 opponent board
"""
def test_player_2_makes_shot_hit_update_player_2_opponent_board():
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    mock_io = Mock()
    player_1_game_mock.rows = 10
    player_1_game_mock.cols = 10
    player_1_game_mock.player_board = []
    player_2_game_mock.opponent_board = ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']
    player_1_game_mock.ships_placed = [
        Mock(coords=[(3, 2), (4, 2)], length=2,  hit=2),
        Mock(coords=[(3, 3), (4, 3), (5, 3)], length=3, hit=3),
        Mock(coords=[(3, 4), (4, 4), (5, 4)], length=3, hit=3),
        Mock(coords=[(3, 5), (4, 5), (5, 5), (6, 5)], length=4, hit=4),
        Mock(coords=[(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)], length=5, hit=5),
    ]
    battle = Battle(mock_io, player_1_game_mock, player_2_game_mock)
    battle.update_player_board_initial(player_1_game_mock)
    battle.place_shot(player_2_game_mock, player_1_game_mock, 2, 2)
    
    assert player_2_game_mock.opponent_board == ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']

"""
test player_2 makes 3 shots, two hits and a miss.
Show player_1 player board (own board with ships)
Show player_2 opponent board with hit and miss markers
"""
def test_hit_twice_then_miss_show_other_player_own_board():
    player_1_game_mock = Mock()
    player_2_game_mock = Mock()
    mock_io = Mock()
    player_1_game_mock.rows = 10
    player_1_game_mock.cols = 10
    player_1_game_mock.player_board = []
    player_2_game_mock.opponent_board = ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵']
    player_1_game_mock.ships_placed = [
        Mock(coords=[(3, 2), (4, 2)], length=2, hit=2),
        Mock(coords=[(3, 3), (4, 3), (5, 3)], length=3, hit=3),
        Mock(coords=[(3, 4), (4, 4), (5, 4)], length=3, hit=3),
        Mock(coords=[(3, 5), (4, 5), (5, 5), (6, 5)], length=4, hit=4),
        Mock(coords=[(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)], length=5, hit=5),
    ]
    battle = Battle(mock_io, player_1_game_mock, player_2_game_mock)
    battle.update_player_board_initial(player_1_game_mock)
    battle.place_shot(player_2_game_mock, player_1_game_mock, 2, 2)
    battle.place_shot(player_2_game_mock, player_1_game_mock, 2, 3)
    player_1_game_mock.ship_at.return_value = False
    battle.place_shot(player_2_game_mock, player_1_game_mock, 10, 10)
    
    
    assert player_2_game_mock.opponent_board == ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵⚪']
    
    assert player_1_game_mock.player_board == ['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵💥💥⚫⚫⚫🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵⚫⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵⚫⚫⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵⚫🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵⚪']

