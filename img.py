from algorithms import *
from PIL import Image
import shutil
import numpy
import os

# setup target directory
targetDirectory='./results/'
shutil.rmtree(targetDirectory, ignore_errors=True)
os.mkdir(targetDirectory)

# retrieve original image
originalImage=Image.open('gadsden.jpg')
originalImageData=numpy.array(originalImage)

#grayscale
#imgGrayscale = Image.fromarray(grayscale(originalImageData))
#imgGrayscale.save(targetDirectory+'grayscale.png')

#blurbox
for i in range(1,30,2):
    imgBlurBox = Image.fromarray(blurBox(originalImageData, i))
    imgBlurBox.save(targetDirectory+'blurBox_'+str(i)+'.png')
