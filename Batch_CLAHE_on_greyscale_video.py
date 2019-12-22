import cv2
import os
import numpy as np

filesFound = []

########### FIND MP4 FILES ###########
for i in os.listdir(os.curdir):
    if i.__contains__(".mp4"):
        filesFound.append(i)

for i in filesFound:
    currentVideo = i
    fileName, fileEnding = currentVideo.split('.', 2)
    saveName = str('CLAHE_') + str(fileName) + str('.avi')
    cap = cv2.VideoCapture(currentVideo)
    imageWidth = int(cap.get(3))
    imageHeight = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(saveName, fourcc, fps, (imageWidth, imageHeight), 0)
    while True:
        ret, image = cap.read()
        if ret == True:
            im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            claheFilter = cv2.createCLAHE(clipLimit=2, tileGridSize=(16, 16))
            claheCorrecttedFrame = claheFilter.apply(im)
            out.write(claheCorrecttedFrame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        else:
            print(str('Completed video ') + str(saveName))
            break

cap.release()
out.release()
cv2.destroyAllWindows()
