import random

class RockPaperScissor:

  def __init__(self):
    self.player_score = 0
    self.computer_score = 0
    self.computer_choices = ["rock", "paper", "scissors"]

  def is_winner(self):
    if self.player_score < 5 and self.computer_score < 5:
      return False
    else:
      return True

  def play_round(self):
    player_choice = input("Rock, Paper, or Scissors?: ").lower()
    pc_choice = random.choice(self.computer_choices)
    print(f"Computer Throws: {pc_choice}")
    if player_choice == "rock" and pc_choice == "rock":
      print("It's a tie!")
    elif player_choice == "rock" and pc_choice == "paper":
      print("You lose!")
      self.computer_score += 1
    elif player_choice == "rock" and pc_choice == "scissors":
      print("You win!")
      self.player_score += 1
    elif player_choice == "paper" and pc_choice == "paper":
      print("It's a tie!")
    elif player_choice == "paper" and pc_choice == "scissors":
      print("You lose!")
      self.computer_score += 1
    elif player_choice == "paper" and pc_choice == "rock":
      print("You win!")
      self.player_score += 1
    elif player_choice == "scissors" and pc_choice == "scissors":
      print("It's a tie!")
    elif player_choice == "scissors" and pc_choice == "rock":
      print("You lose!")
      self.computer_score += 1
    elif player_choice == "scissors" and pc_choice == "paper":
      print("You win!")
      self.player_score += 1

  def current_score(self):
    print()
    print(f"Player Score: {self.player_score}")
    print(f"Computer Score: {self.computer_score}")
    print()
    
  def the_winner_is(self):
    if self.player_score == 5:
      return "Player"
    else:
      return "Computer"
