import random

options = ["✋", "🤚"]
user_choice = 0
user_score = 0
computer1_choice = 0
computer1_score = 0
computer2_choice = 0
computer2_score = 0

#barresi halat mokhtalef va emtiazdehi
for i in range(0,5):
    print("Enter your choice:\n1.🤚\n2.✋")
    user_choice = input()
    computer1_choice = random.choice(options)
    computer2_choice = random.choice(options)

    if user_choice == "2":
        if computer1_choice == "✋":
            if computer2_choice == "✋":
                print("c1:", computer1_choice, "\nc2:",
                      computer2_choice, "\nyou: ✋")
                pass
                
            elif computer2_choice == "🤚":
                print("c1:", computer1_choice, "\nc2:",
                      computer2_choice, "\nyou: ✋")
                computer2_score +=1

        elif computer1_choice == "🤚":
            if computer2_choice == "✋":
                print("c1:", computer1_choice, "\nc2:",
                      computer2_choice, "\nyou: ✋")
                computer1_score += 1
            elif computer2_choice == "🤚":
                print("c1:", computer1_choice, "\nc2:",
                      computer2_choice, "\nyou: ✋")
                user_score += 1

    elif user_choice == "1":
        if computer1_choice == "✋":
            if computer2_choice == "✋":
                print("c1:", computer1_choice, "\nc2:",
                      computer2_choice, "\nyou: 🤚")
                user_score +=1
            elif computer2_choice == "🤚":
                print("c1:", computer1_choice, "\nc2:",
                      computer2_choice, "\nyou: 🤚")
                computer1_score +=1

        elif computer1_choice == "🤚":
            if computer2_choice == "✋":
                print("c1:", computer1_choice, "\nc2:",
                      computer2_choice, "\nyou: 🤚")
                computer2_score +=1
            elif computer2_choice == "🤚":
                print("c1:", computer1_choice, "\nc2:",
                      computer2_choice, "\nyou: 🤚")
                pass
                

#shart bord
if computer1_score > computer2_score & user_score:
    print("c1 score:", computer1_score, "\nc2 score:",
          computer2_score, "\nyour score:", user_score)
    print("Computer1 is the winner!")

elif computer2_score > computer1_score & user_score:
    print("c1 score:", computer1_score, "\nc2 score:",
          computer2_score, "\nyour score:", user_score)
    print("Computer2 is the winner!")

elif user_score > computer1_score & computer2_score:
    print("c1 score:", computer1_score, "\nc2 score:",
          computer2_score, "\nyour score:", user_score)
    print("You're the winner!")
