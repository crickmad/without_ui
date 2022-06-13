import cv2
import os
import keyboard
def look():
    try:
        recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
        recognizer.read('trainer/trainer.yml')   #load trained model
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach
        #font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type
        id = 2 #number of persons you want to Recognize
        #names = ['hi','avi']  #names, leave first empty bcz counter starts from 0
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
        cam.set(3, 640) # set video FrameWidht
        cam.set(4, 480) # set video FrameHeight
        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)
        flag1 = 0
        flag2 = 0
        pause = 0

        count = True

        while count == True:
            ret, img =cam.read() #read the frames using the above created object
            if not ret:
                print("failed to grab frame")
                break
            converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another
            faces = faceCascade.detectMultiScale( converted_image,scaleFactor = 1.2,minNeighbors = 5,minSize = (int(minW), int(minH)),)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image
                id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image
                pause+=1
                print("verifying........")
                # Check if accuracy is less them 100 ==> "0" is perfect match 
                if (accuracy < 100):
                    #id = "Gowtham"#names[id]
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    print(accuracy)
                    flag1+=1
                    #count = False
                else:
                    #id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    print(accuracy)
                    flag2+=1
                    #count = False
                #cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                #cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
                if pause > 10:
                    count = False
        if flag1 > flag2:
            id = "Gowtham"
            #print("hello "+id+" "+str(flag1))
        elif flag2 > flag1:
            id = "unknown"
            #print("hello "+id+" "+str(flag2))
        else:
            print("wrong match equal")

            #count = False
            #cv2.imshow('camera',img)
            """k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break"""
            """try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    print('You Pressed A Key!')
                    break  # finishing the loop
            except:
                break"""
        # Do a bit of cleanup
        #print("Thanks for using this program, have a good day.")
        cam.release()
        cv2.destroyAllWindows()

        return id
    except:
        os._exit(0)

#if __name__ == "main":
#look()