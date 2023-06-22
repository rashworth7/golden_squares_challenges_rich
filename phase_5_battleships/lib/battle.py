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
        row = self._prompt("Which row do you wish to target?")
        col = self._prompt("Which column do you wish to attach?")
        result = self.place_shot(player, attackee, int(row), int(col))
        self._show(result)


    # def _prompt_for_ship_placement(self):
    #     ship_length = self._prompt("Which do you wish to place?")
    #     ship_orientation = self._prompt("Vertical or horizontal? [vh]")
    #     ship_row = self._prompt("Which row?")
    #     ship_col = self._prompt("Which column?")
    #     self._show("OK.")
    #     outcome = self.game.place_ship(
    #         length=int(ship_length),
    #         orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
    #         row=int(ship_row),
    #         col=int(ship_col),
    #     )
    #     self._show(outcome)


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
            (game_on, result) = self.game_over()

            self._show("Player 2, your turn to attack")
            self._show("Your Ships' board")
            self.show_player_board(self.player_2_game)
            self._show("Your attack board")
            self.show_opponent_board(self.player_2_game)
            self._prompt_for_shot_placement(self.player_2_game, self.player_1_game)
            (game_on, result) = self.game_over()
        
        self._show(result)
    
    def show_player_board(self, player):
        return "\n".join(player.player_board)

    def show_opponent_board(self, player):
        return "\n".join(player.opponent_board)

    def place_shot(self, player, attackee, row, col):
        if attackee.ship_at(row, col):
            self.update_boards_after_shot(player, attackee, row, col, "hit")
            # board_row = list(player.opponent_board[row - 1])
            # board_row[col - 1] = "X"
            # player_opp_row = "".join(board_row)
            # player.opponent_board[row - 1] = player_opp_row
            result = self.update_opponents_ship_hit_marker(attackee, row, col)

        else:
            self.update_boards_after_shot(player, attackee, row, col, "miss")
            # board_row = list(player.opponent_board[row - 1])
            # board_row[col - 1] = "0"
            # player_opp_row = "".join(board_row)
            # player.opponent_board[row - 1] = player_opp_row
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
                    row_cells.append("S")
                else:
                    row_cells.append(".")
            rows.append("".join(row_cells))
        player.player_board = rows

    def update_boards_after_shot(self, player, attackee, row, col, hit):
        # player hits attackee

        # update player opponent board
        player_opp_list_row = list(player.opponent_board[row - 1])
        attackee_player_row_list = list(attackee.player_board[row - 1])
        if hit == "hit":
            player_opp_list_row[col - 1] = "X"
            attackee_player_row_list[col - 1] = "X"
        elif hit == "miss":
            player_opp_list_row[col - 1] = "0"
            attackee_player_row_list[col - 1] = "0"

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
            return (True, "Game over: Player 2 wins!")
        elif self.player_2_game.ships_sunk == 5:
            return (True, "Game over: Player 1 wins!")
        else:
            return False



