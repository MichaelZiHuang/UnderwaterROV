import Metashape
import os
import argparse
import datetime

currentDate = datetime.datetime.now()
currentDate = currentDate.strftime("%m-%d-%Y %H-%M-%S")
print(currentDate)

# print(os.environ["VIDEOFOLDER"])
# print(os.getcwd())

parser = argparse.ArgumentParser()
parser.add_argument('--image_folder', '-I', help='Enter path to image directory')
parser.add_argument('folders', nargs='*')
args = parser.parse_args()


os.chdir(args.image_folder)
print(os.getcwd())

doc = Metashape.app.document
for folder in args.folders:
    # doc.open("test1.psx")
    chunk = doc.addChunk()
    myphotos = os.listdir(path='./' + folder)
    myphotos = [('./' + folder + '/' + str(x)) for x in myphotos]
    # print(myphotos)
    chunk.addPhotos(myphotos)
    # chunk.matchPhotos('LowestAccuracy', generic_preselection=True, reference_preselection=False)
    # chunk.matchPhotos(accuracy=PhotoScan.HighAccuracy, generic_preselection=True, reference_preselection=False)
    chunk.matchPhotos()
    chunk.alignCameras()
    # chunk.alignCameras('LowestQuality', filter=Metashape.AggressiveFiltering)
    # chunk.buildDepthMaps(quality=PhotoScan.MediumQuality, filter=PhotoScan.AggressiveFiltering)
    chunk.buildDenseCsloud()
doc.save(currentDate)
