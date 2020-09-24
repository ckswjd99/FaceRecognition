# pip install qrcode pillow matplotlib
import qrcode, numpy, random
import matplotlib.pylab as plt

def qr_gen(text):
    img = qrcode.make(text)
    img.save("original.png")
    return img

def qr_encrypt(img, enc):
    new_img = img.convert('RGB')

    if enc == "RED":
        for i in range(new_img.size[0]):
            for j in range(new_img.size[1]):
                r, g, b = new_img.getpixel((i, j))
                if (r, g, b) == (0, 0, 0):
                    new_img.putpixel((i,j), (255, 0, 0))
    elif enc == "RED_SHUFFLE":
        for i in range(new_img.size[0]):
            for j in range(new_img.size[1]):
                r, g, b = new_img.getpixel((i, j))
                ran_g = random.randint(0,255)
                ran_b = random.randint(0,255)
                if (r, g, b) == (0, 0, 0):
                    new_img.putpixel((i,j), (255, ran_g, ran_b))
                else:
                    ran_g = random.randint(0,255)
                    ran_b = random.randint(0,255)
                    new_img.putpixel((i,j), (0, ran_g, ran_b))
    elif enc == "RED_BSHUFFLE":
        for i in range(round(new_img.size[0]/10)):
            for j in range(round(new_img.size[1]/10)):
                r, g, b = new_img.getpixel((i*10, j*10))
                ran_g = random.randint(0,255)
                ran_b = random.randint(0,255)
                if (r, g, b) == (0, 0, 0):
                    for k in range(100):
                        new_img.putpixel((i*10+int(k/10),j*10+k%10), (255, ran_g, ran_b))
                else:
                    for k in range(100):
                        new_img.putpixel((i*10+int(k/10),j*10+k%10), (0, int(ran_g), int(ran_b)))
    elif enc == "GREEN_BSHUFFLE":
        for i in range(round(new_img.size[0]/10)):
            for j in range(round(new_img.size[1]/10)):
                r, g, b = new_img.getpixel((i*10, j*10))
                ran_r = random.randint(0,255)
                ran_b = random.randint(0,255)
                if (r, g, b) == (0, 0, 0):
                    for k in range(100):
                        new_img.putpixel((i*10+int(k/10),j*10+k%10), (ran_r, 255, ran_b))
                else:
                    for k in range(100):
                        new_img.putpixel((i*10+int(k/10),j*10+k%10), (int(ran_r), 0, int(ran_b)))
    elif enc == "BLUE_BSHUFFLE":
        for i in range(round(new_img.size[0]/10)):
            for j in range(round(new_img.size[1]/10)):
                r, g, b = new_img.getpixel((i*10, j*10))
                ran_r = random.randint(0,255)
                ran_g = random.randint(0,255)
                if (r, g, b) == (0, 0, 0):
                    for k in range(100):
                        new_img.putpixel((i*10+int(k/10),j*10+k%10), (ran_r, ran_g, 255))
                else:
                    for k in range(100):
                        new_img.putpixel((i*10+int(k/10),j*10+k%10), (int(ran_r), int(ran_g), 0))


    plt.imshow(new_img)
    plt.show()

    new_img.save("result.png")

    return new_img

qr = qr_gen("hello")
