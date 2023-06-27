from lib.game import Game

class Battle:

    def __init__(self, io, player_1_game, player_2_game):
        self.player_1_game = player_1_game
        self.player_2_game = player_2_game
        self.io = io

    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    def _prompt_for_shot_placement(self, player, attackee):
        shot_there = True
        while shot_there:
            row_type = False
            col_type = False
            
            while row_type == False:
                row = self._prompt("Which row do you wish to attack?")
                if row.isdigit():
                    row_type = True

            while col_type == False:
                col = self._prompt("Which column do you wish to attack?")
                if col.isdigit():
                    col_type = True

            attack_row = list(player.opponent_board[int(row) - 1])

            if attack_row[int(col) - 1] == "💥":
                self._show("You've already placed a shot there")

            elif not (0 < int(row) < 11) or not (0 < int(col) < 11):
                self._show("That's off the board, please try again")
            else:
                shot_there = False
        result = self.place_shot(player, attackee, int(row), int(col))
        self._show(result)


    def run_battle_ships(self):
        game_on = True
        self.update_player_board_initial(self.player_1_game)
        self.update_player_board_initial(self.player_2_game)
        
        while game_on:
            self._show("Player 1, your turn to attack")
            self._show("Your Ships' board")
            self._show(self.show_player_board(self.player_1_game))
            self._show("Your attack board")
            self._show(self.show_opponent_board(self.player_1_game))
            self._prompt_for_shot_placement(self.player_1_game, self.player_2_game)
            is_game_over = self.game_over()
            if is_game_over:
                result = "Game over: Player 1 wins!"
                game_on = False
            
            self._show("Player 2, your turn to attack")
            self._show("Your Ships' board")
            self._show(self.show_player_board(self.player_2_game))
            self._show("Your attack board")
            self._show(self.show_opponent_board(self.player_2_game))
            self._prompt_for_shot_placement(self.player_2_game, self.player_1_game)
            is_game_over = self.game_over()
            if is_game_over:
                result = "Game over: Player 2 wins!"
                game_on = False
        
        self._show(result)
    
    def show_player_board(self, player):
        return "\n".join(player.player_board)

    def show_opponent_board(self, player):
        return "\n".join(player.opponent_board)

    def place_shot(self, player, attackee, row, col):

        if attackee.ship_at(row, col):
            self.update_boards_after_shot(player, attackee, row, col, "hit")
            result = self.update_opponents_ship_hit_marker(attackee, row, col)

        else:
            self.update_boards_after_shot(player, attackee, row, col, "miss")
            result = self.update_opponents_ship_hit_marker(attackee, row, col)
            
        return result

    def update_player_board_initial(self, player):
        ship_coordinates = []
        for ship in player.ships_placed:
            for coords in ship.coords:
                ship_coordinates.append(coords)
        player.player_board == []
        rows = []
        for row in range(1, player.rows + 1):
            row_cells = []
            for col in range(1, player.cols + 1):
                if (row, col) in ship_coordinates:
                    row_cells.append("⚫")
                else:
                    row_cells.append("🔵")
            rows.append("".join(row_cells))
        player.player_board = rows

    def update_boards_after_shot(self, player, attackee, row, col, hit_or_miss):
        player_opp_list_row = list(player.opponent_board[row - 1])
        attackee_player_row_list = list(attackee.player_board[row - 1])
        if hit_or_miss == "hit":
            player_opp_list_row[col - 1] = "💥"
            attackee_player_row_list[col - 1] = "💥"
        elif hit_or_miss == "miss":
            player_opp_list_row[col - 1] = "⚪"
            attackee_player_row_list[col - 1] = "⚪"

        player_opp_row = "".join(player_opp_list_row)
        player.opponent_board[row - 1] = player_opp_row
        

        attackee_player_row = "".join(attackee_player_row_list)
        attackee.player_board[row - 1] = attackee_player_row

    
    def update_opponents_ship_hit_marker(self, attackee, row, col):
        for ship in attackee.ships_placed:
            if (row, col) in ship.coords:
                ship.hit -= 1
                if ship.hit == 0:
                    attackee.ships_sunk += 1
                    return f"Hit! You sunk the ship length: {ship.length}"
                else:
                    return "You hit!"
                
        return "You missed!"
    

    def game_over(self):
        if self.player_1_game.ships_sunk == 5:
            return True
        elif self.player_2_game.ships_sunk == 5:
            return (True, "Game over: Player 1 wins!")
        else:
            return False



