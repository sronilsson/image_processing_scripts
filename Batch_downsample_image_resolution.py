#!/usr/bin/python
from PIL import Image
import os, sys

path = r"Z:\DeepLabCut\misc\more"
dirs = os.listdir( path )
print(dirs)
loop = 0

for i in dirs:
    print(i)
    impath = os.path.join(path, i)
    im = Image.open(impath)
    print(im)
    imResize = im.resize((300,600), Image.ANTIALIAS)
    savePath = os.path.join(path, str(loop) + '.png')
    imResize.save(savePath, 'PNG', quality=90)
    loop += 1