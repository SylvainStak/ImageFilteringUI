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

#use blurBox.py_func(...) to run with CPU so it turns off the execution with jit
#blurbox
imgBlurBox = Image.fromarray(blurBox(originalImageData, 1))
imgBlurBox.save(targetDirectory+'blurBox.png')
