import random
print("")

computer_wins = 0
user_wins = 0

def welcome_message():
    print("Let's play a game of Rock, Paper, Scissors")
welcome_message()
print("")

def user_instructions():
    print("Rules: Rock beats scissors. Paper beats rock. Scissors beats paper.")
    print("To choose, please input one of the following letters. Rock = R, Paper = P, Scissors = S.")
user_instructions()
print("")


user_choice = input("Please Choose: ")
print("")

if user_choice == "R":
    user_choice = 0
    print("You choose: Rock")
elif user_choice == "P":
    user_choice = 1
    print("You choose: Paper")
elif user_choice == "S":
    user_choice = 2
    print("You choose: Scissors")
else:
    user_choice = 4
    print("Wrong input. Please try again")


computer_choice = random.randint(0, 2)

while user_choice in range(0, 3):
    if computer_choice == 0:
        print("Computer choice: Rock")
        break
    elif computer_choice == 1:
        print("Computer choice: Paper")
        break
    elif computer_choice == 2:
        print("Computer choice: Scissors")
        break
else:
    pass

print("")

if user_choice == 0 and computer_choice == 1:
    print("You Lose!")
    computer_wins += 1
elif user_choice == 1 and computer_choice == 2:
    print("You Lose!")
    computer_wins += 1
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
    computer_wins += 1
elif user_choice == computer_choice:
    print("It's a tie!")
elif user_choice + computer_choice >= 3:
    pass
else:
    print("You Win!")
    user_wins += 1

print("")

def score_tally():
    print("Computer wins: ", computer_wins)
    print("Your wins: ", user_wins)
score_tally()


