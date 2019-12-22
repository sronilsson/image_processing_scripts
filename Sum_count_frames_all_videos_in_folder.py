import imageio

fname = 'Tvideo_1.mp4'
vid = imageio.get_reader(fname,  'ffmpeg')

########### FIND CSV FILES ###########
for i in os.listdir(os.curdir):
    if i.__contains__("Tvideo_35.mp4"):
        filesFound.append(i)


# number of frames in video
num_frames=vid._meta['nframes']
print(num_frames)