import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return None

    area = 0
    for(x,y,w,h) in faces:
        if area < w*h:
            cropped_face = img[y:y+h, x:x+h]
    
    return cropped_face
