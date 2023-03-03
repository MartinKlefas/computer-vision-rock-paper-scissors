import random

def get_computer_choice():
    cGuess = random.choice(["Rock","Paper","Scissors"])
    return cGuess

def get_user_choice():
    while True:
        guess = input("Please choose your play: ")

        try:
            if guess in ["Rock","Paper","Scissors"]:  
                break
            else:
                print("Invalid Choice. Please choose from:", ["Rock","Paper","Scissors"])
        except:
            print("Invalid Choice. Please choose from:", ["Rock","Paper","Scissors"])

    return guess

def get_winner(computer_choice, user_choice):
    if computer_choice == "Rock":
        if user_choice == "Rock":
            print("It is a tie!")
        elif user_choice == "Paper":
            print("You won!")
        else:
            print("You lost")
        
    elif computer_choice == "Paper":
        if user_choice == "Rock":
            print("You lost")
        elif user_choice == "Paper":
            print("It is a tie!")
        else:
            print("You won!")
    else:
        if user_choice == "Rock":
            print("You won!")
        elif user_choice == "Paper":
            print("You lost")
        else:
            print("It is a tie!")
        

get_winner(get_computer_choice(),get_user_choice())

