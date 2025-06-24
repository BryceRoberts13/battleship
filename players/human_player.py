"""Human player class for the Battleship game."""

import re

from players.player import Player


class HumanPlayer(Player):
    """
    Human player class that extends the base Player class.
    Handles user input for ship placement and moves.
    """

    def place_ship(self, ship_type: str, ship_length: int) -> list[str | int]:
        """
        Place a ship on the board via terminal input.
        
        Args:
            ship_type: String representing the ship type
            ship_length: Integer representing the ship length
            
        Returns:
            Tuple: (row, col, orientation) where row and col are integers and orientation is 'H' or 'V'

        """
        while True:
            try:
                user_input = input(f"Enter placement for {ship_type} (length {ship_length}) - format: row,col,orientation (e.g., '0,0,h' or '1 2 v'): ").strip()

                # Remove all non-alphanumeric characters except spaces, then split
                # Extract numbers and letters separately
                numbers = re.findall(r"\d+", user_input)
                letters = re.findall(r"[hvHV]", user_input)

                if len(numbers) == 2 and len(letters) == 1:
                    row = int(numbers[0])
                    col = int(numbers[1])
                    orientation = letters[0].upper()

                    return (row, col, orientation)
                print("Invalid format. Please enter row, column, and orientation (h/v).")
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")


    def make_move(self, shots_taken: dict[tuple[int, int], int]) -> tuple[int, int]:
        """
        Make a move (shoot at coordinates) via terminal input.
        
        Args:
            shots_taken: Dictionary of shots taken by the player
            
        Returns:
            tuple: (row, col) coordinates to shoot at

        """
        return tuple(int(x) for x in input('Enter coordinates (input like "row, col") to shoot at: ').strip().split(", "))
