import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Crop Images into Face only Image
def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces == ():
        return None

    area = 0
    for(x,y,w,h) in faces:
        if area < w*h:
            cropped_face = img[y:y+h, x:x+h]
    
    return cropped_face

# Find Directories, Add to 'names', Sample Faces
import os
import glob
def face_sampler(directory):
    user = os.listdir(directory)
    
    for u in user:
        print("user "+u+" now sampling")
        user_path = directory+"/"+u
        original_photos = glob.glob(os.path.join(user_path, "*.jpg"))
        print("user "+u+" has "+str(len(original_photos))+" photos")
        try:
            if not(os.path.isdir(user_path+"/verified")):
                os.makedirs(os.path.join(user_path+"/verified"))
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("Failed to create directory!!!!!")
                raise

        count = 0
        for op in original_photos:
            print("    image "+op+" check...")
            temp_image = cv2.imread(op, cv2.IMREAD_UNCHANGED)

            if face_extractor(temp_image) is not None:
                print("YES")
                count += 1
                face = cv2.resize(face_extractor(temp_image), (200,200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                verified_path = user_path+"/verified/"+str(count)+".jpg"
                cv2.imwrite(verified_path, face)
            else:
                print("NO")



