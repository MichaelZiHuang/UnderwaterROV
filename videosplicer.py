import cv2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('videos', nargs='*')
args = parser.parse_args()

render_directories = []

# print(os.environ["VIDEOFOLDER"])

for video in args.videos:
    vidcap = cv2.VideoCapture(video)
    success,image = vidcap.read()
    count = 0
    success = True
    videoname = video.replace(".mp4", "")
    try:
        os.mkdir("./" + videoname)
    except:
        print("folder already exists")
        print("checking if empty...")
        render_directories.append(videoname)
        if len(os.listdir('./' + videoname)) == 0:
            print("directory is empty continuing to parse")
        else:
            print("directory not empty continuing to next video, frames in non-empty directory will be used in agisoft render")
            continue
        print("**************************")
    while success:
        cv2.imwrite("./" + videoname + "/frame%d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        print('Read a new frame: ' + str(count), success)
        count += 1
print("*****************************************")
# print("In Bash Shell Run the command: export VIDEOFOLDER='" + os.getcwd() + "'")
print("In the agisoft console: run the createModel.py script with the arguments:\n--image_folder " + os.getcwd(), end=' ')
for folder in render_directories:
    print(folder, end=' ')
print()
# os.environ["VIDEOFOLDER"] = os.getcwd()
# print(os.environ["VIDEOFOLDER"])
