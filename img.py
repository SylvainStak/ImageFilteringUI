from PIL import Image
import numpy

image = Image.open('gadsden.jpg')
r=c=numpy.array(image)

for i in range(len(r)):
    for j in range(len(r[i])):
        actualPixel=c[i][j]
        red=actualPixel[0]
        green=actualPixel[1]
        blue=actualPixel[2]

        newColor=(int(red)+int(green)+int(blue))/3
        c[i][j]=[newColor,newColor,newColor]

imageCopy = Image.fromarray(c)
imageCopy.show()

def grayscaleAverage(img):
    c=img