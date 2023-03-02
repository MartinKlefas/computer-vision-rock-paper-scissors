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
                print("Invalid Choice. Please choose from:", choices)
        except:
            print("Invalid Choice. Please choose from:", choices)

    return guess

print(get_computer_choice())