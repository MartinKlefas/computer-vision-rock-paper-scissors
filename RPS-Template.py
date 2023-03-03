import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

f = open('labels.txt', 'r')

try:
    lines = f.readlines()
    labels = list()
    for line in lines:
        labels.append(line.split(" ")[1].rstrip('\n'))
    print("labels are: ", labels)

finally:
    f.close()


while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data,verbose= 0)
    
    # Press q to close the window
    #print(prediction)
    strPrediction = labels[np.argmax(prediction)]
    
    cv2.putText(frame,strPrediction,(10, 50),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255),4)

    cv2.imshow('frame', frame)
    #print("prediction:", strPrediction )
    

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
