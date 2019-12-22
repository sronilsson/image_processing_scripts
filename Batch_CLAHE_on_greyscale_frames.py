import cv2 as cv
import numpy as np
import os
import natsort
loop = 0
currentDir = os.getcwd()

filesFound = []

########### FIND CSV FILES ###########
for i in os.listdir(os.curdir):
    if i.__contains__(".png"):
        filesFound.append(i)
filesFound = natsort.natsorted(filesFound)

for i in filesFound:
    currentImage = i
    img = cv.imread(currentImage,0)
    clahe = cv.createCLAHE(clipLimit=2, tileGridSize=(16,16))
    cl1 = clahe.apply(img)
    v = str(loop) + str('.png')
    saveFolderName = 'CLL'
    saveFolderPath = os.path.join(currentDir, saveFolderName)
    if not os.path.exists(saveFolderPath):
        os.makedirs(saveFolderPath)
    saveFileName = os.path.join(saveFolderPath, currentImage)
    cv.imwrite(saveFileName,cl1)
	print(str(currentImage) + str(' saved))
