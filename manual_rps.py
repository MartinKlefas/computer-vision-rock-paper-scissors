import random
choices = ["Rock","Paper","Scissors"]
def get_computer_choice():
    cGuess = random.choice(["Rock","Paper","Scissors"])
    return cGuess

def get_user_choice():
    while True:
        guess = input("Please choose your play: ").lower()

        try:
            if guess in ["rock","paper","scissors"]:  
                break
            else:
                print("Invalid Choice. Please choose from:", choices)
        except:
            print("Invalid Choice. Please choose from:", choices)

    return guess

def get_winner(computer_choice, user_choice):
    if computer_choice == "Rock":
        if user_choice == "rock":
            return "draw"
        elif user_choice == "paper":
            return "win"
        else:
            return "lose"
        
    elif computer_choice == "Paper":
        if user_choice == "rock":
            return "lose"
        elif user_choice == "paper":
            return "draw"
        else:
            return "win"
    else:
        if user_choice == "rock":
            return "win"
        elif user_choice == "paper":
            return "lose"
        else:
            return "draw"
        
def print_result(result):
    if result == "win":
        print("You lost")
    elif result == "lose":
        print("You won!")
    else:
        print("It is a tie!")

game_result = get_winner(get_computer_choice(),get_user_choice())

print_result(game_result)