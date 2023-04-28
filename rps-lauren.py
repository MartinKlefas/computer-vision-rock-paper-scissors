import cv2
from keras.models import load_model
import numpy as np
import random
import time

def get_computer_choice():
    game_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(game_options)
    return computer_choice

def get_prediction():
    print("m: loading model")
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    choices_list = ['rock', 'paper', 'scissors', 'nothing']
    computer_wins = 0
    user_wins = 0
    round_count = 0
    while computer_wins < 3 and user_wins < 3:
        print("m: round start")
        round_count += 1
        count = 3
        start_time = time.time()
        while True:
            print("m: wait start")
            time_left = time.time() - start_time
            if time_left <= count:
                print(f"{count}...")
                count -= 1
                time.sleep(1)
            else:
                break
            while True:
                print("m: observation start")
                ret, frame = cap.read()
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                prediction = model.predict(data)
                user_choice = choices_list[prediction.argmax()]
                computer_choice = get_computer_choice()
                winner = get_winner(user_choice, computer_choice)
                print(f"You chose {user_choice}. Computer chose {computer_choice}.")
                if winner == "Computer":
                    computer_wins += 1
                    print("Computer wins this round!")
                elif winner == "User":
                    user_wins += 1
                    print("You win this round!")
                elif winner == "Tie":
                    print("This round is a tie.")
                else:
                    print("Invalid input")
                print(f"User score: {user_wins}. Computer score: {computer_wins}.")
                cv2.imshow('frame', frame)
                    # Press q to close the window
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                if computer_wins == 3 or user_wins == 3:
                    break

            if computer_wins == 3:
                print("Computer wins!")
                break
            elif user_wins == 3:
                print("User wins!")
                break

        cap.release()
        cv2.destroyAllWindows()
        return

def get_winner(user_choice, computer_choice):
    if (computer_choice == 'rock' and user_choice == 'scissors') or (computer_choice == "scissors" and user_choice == 'paper') or (computer_choice == 'paper' and user_choice == 'rock'): 
        return "Computer"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == "scissors" and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'): 
        return "User"
    elif user_choice == computer_choice: 
        return "Tie"
    else:
        return "invalid input"

get_prediction()