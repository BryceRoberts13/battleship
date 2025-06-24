"""Base player class for the Battleship game."""

class Player:
    """Generic player class that can be inherited by human players and AI players."""

    PLACE_SHIP_ERROR_MSG: str = "Subclasses must implement place_ship method"
    MAKE_MOVE_ERROR_MSG: str = "Subclasses must implement make_move method"

    def __init__(self) -> None:
        pass

    def place_ship(self, ship_type: str, ship_length: int) -> list[str | int]:
        """
        Place a ship on the board.
            
        Returns:
            bool: True if placement is successful, False otherwise

        """
        raise NotImplementedError(self.PLACE_SHIP_ERROR_MSG)

    def make_move(self, shots_taken: dict[tuple[int, int], int]) -> tuple[int, int]:
        """
        Make a move (shoot at coordinates).
        
        Args:
            shots_taken: Dictionary of shots taken by the player
            
        Returns:
            tuple: (row, col) coordinates to shoot at
            where row and col are integers

        """
        raise NotImplementedError(self.MAKE_MOVE_ERROR_MSG)
