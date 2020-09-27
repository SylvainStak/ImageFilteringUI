# Takes array of 3 elements representing rgb colors
# and transform to decimal
def RGBtoDECIMAL(rgb):
    return int('%02x%02x%02x' % tuple(rgb),16)

# Takes decimal number between 0 and 16777215 representing a color
# and transform to array of 3 elements with r,g and b
def DECIMALtoRGB(decimal):
    return [int(hex(decimal)[2:][i:i+2], 16) for i in (0, 2, 4)]

# Takes 3D array representing a 2D image and its RGB colors
# and apply grayscale filter on it
def grayscale(img):
    filtered=img
    for h in range(len(img)):
        for w in range(len(img[h])):
            red=img[h][w][0]
            green=img[h][w][1]
            blue=img[h][w][2]

            newColor=(int(red)+int(green)+int(blue))/3

            filtered[h][w]=[newColor]*3

    return filtered

# Takes 3D array representing a 2D image and its RGB colors
# and apply box blur filter on it (this version is actually 
# psycholdelic, try on ur own images and you will see)
def blurBox(img):
    filtered=img
    for h in range(3,len(img)-3):
        for w in range(3,len(img[h])-3):
            tR=tG=tB=0
            for x in range(-3,3+1):
                for y in range(-3,3+1):
                    kernelCell=img[x+h,y+w]
                    tR+=kernelCell[0]
                    tG+=kernelCell[1]
                    tB+=kernelCell[2]
            filtered[h,w]=[tR/9,tG/9,tB/9]
    return filtered
