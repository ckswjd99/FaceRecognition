# pip install qrcode pillow matplotlib
import qrcode, numpy, random
import matplotlib.pylab as plt

def qr_gen(text):
    img = qrcode.make(text)
    print(img.size)
    return img

def qr_encrypt(img, enc):
    new_img = img.convert('RGB')
    
    for i in range(new_img.size[0]):
        for j in range(new_img.size[1]):
            r, g, b = new_img.getpixel((i, j))
            if enc == "RED":    # RED will be key color
                if (r, g, b) == (0, 0, 0):
                    new_img.putpixel((i,j), (255, 0, 0))
                else:
                    ran_g = random.randint(0,255)
                    ran_b = random.randint(0,255)
                    new_img.putpixel((i,j), (0, ran_g, ran_b))
            elif enc == "RED_SHUFFLE":    # RED will be key color
                ran_g = random.randint(0,255)
                ran_b = random.randint(0,255)
                if (r, g, b) == (0, 0, 0):
                    new_img.putpixel((i,j), (255, ran_g, ran_b))
                else:
                    
                    new_img.putpixel((i,j), (0, ran_g, ran_b))


    plt.imshow(new_img)
    plt.show()

    new_img.save("result.png")

    return new_img


