import cv2
import os
from datetime import datetime

path = '/media/usens/My Passport/dataset/RGBHT0630/image_aug_0630/img_anno'
images = os.listdir(path)

if 'scrape' not in images:
    os.mkdir(os.path.join(path, 'scrape'))

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
    if count % 100 == 0:
        print("Read and verified {} images".format(count))

print("moving all zero byte images to scrape")
if len(img_zero) == 0:
    print("No zero byte image found")
for images in img_zero:
    os.rename(os.path.join(path, images),os.path.join(path, 'scrape'))

time_elapsed = datetime.now() - start_time
print("Time taken to run the program ", time_elapsed)
