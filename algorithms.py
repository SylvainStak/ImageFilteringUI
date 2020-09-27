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

# Takes array of 3 elements representing rgb colors
# and transform to decimal
def RGBtoDECIMAL(rgb):
    return int('%02x%02x%02x' % tuple(rgb),16)

# Takes decimal number between 0 and 16777215 representing a color
# and transform to array of 3 elements with r,g and b
def DECIMALtoRGB(decimal):
    return [int(hex(decimal)[2:][i:i+2], 16) for i in (0, 2, 4)]
