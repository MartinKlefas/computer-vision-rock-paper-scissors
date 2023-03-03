import cv2
from keras.models import load_model
import numpy as np
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


f = open('labels.txt', 'r')

try:
    lines = f.readlines()
    labels = list()
    for line in lines:
        labels.append(line.split(" ")[1].rstrip('\n'))
    
finally:
    f.close()

def get_prediction():    
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('Game', frame)
                 
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    #print(labels)
   # print(prediction)
    return labels[np.argmax(prediction)]

def play():
    countDown = -200 # initialise this to impossible time
    #start_time = time.time() # this isn't really the start - we have to wait for the webcam to open

    while cap.isOpened():
        ret, frame = cap.read()

        #we now know the webcam is booted and running
        if countDown == -200 : # if it's this low it must be the first time the camera is working
            countDown = 5 # set it back to something sensible
            start_time = time.time() # now we start the timer


        cv2.putText(frame,str(countDown),(round(frame.shape[1] / 2) - 15, round(frame.shape[0] / 2)+10),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255))
        
        cv2.imshow("Game",frame)

        # Press 'q' to exit
        if cv2.waitKey(10) == ord('q'):
            break

        currentTime= time.time()
        if (currentTime - start_time)  > 1.0 : # If a second has elapsed then update countdown            
            countDown -= 1
            start_time = time.time() # we're time since the last updated frame - start time is a misnomer

            if countDown <= 0:
                retval = get_prediction()
                print(retval)


play()
