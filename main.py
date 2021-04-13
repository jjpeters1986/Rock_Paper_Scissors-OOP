import random
from rps_brain import RockPaperScissor

game = RockPaperScissor()

print("ROCK, PAPER, SCISSORS!")
print("The first to 5 points wins.")
print()

while game.is_winner() == False:
  game.play_round()
  game.current_score()


winner = game.the_winner_is()

print(f"The winner of this game is the {winner}.")
