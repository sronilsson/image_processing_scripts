import subprocess
import os
import cv2
from os import listdir
from os.path import isfile, join


currDir = os.getcwd()
my_dirs = [d for d in os.listdir(currDir) if os.path.isdir(os.path.join(currDir, d))]
frameDirs = [x for x in my_dirs if "merged" in x]

fps = 25
fileformat = '.mp4'
bitrate = '2400'

for dir in frameDirs:
    currentDir = dir
    fileOut = str(currentDir) + str(fileformat)
    currentDirPath = os.path.join(currDir, currentDir)
    currentFileList = [f for f in listdir(currentDirPath) if isfile(join(currentDirPath, f))]
    imgPath = os.path.join(currentDirPath, currentFileList[0])
    img = cv2.imread(imgPath)
    ffmpegFileName = os.path.join(currentDirPath, '%d.png')
    imgShape = img.shape
    height = imgShape[0]
    width = imgShape[1]
    command = str('ffmpeg -r ' + str(fps) + str(' -f image2 -s ') + str(height) + 'x' + str(width) + ' -i ' + str(ffmpegFileName) + ' -vcodec libx264 -b ' + str(bitrate) + 'k ' + str(fileOut))
    print(command)
    subprocess.call(command, shell=True)