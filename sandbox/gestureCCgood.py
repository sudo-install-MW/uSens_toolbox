# code to crop images from img dir and put them in different folders

from os import listdir
import os
import cv2
import numpy as np
import shutil
import ntpath

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#  rootPath = 'C:\\Users\\jiyin\\Desktop\\Coding Taks\\gestureCrop\\' #  The two folders: destination and source must be in same directory or else you can change the code
exportPath = 'Y:\\Data_RGB\\GreenScreen_20180710Selfie_clean\\' #  Where the image files exist and want to be taken out
importPath = 'Y:\\Data_RGB\\GreenScreen_Destination0710\\' #  Where you want to move the image files
dumpPath = 'Y:\\Data_RGB\\GreenScreen_Destination0710\\dump\\'

gestureDict = {
    '0': '0\\',
    '1': '1\\',
    '2': '2\\',
    '3': '3\\',
    '4': '4\\',
    '5': '5\\',
    '6': '6\\',
    '7': '7\\',
    '8': '8\\',
    '9': '9\\',
    '10': '10\\'
}

def fileTraversalWriteToText(folderPathList, pathing, importP):
    """
    :param folderPathList:
    :param pathing:
    :param importP:
    :return:
    """
    files = []
    f = open(importP + "fileList.txt", "w+")
    for folderPath in folderPathList:
        newPath = pathing + '\\' + folderPath
        if os.path.isdir(newPath) == True:
            fileTraversal(listdir(newPath), newPath, importP)
        else:
            if(folderPath[-4:]=='.txt' and 'flip' not in folderPath and '.5' not in folderPath and '.75' not in folderPath and '1.25' not in folderPath and '1.5' not in folderPath):
                f.write(newPath + '\n')
                files.append(newPath + '\n')
                #  print(newPath)
                shutil.copy2(newPath,dumpPath + folderPath)
                imagePath = newPath.replace('.txt', '.png')
                imageNewPath = folderPath.replace('.txt', '.png')
                shutil.copy2(imagePath,dumpPath + imageNewPath)
    f.close()
    return files

def cropImage(arrayOfFiles, pathing, importP):
    """
    :param arrayOfFiles:
    :param pathing:
    :param importP:
    :return:
    """
    for fileText in arrayOfFiles:
        fileText = fileText[:-1]
        fileImage = fileText.replace('.txt', '.png')
        #  print(fileImage[len(exportPath)+1:])
        newPath = fileImage.replace(':\\', '\\')
        newPath = newPath.replace('\\', '-')
        newPath = newPath.replace('/', '-')
        boundingBox = open(fileText, 'r')
        number_line = boundingBox.readline()
        img = cv2.imread(fileImage, 1)
        
        if not img is None:
            imgHeight, imgWidth, imgChannels = img.shape
            gestureLine = 0
            while number_line:
                numberSplit = number_line.split()
                gesture, xcord, ycord, width, height = numberSplit[0], float(numberSplit[1]), float(numberSplit[2]), float(numberSplit[3]), float(numberSplit[4])
                    #  print(gesture)
                if number_line == "":
                    break
                number_line = boundingBox.readline()
                if gesture in gestureDict:
                    #  print(importP + gestureDict[gesture] + newPath)
                    try:
                        y1 = int(ycord*imgHeight)-int(height*imgHeight)//2 - 20
                        y2 = int(ycord*imgHeight)+int(height*imgHeight)//2 + 20
                        x1 = int(xcord*imgWidth)-int(width*imgWidth)//2 -20
                        x2 = int(xcord*imgWidth)+int(width*imgWidth)//2 +20
                        x1 = x1 if x1 >= 0 else 0
                        x2 = x2 if x2 < imgWidth else imgWidth
                        y1 = y1 if y1 >= 0 else 0
                        y2 = y2 if y2 < imgHeight else imgHeight
                        #  print(x1, x2, y1, y2)
                        #  print(x1, x2, y1, y2)
                        cropped = img[y1:y2, x1:x2]
                        resized = cv2.resize(cropped, (160, 160))
                        print(importP + gestureDict[gesture] + str(gestureLine) + '_' + path_leaf(fileImage))
                        cv2.imwrite(importP + gestureDict[gesture] + str(gestureLine) + '_' + path_leaf(fileImage), resized)
                    except TypeError:
                        print("Error")
                        continue
                gestureLine += 1


topFileList = listdir(exportPath)
fileList = fileTraversalWriteToText(topFileList, exportPath, importPath)

#  fileList = open('./Destination/fileList.txt', 'r').readlines()
#  randomFiles = []
#  randomFiles = np.random.choice(fileList, 2)
cropImage(fileList, exportPath, importPath)
