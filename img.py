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
originalImage=Image.open('test.jpg')
originalImageData=numpy.array(originalImage)

#grayscale
#imgGrayscale = Image.fromarray(grayscale(originalImageData))
#imgGrayscale.save(targetDirectory+'grayscale.png')

#blurbox
imgBlurBox = Image.fromarray(blurBox(originalImageData))
imgBlurBox.save(targetDirectory+'blurBox.png')