import cv2
import os
from datetime import datetime

path = '/media/usens/My Passport/dataset/RGBHT0630/image_aug_0630'
images = os.listdir(path)
img_list = []
img_zero = []
count = 0

start_time = datetime.now()
for image in images:
    if image[len(image)-4:] == '.jpg':
        img_list.append(image)


for image in img_list:
    img = cv2.imread(os.path.join(path, image))
    if img is None:
        print("zero size image found ", image)
        img_zero.append(image)
        print(img_zero)
    count += 1
    if count % 1000 == 0:
        print(count)

time_elapsed = datetime.now() - start_time
print("Time taken to run the program ", time_elapsed)


