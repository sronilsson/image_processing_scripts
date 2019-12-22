import cv2
import os
import subprocess
currentDir = os.getcwd()

#extract one frame
videoName = "Z:\DeepLabCut\Videos\CLAHE\LinLab\clip_and_crop\Video_11_clip.avi"
cap = cv2.VideoCapture(videoName)
cap.set(1, 0)
ret, frame = cap.read()
fileName = str(0) + str('.bmp')
filePath = os.path.join(currentDir, fileName)
cv2.imwrite(filePath,frame)

#find ROI
if __name__ == '__main__':
    img = cv2.imread(filePath)
    ROI = cv2.selectROI(img)
    width = abs(ROI[0] - (ROI[2] + ROI[0]))
    height = abs(ROI[2] - (ROI[3] + ROI[2]))
    topLeftX = ROI[0]
    topLeftY = ROI[1]
    cv2.waitKey(0)
cv2.destroyAllWindows()

#crop video with ffmpeg
fileOut, fileType = videoName.split(".", 2)
fileOutName = str(fileOut) + str('_cropped.mp4')
command = str('ffmpeg -i ') + str(videoName) + str(' -vf ') + str('"crop=') + str(width) + ':' + str(height) + ':' + str(topLeftX) + ':' + str(topLeftY) + '" ' + str('-c:v libx264 -c:a copy ') + str(fileOutName)
print(command)
subprocess.call(command, shell=True)
