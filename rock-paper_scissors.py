import random

counter = 0


pos_act = ["rock", "paper", "scissors"]


while True:
   
    user_act = input("please enter then action: ")
    
    computer_act = random.choice(pos_act)

    print(f"your choise {user_act}  \ncomputer choise {computer_act}")

    if user_act == computer_act:
        print(f"Both players selected {user_act}. It's a tie!")
        counter += 1
    elif user_act == "rock":
        counter += 1

        if computer_act == "scissors":
            print("Rock smashes scissors! You win!")
            # counter += 1
        else:
            print("Paper covers rock! You lose.")
            # counter += 1

    elif user_act == "paper":
        counter += 1
        if computer_act == "rock":
            print("Paper covers rock! You win!")
            # counter += 1

        else:
            print("Scissors cuts paper! You lose.")

    elif user_act == "scissors":
        counter +=1

        if computer_act == "paper":
            print("Scissors cuts paper! You win!")
            # counter += 1
        else:
            print("Rock smashes scissors! You lose.")

    if counter == 3: 
        break
