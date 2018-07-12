import cv2
import os

path = '/home/mahesh/Universe/data_sets/12_gesture_master/img_anno'
images = os.listdir(path)
img_list = []
img_zero = []
for image in images:
    if image[len(image)-4:] == '.jpg':
        img_list.append(image)


for image in img_list:
    print(image)
    img = cv2.imread(os.path.join('/home/mahesh/Universe/data_sets/12_gesture_master/img_anno', image))
    if img is None:
        print("zero size image found ", image)
        img_zero.append(image)
        print(img_zero)

    #print(img)


