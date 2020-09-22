import pyzbar.pyzbar as pyzbar
import cv2

def qr_decoder(img):
    gray = gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    decoded = pyzbar.decode(gray)
    print(decoded)

    if len(decoded) == 0:
        return None
    
    data = []
    for d in decoded:
        data.append(d.data.decode('utf-8'))
    return data

test_img = cv2.imread('img/test16.png')
test_img_reverse = cv2.bitwise_not(test_img)

print(qr_decoder(test_img))