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
grayscale_average = Image.fromarray(grayscale(originalImageData))
grayscale_average.save(targetDirectory+'grayscale.png')
