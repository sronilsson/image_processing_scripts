import cv2
import os
import numpy as np
import subprocess

filesFound = []

########### FIND MP4 FILES ###########
for i in os.listdir(os.curdir):
    if i.__contains__(".mp4"):
        filesFound.append(i)
		
for m in filesFound:
	currentFile = m
	currFPathName = m.split('.')
	command = 'ffmpeg -i ' + str(currentFile) + ' ' + '-vf extractplanes=y ' + ' ' + str(currFPathName[0]) + '_BW.mp4'
	subprocess.call(command, shell=True)