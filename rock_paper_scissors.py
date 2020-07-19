"""
A quick rock, paper, scissors game
The number of rounds can be changed without affect in game
Give it a try, can you beat the PC 
"""
import random

characters = ["rock", "paper", "scissors"]
player_input = None
computer_input = None
total_rounds = 3
rounds_played = 0

player_score = 0
computer_score = 0
while rounds_played < total_rounds:
    player_input = input("Input your character: ")
    computer_input = random.choice(characters)
    p = player_input.lower()
    c = computer_input
    if p not in characters:
        print("Please input the right character!")
    else:
        print(f"You played {p} and computer played {c}")
        rounds_played += 1
        if p == c:
            print("equal output")
        elif (p == "rock" and c == "paper") or (p == "paper" and c == "scissors") or (p == "scissors" and c == "rock"):
            computer_score += 1
            print("Computer won round!")
        else:
            player_score += 1
            print("You won round!")

if player_score > computer_score:
    print("You won\nCongratulations You Rock 😉")
elif player_score == computer_score:
    print("It's a tie")
else:
    print("You lost!!!\nBetter luck next time")
