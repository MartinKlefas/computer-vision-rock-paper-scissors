import random
import cv2
from keras.models import load_model
import numpy as np
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
max_countdown = 5
user_wins = 0
computer_wins  = 0
RoundsPlayed = 0

f = open('labels.txt', 'r')

try:
    lines = f.readlines()
    labels = list()
    for line in lines:
        labels.append(line.split(" ")[1].rstrip('\n'))
    
finally:
    f.close()

def get_prediction(): 
    strPrediction = "Nothing"   
    while strPrediction == "Nothing" :
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('Game', frame)
        strPrediction = labels[np.argmax(prediction)]
            
    print("You Chose: ", strPrediction)
    return strPrediction

def play():
    countDown = -200 # initialise this to impossible time - as we need to wait for the cam as below
     # this isn't really the start - we have to wait for the webcam to open

    while cap.isOpened():
        ret, frame = cap.read()

        #we now know the webcam is booted and running
        if countDown == -200 : # if it's this low it must be the first time the camera is working
            countDown = max_countdown # set it back to something sensible
            start_time = time.time() # now we start the timer


        cv2.putText(frame,str(countDown),(round(frame.shape[1] / 2) - 15, round(frame.shape[0] / 2)+10),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255),3)
        
        cv2.imshow("Game",frame)

        # Press 'q' to exit
        if cv2.waitKey(10) == ord('q'):
            break

        currentTime= time.time()
        if (currentTime - start_time)  > 1.0 : # If a second has elapsed then update countdown            
            countDown -= 1
            start_time = time.time() # we're time since the last updated frame - start time is a misnomer

            if countDown <= 0:
                return get_prediction()
                


def get_computer_choice():
    return random.choice(["Rock","Paper","Scissors"])

def get_winner(computer_choice, user_choice):
    if computer_choice == "Rock":
        if user_choice == "Rock":
            return 0
        elif user_choice == "Paper":
            return 1
        else:
            return -1
        
    elif computer_choice == "Paper":
        if user_choice == "Rock":
            return -1
        elif user_choice == "Paper":
            return 0
        else:
            return 1
    else:
        if user_choice == "Rock":
            return 1
        elif user_choice == "Paper":
            return -1
        else:
            return 0

while user_wins < 3 and computer_wins < 3 and RoundsPlayed < 5:
    result = get_winner(get_computer_choice(),play())
    if result < 0 :
        computer_wins += 1
        print("You lost this round")
    elif result > 0 :
        user_wins +=1
        print("You won this round")
    else:
        print("This round was a tie")

    RoundsPlayed += 1
    print("From %s games, the score is:" % RoundsPlayed)
    print(" user %i : %i Computer" % (user_wins, computer_wins))

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()


if user_wins == 3:
    print("Looks like you dominated this game!")
elif computer_wins == 3:
    print("Wow, you really got your butt handed to you!")
else:
    if user_wins > computer_wins:
        print("Well done, you're the champion")
    elif computer_wins > user_wins:
        print("Unlucky, Loser!")
    else:
        print("seems we're evenly matched!")


