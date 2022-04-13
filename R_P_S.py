import random

option = ["Rock", "Paper", "scissor"]

user_choice = 0
user_score = 0
computer_choice = 0
computer_score = 0

# barresi halat motefavet va emtiazdehi
for i in range(5):
    print("Enter one of these options:\n1.Rock\n2.Paper\n3.scissor")
    user_choice = input()
    computer_choice = random.choice(option)
    if user_choice == "1":
        if computer_choice == "Rock":
            pass
        elif computer_choice == "Paper":
            computer_score += 1
        elif computer_choice == "scissor":
            user_score += 1

    elif user_choice == "2":
        if computer_choice == "Rock":
            user_score += 1
        elif computer_choice == "Paper":
            pass
        elif computer_choice == "scissor":
            computer_score += 1

    elif user_choice == "3":
        if computer_choice == "Rock":
            computer_score += 1
        elif computer_choice == "Paper":
            user_score += 1
        elif computer_choice == "scissor":
            pass
    else:
        print("out of the range")

#shart bord
if computer_score > user_score:
    print("Computer score is:", computer_score,
          "\nYour score is:", user_score, "\nComputer win!")
elif user_score > computer_score:
    print("Computer score is:", computer_score,
          "\nYour score is:", user_score, "\nYou win!")
elif user_score == computer_score:
    print("The score:", user_score, "Your score is equal.")
