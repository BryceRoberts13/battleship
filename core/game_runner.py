
from core.game_logic import Game
from players.human_player import HumanPlayer
from players.player import Player  # Import the base Player class
from players.random_ai import RandomAI


class GameRunner:
    """Main game runner that controls the flow of the battleship game."""

    def __init__(self) -> None:
        self.game: Game = Game()
        self.player1: HumanPlayer | RandomAI | None = None
        self.player2: HumanPlayer | RandomAI | None = None

    def select_players(self) -> None:
        """Allow users to select player types for player 1 and player 2."""
        print("Welcome to Battleship!")
        print("Player types: 1 = Human, 2 = Random AI")

        # Select Player 1
        while True:
            try:
                choice = int(input("Select Player 1 type (1 or 2): "))
                if choice == 1:
                    self.player1 = HumanPlayer()
                    self.player1.name = "Player 1 (Human)"
                    break
                if choice == 2:
                    self.player1 = RandomAI(self.game.board_size) # Pass board_size to RandomAI
                    self.player1.name = "Player 1 (AI)"
                    break
                print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Select Player 2
        while True:
            try:
                choice = int(input("Select Player 2 type (1 or 2): "))
                if choice == 1:
                    self.player2 = HumanPlayer()
                    self.player2.name = "Player 2 (Human)"
                    break
                if choice == 2:
                    self.player2 = RandomAI(self.game.board_size) # Pass board_size to RandomAI
                    self.player2.name = "Player 2 (AI)"
                    break
                print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def ship_placement_phase(self) -> None:
        """Handle ship placement for both players."""
        print("\n=== Ship Placement Phase ===")

        # Player 1 ship placement
        print(f"\n{self.player1.name} - Place your ships:")
        self.place_ships_for_player("player1", self.player1)

        # Player 2 ship placement
        print(f"\n{self.player2.name} - Place your ships:")
        self.place_ships_for_player("player2", self.player2)

    def place_ships_for_player(self, player_key: str, player_obj: Player) -> None:
        """
        Handle ship placement for a single player.

        Args:
            player_key: String ('player1' or 'player2')
            player_obj: Player object (HumanPlayer or RandomAI)

        """
        for ship_type, ship_length in self.game.ships_config.items():
            while True:
                try:
                    # Get ship placement from player
                    placement = player_obj.place_ship(ship_type, ship_length)

                    # Parse placement data
                    def validate_placement_format():
                        if len(placement) != 3:
                            raise ValueError("Invalid placement format")

                    validate_placement_format()

                    row, col, orientation = int(placement[0]), int(placement[1]), placement[2].upper()
                    start_coords = (row, col)

                    # Validate and place ship
                    if self.game.is_valid_ship_placement(player_key, ship_type, start_coords, orientation):
                        self.game.place_ship(player_key, ship_type, start_coords, orientation)
                        print(f"Successfully placed {ship_type} at {start_coords} with orientation {orientation}")
                        break

                except (ValueError, IndexError) as e:
                    print(f"Invalid placement: {e}. Please try again.")

    def battle_phase(self) -> None:
        """Handle the main battle phase where players take turns making moves."""
        print("\n=== Battle Phase ===")
        current_player: str = "player1"
        current_player_obj: Player = self.player1

        while True:
            print(f"\n{current_player_obj.name}'s turn:")

            # Get player's move
            while True:
                try:
                    # Get shots taken by current player
                    shots_taken: dict[tuple[int, int], int] = self.game.player_data[current_player]["shots"]

                    # Get move from player
                    move: tuple[int, int] = current_player_obj.make_move(shots_taken)

                    # Parse move data
                    if self.game.is_valid_move(current_player, move):
                        # Apply the move (note: we need to target the opponent's board)
                        is_hit: bool = self.game.apply_move(current_player, move)
                    else:
                        raise ValueError("Invalid move")

                    if is_hit:
                        print(f"Hit at {move}!")
                    else:
                        print(f"Miss at {move}.")

                    # Record the shot for the current player
                    shots_taken[move] = 1 if is_hit else 0
                    break

                except (ValueError, IndexError) as e:
                    print(f"Invalid move: {e}. Please try again.")

            # Check for win condition
            if self.game.check_win(current_player):
                print(f"\n{current_player_obj.name} wins! All opponent ships have been sunk!")
                break

            # Switch players
            if current_player == "player1":
                current_player = "player2"
                current_player_obj = self.player2
            else:
                current_player = "player1"
                current_player_obj = self.player1

    def run_game(self) -> None:
        """Run the complete battleship game."""
        self.select_players()
        self.ship_placement_phase()
        self.battle_phase()
        print("\nThanks for playing Battleship!")

# Main execution
if __name__ == "__main__":
    game_runner = GameRunner()
    game_runner.run_game()
