import os
import pandas as pd
import subprocess

videosInDir = r"Z:\DeepLabCut\misc\CRIM13\mp4\mp4_top_videos_cropped"
videoInfoDf = pd.read_csv(r"Z:\DeepLabCut\misc\CRIM13\mp4\video_information.csv", index_col=False)
videoList = []
outputDir = r"Z:\DeepLabCut\misc\CRIM13\mp4\mp4_top_videos_cropped_clipped"
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

for i in os.listdir(videosInDir):
    if i.__contains__(".mp4"):
        file = os.path.join(videosInDir, i)
        videoList.append(file)

for currentVideoFilePath in videoList:
    curVideoFileNamePath = os.path.basename(currentVideoFilePath)
    curVideoFileName = curVideoFileNamePath.replace('.mp4', '')
    outputFileName = os.path.join(outputDir, curVideoFileNamePath)
    currentVidInf = videoInfoDf.loc[videoInfoDf['Video_name'] == curVideoFileName].astype('str')
    currVidEndTime = str(currentVidInf['Clip end (s)'])
    currVidEndTime = str((currVidEndTime.split('nName:', 2)))
    currVidEndTimeMinute = (currVidEndTime.split(':'))[0]
    currVidEndTimeMinute = (currVidEndTimeMinute.split('    '))[1]
    currVidEndTimeSec = (currVidEndTime.split(':'))[1]
    currVidEndTimeSec = (currVidEndTimeSec.split('\\'))[0]

    currVidStartTime = str(currentVidInf['Clip beginning (s)'])
    currVidStartTime = str((currVidStartTime.split('nName:', 2)))
    currVidStartTimeMinute = (currVidStartTime.split(':'))[0]
    currVidStartTimeMinute = (currVidStartTimeMinute.split('    '))[1]
    currVidStartTimeSec = (currVidStartTime.split(':'))[1]
    currVidStartTimeSec = (currVidStartTimeSec.split('\\'))[0]

    if len(currVidEndTimeMinute) < 2:
        currVidEndTimeMinute = '0' + currVidEndTimeMinute
    if len(currVidStartTimeMinute) < 2:
        currVidStartTimeMinute = '0' + currVidStartTimeMinute

    ffmpegCmd = 'ffmpeg -y -i ' + currentVideoFilePath + ' -ss 00:' + currVidStartTimeMinute + ':' + currVidStartTimeSec + ' -to 00:' + currVidEndTimeMinute + ':' + currVidEndTimeSec +' -async 1 ' + str(outputFileName)
    print(ffmpegCmd)
    subprocess.call(ffmpegCmd, shell=True)






