import os
import subprocess

filesFound = []

def execute(command):
    print(command)
    subprocess.call(command, shell=True, stdout = subprocess.PIPE)

########### FIND FILES ###########
for i in os.listdir(os.curdir):
    if i.__contains__(".mp4"):
        filesFound.append(i)

########### DEFINE COMMAND ###########
for i in filesFound:
    currentFile = i
    outFile = currentFile.replace('.mp4', '')
    outFile = str(outFile) + '_downsampled.mp4'
    command = (str('ffmpeg -i ') + str(currentFile) + ' -vf scale=1228:1026 ' + outFile + ' -hide_banner')
    execute(command)


