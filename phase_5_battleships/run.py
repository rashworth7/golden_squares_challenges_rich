import sys
from lib.game import Game
from lib.battle import Battle
from lib.user_interface import UserInterface


class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)


io = TerminalIO()

player_1_game = Game()
user_interface = UserInterface(io, player_1_game)
user_interface.run()
    

player_2_game = Game()
user_interface = UserInterface(io, player_2_game)
user_interface.run()


battle = Battle(io, player_1_game, player_2_game)
battle.run_battle_ships()


