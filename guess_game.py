"""
A number guessing game
You can change the of the number to guess
You can also change the limit of amount of guess limit you have to increase your chances
Try it out, can you guess the number?
"""
import random

allocated_range = 41
secret_num = random.randrange(allocated_range)
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    try:
        guess = int(input("Guess number: "))
        if guess == secret_num:
            print("You won Yayyyyy!!!")
            break
        elif guess not in range(allocated_range):
            print("Guess within the range allocated please")
        elif guess != secret_num and guess_count < guess_limit:
            guess_count += 1
            if guess < secret_num:
                print("Try a higher number next time")
            else:
                print("Try a lower number next time")
    except ValueError:
        print("Please input a whole number instead")
else:
    print(f"You lost\nThe answer was {secret_num}\nBetter luck next time")
