import cv2
import os

cam = cv2.VideoCapture(0)

Classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

face_id = input('Enter User Id: ')

print("face is Being Captured. Look at the camera, your face will be added to the database.")
count = 0

while(True):
 ret,img = cam.read()
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 faces = Classifier.detectMultiScale(gray, 1.3, 5)
 
 for (x,y,w,h) in faces:
  cv2.rectangle(img, (x,y), (x+w,y+h), (250,0,0), 2)
  count += 1
  
  cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
  cv2.imshow('image', img)
 k = cv2.waitKey(100) & 0xff
 if k == 27:
   break
 elif count >= 30:
   break
 
cam.release()
cv2.destroyAllWindows()
