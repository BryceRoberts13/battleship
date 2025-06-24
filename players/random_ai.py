import random

from players.player import Player


class RandomAI(Player):
    """
    Random AI player class that extends the base Player class.

    Makes random moves and ship placements.
    """

    def __init__(self, board_size: int) -> None:
        super().__init__()
        self.board_size: int = board_size

    def place_ship(self, _ship_type: str, _ship_length: int) -> tuple[int, int, str]:
        """
        Place a ship on the board randomly.
        
        Args:
            ship_type: String representing the ship type
            ship_length: Integer representing the ship length
            
        Returns:
            tuple: (start_coords, orientation) where start_coords is (row, col) and orientation is 'H' or 'V'

        """
        orientation: str = random.choice(["H", "V"])

        if orientation == "H":
            # For horizontal placement, ensure ship fits within board width
            max_col: int = self.board_size - _ship_length
            row: int = random.randint(0, self.board_size - 1)
            col: int = random.randint(0, max_col)
        else:  # orientation == 'V'
            # For vertical placement, ensure ship fits within board height
            max_row: int = self.board_size - _ship_length
            row: int = random.randint(0, max_row)
            col: int = random.randint(0, self.board_size - 1)

        return (row, col, orientation)

    def make_move(self, shots_taken: dict[tuple[int, int], int]) -> tuple[int, int]:
        """
        Make a random move (shoot at coordinates).
        
        Args:
            shots_taken: Dictionary of shots taken by the player
        Returns:
            tuple: (row, col) coordinates to shoot at

        """
        # Generate random coordinates that haven't been shot at yet
        while True:
            row: int = random.randint(0, self.board_size - 1)
            col: int = random.randint(0, self.board_size - 1)
            coords: tuple[int, int] = (row, col)

            # Check if this coordinate hasn't been shot at yet
            if coords not in shots_taken:
                return coords
