from numba import jit

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
# and apply box blur filter on it
# kA --> kernelAmplitude
# 1 --> -1 0 1
# 3 --> -3 -2 -1 0 1 2 3
# 5 --> -5 -4 -3 -2 -1 0 1 2 3 4 5
# and so on...
@jit(nopython=True)
def blurBox(img, kA):
    filtered=img
    for h in range(kA,len(img)-kA):
        for w in range(kA,len(img[h])-kA):
            tR=tG=tB=0
            for x in range(kA*-1,kA+1):
                for y in range(kA*-1,kA+1):
                    kernelCell=img[x+h,y+w]
                    tR+=kernelCell[0]
                    tG+=kernelCell[1]
                    tB+=kernelCell[2]
            filtered[h,w]=[tR/(((kA*2)+1)**2),tG/(((kA*2)+1)**2),tB/(((kA*2)+1)**2)]
    return filtered
