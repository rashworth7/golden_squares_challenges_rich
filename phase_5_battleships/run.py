import sys
from lib.game import Game
from lib.user_interface import UserInterface


class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)


io = TerminalIO()

game_1 = Game()
user_interface = UserInterface(io, game_1)
user_interface.run()
user_interface.run_board_set_up()
    

game_2 = Game()
user_interface = UserInterface(io, game_2)
user_interface.run()
user_interface.run_board_set_up()


user_1 = Game(game_1, game_2)
user_2 = Game(game_2, game_1)


