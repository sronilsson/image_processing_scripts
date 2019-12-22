import cv2
import os
path = r"Z:\DeepLabCut\misc\tensorflow\coco_project_heads\pyimagesearch\source_code\my_weights\output\Mouse_2_clahe"
fileNames = os.listdir(path)
inputPath = path

for i in fileNames:
    #-----Reading the image-----------------------------------------------------
    imgPath = os.path.join(inputPath, i)
    img = imgPath
    img = cv2.imread(img, 1)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    #-----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)

    #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl,a,b))

    #-----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    cv2.imwrite(imgPath, final)
    print(imgPath)
