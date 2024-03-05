#Number Guessing Game

import random
import os
from art import logo

EASY_MODE = 10
HARD_MODE = 5

def check_answer (guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}.")
        
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_MODE
    else:
        return HARD_MODE

def game():
    print(logo)
    print("""\
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    """)
    answer  = random.randint(1,100)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print()
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess agin")

game()