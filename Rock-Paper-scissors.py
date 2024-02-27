#Rock-Paper-scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def get_user_choice():
    while True:
        user_choice = input("가위(1), 바위(2), 보(3) 중 하나를 선택하세요: ")
        if user_choice in ['1','2','3']:
            return int(user_choice)
        else:
            print("올바른 입력이 아닙니다. 1,2,3 중 하나를 선택해주세요.")

def get_computer_choice():
    return random.randint(1,3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "무승부"
    elif (user_choice ==1 and computer_choice ==3) or\
         (user_choice ==2 and computer_choice == 1)or\
         (user_choice==3 and computer_choice ==2):
        return "User Win!"
    else:
        return "You Lose"
    
def main():
    print("Starts Rock-Paper-Scioors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        user_img = ""
        computer_img = ""

        if user_choice ==1:
            user_img = scissors
        elif user_choice ==2:
            user_img = rock
        else:
            user_img = paper

        if computer_choice ==1:
            computer_img = scissors
        elif computer_choice ==2:
            computer_img = rock
        else:
            computer_img = paper

        print("사용자:")
        print(user_img)
        print("컴퓨터:")
        print(computer_img)
        
        result = determine_winner(user_choice, computer_choice)
        print("결과:", result)

        play_again = input("계속 하시겠습니까? (yes/no): ").lower()
        if play_again != "yes":
            print("게임종료")
            break
if __name__ == "__main__":
    main()
    