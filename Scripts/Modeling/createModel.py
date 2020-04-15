import Metashape
import os
import argparse
import datetime

#this gets the current time and date and will be used to create the save file for when the user runs this script
currentDate = datetime.datetime.now()
currentDate = currentDate.strftime("%m-%d-%Y %H-%M-%S")

#this gets the paths to the directories of frames that were created in the video splicer script
#these are needed in order to import into agisoft
parser = argparse.ArgumentParser()
parser.add_argument('--image_folder', '-I', help='Enter path to image directory')
parser.add_argument('folders', nargs='*')
args = parser.parse_args()


os.chdir(args.image_folder)
# print(os.getcwd())

#for each folder of images, it will add a new chunk to the agisoft project
#match the photos
#align the cameras
#and build the buildDenseCsloud
doc = Metashape.app.document
for folder in args.folders:
    chunk = doc.addChunk()
    myphotos = os.listdir(path='./' + folder)
    myphotos = [('./' + folder + '/' + str(x)) for x in myphotos]
    chunk.addPhotos(myphotos)
    chunk.matchPhotos()
    chunk.alignCameras()
    chunk.buildDenseCloud()
doc.save(currentDate)
