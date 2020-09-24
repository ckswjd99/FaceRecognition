#pip install pyzbar opencv-python
import copy
import pyzbar.pyzbar as pyzbar
import matplotlib.pylab as plt
from PIL import Image
import PIL.ImageOps

def qr_reader(img):
    gray = img.convert('LA')
    plt.imshow(gray)
    gray.save("decoding.png")
    decoded = pyzbar.decode(gray)
    print(decoded)

    if len(decoded) == 0:
        return None
    
    data = []
    for d in decoded:
        data.append(d.data.decode('utf-8'))
    return data

def qr_decoder(img, enc):
    new_img = copy.deepcopy(img)
    if enc == "":
        pass
    elif enc == "RED_SHUFFLE" or enc == "RED_BSHUFFLE":
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = new_img.getpixel((i, j))
                new_img.putpixel((i,j), (r, r, r))
        new_img = PIL.ImageOps.invert(new_img)
    elif enc == "GREEN_SHUFFLE" or enc == "GREEN_BSHUFFLE":
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = new_img.getpixel((i, j))
                new_img.putpixel((i,j), (g, g, g))
        new_img = PIL.ImageOps.invert(new_img)
        pass
    elif enc == "BLUE_SHUFFLE" or enc == "BLUE_BSHUFFLE":
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = new_img.getpixel((i, j))
                new_img.putpixel((i,j), (b, b, b))
        new_img = PIL.ImageOps.invert(new_img)
        pass

    new_img.save("decoding.png")
    return new_img


test_img = Image.open('result.png')
test_img_reverse = PIL.ImageOps.invert(test_img)

#qr_reader(qr_decoder(test_img, "RED_BSHUFFLE"))