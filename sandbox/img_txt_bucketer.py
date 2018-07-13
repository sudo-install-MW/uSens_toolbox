# Sort the image and annotation in a file to corresponding directory
# img_anno(.jpg and .txt), img(.jpg) and txt(.txt)

# HOW TO USE THIS SCRIPT : keep the script where you have all the dumped files for
# which you want to sort the img and txt to the corresponding directory bucket

# Import statements
import os
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

#get the root working directory
root_wd = '/media/usens/My Passport/dataset/RGBHT0630/10_heart'

print("\ncurrent working directory is :", root_wd)
root_files = os.listdir(root_wd)

# create the folder for image and text transfer
if 'img_anno' not in root_files:
    os.mkdir(root_wd + '/img_anno')
if 'img' not in root_files:
    os.mkdir(root_wd + '/img')
if 'txt' not in root_files:
    os.mkdir(root_wd + '/txt')


txt_dict = dict()
img_list = []
jpg_list = []

# create a dictionary txt_dict for all txt files in the root directory
start_time = datetime.now()
for elements in root_files:
    if '.txt' in elements:
        txt_dict[elements[:len(elements) - 4]] = elements
    elif '.jpg' in elements:
        jpg_list.append(elements[:len(elements)-4])

#print(txt_dict)

for images in jpg_list:
    # check if corrensponding entry is in txt_dict
    if images in txt_dict:
        print("found image {} with associated txt".format(images))
        
        os.rename( root_wd + "/" + images + ".jpg", root_wd + "/img_anno/" + images + ".jpg")
        os.rename( root_wd + "/" + images + ".txt", root_wd + "/img_anno/" + images + ".txt")


files_updated = os.listdir(root_wd)

for all_files in files_updated:
    if '.jpg' in all_files:
        os.rename( root_wd + "/" + all_files, root_wd + "/img/" + all_files)
    if '.txt' in all_files:
        os.rename( root_wd + "/" + all_files, root_wd + "/txt/" + all_files)
end_time = datetime.now() - start_time