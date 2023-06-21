from lib.game import Game

class User:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
      
    def run_battle_ships(self):
        pass
    
    def show_player_board(self, player):
        
        return player.player_board

    def show_opponent_board(self, player):
        return "\n".join(player.opponent_board)

    def place_shot(self, player, attackee, row, col):
        if attackee.ship_at(row, col):
            board_row = list(player.opponent_board[row - 1])
            board_row[col - 1] = "X"
            new_board_row = "".join(board_row)
            player.opponent_board[row - 1] = new_board_row
            result = self.update_opponents_ship_hit_marker(attackee, row, col)
            

        else:
            board_row = list(player.opponent_board[row - 1])
            board_row[col - 1] = "0"
            new_board_row = "".join(board_row)
            player.opponent_board[row - 1] = new_board_row
            result = self.update_opponents_ship_hit_marker(attackee, row, col)
            
        return result

    def update_player_board(self):
        pass

    def update_opponents_ship_hit_marker(self, attackee, row, col):
        print(attackee.ships_placed)
        for ship in attackee.ships_placed:
            if (row, col) in ship.coords:
                ship.hit -= 1
                return "You hit!"
                
        return "You missed!"
        

        


