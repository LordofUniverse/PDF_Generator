from email.mime import image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import numpy as np
import os

width = 800
height = 800

img = Image.new('RGBA', (height, width), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)

# font - Opensans
fonts_path = os.path.join(os.path.dirname(__file__), 'fonts')
font = ImageFont.truetype(os.path.join(fonts_path, 'OpenSans-VariableFont_wdth,wght.ttf'), 24)

# paste text in coordinate x and y
def pasteText(x, y, text):
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((x, y), text, (0, 0, 0), font=font)

# paste image in coordinate x and y
def pasteImage(x, y, imageurl):
    if type(imageurl) == Image.Image:
        Image.Image.paste(img, imageurl, (x, y))
    else:
        Image.Image.paste(img, Image.open("images/" + imageurl), (x, y))

#resize image to size of height h and w
def resiz(imageurl, h, w):
    if type(imageurl) == Image.Image:
        return imageurl.resize((h, w))
    else:
        return Image.open("images/" + imageurl).resize((h, w))

# Put white bg to wherever is transparent
def whiteBG(url):
    im = Image.open('images/' + url)
    arr = np.array(im)
    height = arr.shape[0]
    width = arr.shape[1]

    for i in range(height):
        for j in range(width):
            if arr[i][j][3] == 0:
                arr[i][j] = [255, 255, 255, 255]
            else:
                arr[i][j] = [255, 255, 255, 0]
    returnimg = Image.fromarray(arr)
    
    return returnimg

pasteText(330, 80, "Welcome to IITB")
# pasteImage(100, 100, "logo.png")
pasteImage(80, 30, resiz(whiteBG("logo.png"), 50, 50))
pasteImage(380, 30, resiz(whiteBG("DC_logo.png"), 80, 60))
pasteImage(80, 150, resiz("guestimg.png", 150, 150))
pasteText(250, 160, "Guest Name: ")
pasteText(250, 200, "Aadhar num: ")

img.save('guestEntry.png')