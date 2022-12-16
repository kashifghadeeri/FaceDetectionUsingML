#OpenCv is a library used for image processing and computer vision 
#haarcascade is a machine learning approachand it is a cascading function that is used to train the data
#importing opencv as cv2
import cv2

#loading the classifier of face detection
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#detect the face from the video that is being captured by camera
#video capture object
cap=cv2.VideoCapture(0)
while True:
    _,img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    cv2.imshow('img',img)

    k=cv2.waitKey(30) & 0xff #esc
    if k==27:
        break
cap.release()