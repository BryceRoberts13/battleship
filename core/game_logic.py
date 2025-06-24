"""Game logic for the Battleship game."""

class Game:
    """Represents the game logic for Battleship, managing the board, ship placements, moves, and win conditions."""

    # Error messages
    SHIP_PLACEMENT_OUT_OF_BOUNDS_MSG: str = "Ship placement out of bounds: {start_coords} with orientation {orientation}"
    SHIP_OVERLAP_MSG: str = "Ship placement overlaps with another ship: {start_coords} with orientation {orientation}"
    INVALID_MOVE_FORMAT_MSG: str = "Invalid move coordinates: {coords} is not a tuples wiht length 2"
    INVALID_MOVE_INT_MSG: str = "Invalid move coordinates: {coords} are not integers"
    MOVE_OUT_OF_BOUNDS_MSG: str = "Move coordinates are out of bounds: {coords}"
    MOVE_ALREADY_SHOT_MSG: str = "Move coordinates have already been shot at: {coords}"
    INVALID_SHIP_TYPE_MSG: str = "Invalid ship type: {ship_type}"
    COORDS_LENGTH: int = 2 # Constant for the expected length of coordinate tuples

    def __init__(self) -> None:
        self.board_size: int = 10
        self.ships_config: dict[str, int] = {
            "Carrier": 5,
            # "Battleship": 4,
            # "Cruiser": 3,
            # "Submarine": 3,
            # "Destroyer": 2
        }
        self.player_data: dict[str, dict[str, dict[tuple[int, int], int]]] = {
            "player1": {
                "shots": {},
                "board": {(a, b): 0 for a in range(self.board_size) for b in range(self.board_size)},
                "hits_left": {},
            },
            "player2": {
                "shots": {},
                "board": {(a, b): 0 for a in range(self.board_size) for b in range(self.board_size)},
                "hits_left": {},
            },
        }

    def is_valid_ship_placement(self, player: str, ship_type: str, start_coords: tuple[int, int], orientation: str) -> bool:
        """
        Check if a ship placement is valid (coordinates are within bounds and not already played).
        
        Args:
            player: String representing the player ('player1' or 'player2')
            ship_type: String representing the ship type
            start_coords: Tuple of (row, col) coordinates
            orientation: String representing the orientation ('H' for horizontal, 'V' for vertical)
            
        Returns:
            bool: True if placement is valid, False otherwise

        """
        player_board = self.player_data[player]["board"]
        if ship_type not in self.ships_config:
            raise ValueError(self.INVALID_SHIP_TYPE_MSG.format(ship_type=ship_type))

        length = self.ships_config[ship_type]
        row, col = start_coords

        if orientation == "H":
            if col + length > self.board_size:
                raise ValueError(self.SHIP_PLACEMENT_OUT_OF_BOUNDS_MSG.format(start_coords=start_coords, orientation=orientation))
            for i in range(length):
                if player_board[(row, col + i)] != 0:
                    raise ValueError(self.SHIP_OVERLAP_MSG.format(start_coords=start_coords, orientation=orientation))
        elif orientation == "V":
            if row + length > self.board_size:
                raise ValueError(self.SHIP_PLACEMENT_OUT_OF_BOUNDS_MSG.format(start_coords=start_coords, orientation=orientation))
            for i in range(length):
                if player_board[(row + i, col)] != 0:
                    raise ValueError(self.SHIP_OVERLAP_MSG.format(start_coords=start_coords, orientation=orientation))
        return True

    def place_ship(self, player: str, ship_type: str, start_coords: tuple[int, int], orientation: str) -> None:
        """
        Place a ship on the board assuming the placement is valid.
        
        Args:
            player: String representing the player ('player1' or 'player2')
            ship_type: String representing the ship type
            start_coords: Tuple of (row, col) coordinates
            orientation: String representing the orientation ('H' for horizontal, 'V' for vertical)
            
        Returns:
            bool: True if placement is valid, False otherwise

        """
        player_board = self.player_data[player]["board"]
        # add opponent's ships to the player's ships left
        player_ships_left = self.player_data["player2"]["hits_left"] if player == "player1" else self.player_data["player1"]["hits_left"]
        length = self.ships_config[ship_type]
        row, col = start_coords
        if orientation == "H":
            for i in range(length):
                player_board[(row, col + i)] = 1
                player_ships_left[(row, col + i)] = 1
        elif orientation == "V":
            for i in range(length):
                player_board[(row + i, col)] = 1
                player_ships_left[(row + i, col)] = 1

    def is_valid_move(self, player: str, coords: tuple[int, int]) -> bool:
        """
        Check if a move is valid (coordinates are within bounds and not already played).
        
        Args:
            player: String representing the player ('player1' or 'player2')
            coords: Tuple of (row, col) coordinates
            
        Returns:
            bool: True if move is valid, False otherwise

        """
        if not isinstance(coords, tuple) or len(coords) != self.COORDS_LENGTH:
            raise TypeError(self.INVALID_MOVE_FORMAT_MSG.format(coords=coords))

        row, col = coords

        if not isinstance(row, int) or not isinstance(col, int):
            raise TypeError(self.INVALID_MOVE_INT_MSG.format(coords=coords))

        # Check if coordinates are within board bounds
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            raise ValueError(self.MOVE_OUT_OF_BOUNDS_MSG.format(coords=coords))

        # Check if this position has already been shot at
        player_shots = self.player_data[player]["shots"]
        if coords in player_shots:
            raise ValueError(self.MOVE_ALREADY_SHOT_MSG.format(coords=coords))
        return True

    def apply_move(self, player: str, coords: tuple[int, int]) -> bool:
        """
        Apply a move to the board.
        
        Args:
            player: String representing the player ('player1' or 'player2')
            coords: Tuple of (row, col) coordinates
            
        Returns:
            bool: True if move is valid, False otherwise

        """
        player_shots = self.player_data[player]["shots"]
        player_board = self.player_data[player]["board"]
        player_ships_left = self.player_data["player1"]["hits_left"] if player == "player1" else self.player_data["player2"]["hits_left"]

        is_hit = False
        if player_board[coords] == 1:
            player_shots[coords] = 1
            # remove the ship from the player's ships left
            player_ships_left.pop(coords)
            is_hit = True
        else:
            player_shots[coords] = 0
        return is_hit

    def check_win(self, player: str) -> bool:
        """
        Check if a player has won the game.
        
        Args:
            player: String representing the player ('player1' or 'player2')
            
        Returns:
            bool: True if player has won, False otherwise

        """
        player_ships_left = self.player_data[player]["hits_left"]
        return len(player_ships_left) == 0 ## how long does this take
