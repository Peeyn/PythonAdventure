# A rock-paper-scissors game:
# Write a program that allows the user to play a game of rock-paper-scissors against the computer.
# You can use the random module to generate the computer's move.

# Optimized code of the rock-paper-scissors game

import random

def play_game():
  # list of play options
  plays = ["rock", "paper", "scissors"]

  # initialize game statistics
  player_wins = 0
  computer_wins = 0
  ties = 0

  while True:
    # print game statistics
    print(f"\nWins: {player_wins}")
    print(f"Losses: {computer_wins}")
    print(f"Ties: {ties}")

    # get player play
    player = input("\nEnter your play (rock, paper, scissors) or (q)uit: ")

    # check if player wants to quit
    if player == "q":
      break

    # check if player input is valid
    if player not in plays:
      print("Invalid play. Try again.")
      continue

    # get computer play
    computer = random.choice(plays)

    # determine winner
    if player == computer:
      print("Computer chose",computer,", Tie!")
      ties += 1
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
      print("Computer chose",computer,", You win!")
      player_wins += 1
    else:
      print("Computer chose",computer,", Computer wins!")
      computer_wins += 1

play_game()
