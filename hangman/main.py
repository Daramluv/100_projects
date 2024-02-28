import random
from hangman_art import logo, stages
from hangman_words import word_list
import os
import sys

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    #LOGO 프린트하기
    print(logo)

    #Generating Random Word
    chosen_word = random.choice(word_list)
    

    #목숨갯수
    lives = 6

    #단어별 "_" 추가하기
    display = []
    for _ in range(len(chosen_word)):
        display.append("_")

    print(display)
    print()
    #게임 반복
    end_of_game = False

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        clear_console()

        if guess in display:
            print("You've already gussed {guess}")

        #check guessed letter
        for i in range(len(chosen_word)):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = letter
                print("You guessed the letter")
        #check if user is wrong.
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. you lose a life")
            if lives == 0:
                end_of_game = True
                print("You lose")
        
        #Join all the elements in the list and turn it into a string
        print(f"{' '.join(display)}")

        #check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You Win!")

        print(stages[lives])

    #게임이 종료되면 사용자에게 다시 게임을 할 것인지 물어봄
    y_n = False
    while not y_n:
        play_again = input("Do you want to play again? Y/N: ").lower()
        if play_again in ["y", "n"]:
            y_n = True
        else:
            y_n = False
            print("Y or N를 선택해주세요")

    if play_again == "y":
        play_game()
    else:
        print("Goodbye!")
        sys.exit()
        

play_game()