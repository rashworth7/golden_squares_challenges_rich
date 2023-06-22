from lib.ship import Ship
from lib.ship_placement import ShipPlacement


class Game:
    def __init__(self, rows=10, cols=10):
        self.ships_placed = []
        self.rows = rows
        self.cols = cols
        self.unplaced_ships = [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5),
        ]
        self.player_board = []
        self.opponent_board = [
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
        self.ships_sunk = 0

    def place_ship(self, length, orientation, row, col):
        try:
            ship_lengths = [x.length for x in self.unplaced_ships]
            if length not in ship_lengths:
                raise Exception("Error, you've already placed that ship!")
            if abs(row) > self.rows or abs(col) > self.cols:
                raise Exception(f"""Error, you can't place your ship here. The board has {self.rows} rows and {self.cols} columns. Please try again!""")
            elif orientation == "vertical" and row + length - 1 > self.rows:
                raise Exception(f"Error, your ship is off the board, please start no higher than row {self.rows - length}")
            elif orientation == "horizontal" and col + length - 1 > self.cols:
                raise Exception(f"Error, your ship is off the board, please start no lower than column {self.cols - length}")

            ship_placement = ShipPlacement(
                length=length,
                orientation=orientation,
                row=row,
                col=col,
            )

            coordinates = []
            if ship_placement.orientation == "vertical":
                for i in range(length):
                    coordinates.append((row + i, col))
            else:
                for i in range(0, length):
                    coordinates.append((row, col + i))

            for coord in coordinates:
                if self.ship_at(coord[0], coord[1]):
                    raise Exception("Error, your ship is placed on another ship. Please try again")

            ship_placement.coords = coordinates

            for ship in self.unplaced_ships:
                if ship.length == length:
                    self.unplaced_ships.remove(ship)
                    break

            self.ships_placed.append(ship_placement)
            return "Ship placed"
        
        except Exception as e:
            return str(e)
            

    def ship_at(self, row, col):
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False