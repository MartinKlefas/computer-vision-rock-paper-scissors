import random

choices = ["Rock","Paper","Scissors"]

def get_computer_choice():
    cGuess = random.choice(choices)
    return cGuess

def get_user_choice():
    while True:
        guess = input("Please choose your play: ")

        try:
            if guess in choices:  
                break
            else:
                print("Invalid Choice. Please choose from:", choices)
        except:
            print("Invalid Choice. Please choose from:", choices)

    return guess

print(get_computer_choice())