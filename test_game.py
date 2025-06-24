"""Test cases and setup for the Battleship game runner and AI players."""

from core.game_runner import GameRunner
from players.random_ai import RandomAI

# Initialize game runner
game_runner = GameRunner()

# Set up both players as Random AI for testing
game_runner.player1 = RandomAI(10)
game_runner.player1.name = "Player 1 (AI)"
game_runner.player2 = RandomAI(10)
game_runner.player2.name = "Player 2 (AI)"

# Run ship placement phase
game_runner.ship_placement_phase()

# Game is now ready with all ships placed
print("\nGame initialized with all ships placed!")
print("You can now access the game state through game_runner.game")
