from lib.user import *
from lib.game import *
from lib.ship_placement import *
from unittest.mock import Mock

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

    player_1_user = User(player_1, player_2)
    
    player_1_user.place_shot(player=player_1, attackee=player_2, row=3, col=2)

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

    player_user = User(player_1, player_2)
    
    player_user.place_shot(player=player_1, attackee=player_2, row=3, col=2)
    player_user.place_shot(player=player_1, attackee=player_2, row=2, col=4)

    assert player_2.ships_placed[0].hit == 1
    assert player_2.ships_placed[4].hit == 4


    


