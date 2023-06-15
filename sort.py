import sys
import os
import re
import datetime
import shutil
from PIL import Image
from PIL.ExifTags import TAGS

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print("Provide a folder path to traverse.")
        quit()

    path = sys.argv[1]
    if not os.path.exists(path):
        print("Path provided is not valid")
        quit()
    
    for subdir, dirs, files in os.walk(path):
        print(subdir)
        for dir in dirs:
            match = re.search(r'[0-9]*CANON', dir)
            if match:
                canonDir = os.path.join(path, dir)
                for canonFolder, canonSubFolders, imageFiles in os.walk(canonDir):
                    print(canonFolder)
                    #print(canonSubFolders)
                    for image in imageFiles:
                        imagePath = os.path.join(canonFolder, image)
                        imageDt = datetime.datetime.fromtimestamp(os.path.getctime(imagePath))

                        img = Image.open(imagePath)
                        exifdata = img.getexif()
                        dateShot = exifdata[306]
                        img.close()

                        dateTimeParts = dateShot.split()
                        dateParts = dateTimeParts[0].split(":")
                        year = dateParts[0]
                        month = dateParts[1]
                        day = dateParts[2]

                        dtFolder = os.path.join(subdir, f"{year}-{month}-{day}")

                        if not os.path.exists(dtFolder):
                            print(f"To create: {dtFolder}")
                            os.mkdir(dtFolder)

                        newImagePath = os.path.join(dtFolder, image)
                        shutil.move(imagePath, newImagePath)
                        
                        print(f"moved {imagePath} to {newImagePath}")
                    
                    os.rmdir(canonFolder)
                    

                        
                    
