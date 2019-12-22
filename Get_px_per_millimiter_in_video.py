from configparser import ConfigParser
import os
import cv2
import numpy as np

config = ConfigParser()
configFile = r"Y:\DeepLabCut\DLC_extract\New_062719\project_folder\project_config.ini"
config.read(configFile)
frames_dir_in = config.get('Frame settings', 'frames_dir_in')
frames_dir_in = [f.path for f in os.scandir(frames_dir_in) if f.is_dir()][0]
imgPath = os.path.join(frames_dir_in, '0.png')
img = cv2.imread(imgPath)
ix,iy = -1,-1
cordList = []

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),12,(0,0,255),-1)
        cordList.append(x)
        cordList.append(y)
        if len(cordList) == 4:
            cv2.line(img, (cordList[0], cordList[1]), (cordList[2], cordList[3]), (0, 0, 255), 4)

cv2.namedWindow('Select coordinates: double left mouse click at two locations. Press ESC when done', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('Select coordinates: double left mouse click at two locations. Press ESC when done',draw_circle)

while(1):
    cv2.imshow('Select coordinates: double left mouse click at two locations. Press ESC when done',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
euclidPixelDist = np.sqrt((cordList[0] - cordList[2]) ** 2 + (cordList[1] - cordList[3]) ** 2)
mm_dist = int(input("Input in mm? "))
ppm = euclidPixelDist / mm_dist
print(ppm)