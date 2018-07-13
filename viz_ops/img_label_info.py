# This script will perform the following
# 1. create individual folder for each gesture and put image and annotations in it
# 2. create a scrape folder which has rogue annotations
# 3. performs sanity in all the annotations
# HOW TO USE : copy the script in the main directory where .txt exists
# and run the script ASAT

# Author : Maheshwaran Umapathy
# Tested and Debugged on : 11th July 2018 21:23

import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

path = '/media/usens/My Passport/dataset/RGBHT0630/image_aug_0630/img_anno'

cur_w_dir = path
files = os.listdir(cur_w_dir)

# Label class dictionary
class_dic = {'0':'palm', '1':'thumbup', '2':'beg', '3':'fheart', '4':'okay', '5':'yeah', '6':'gun', '7':'pointup', '8':'hand2gr', '9':'honor', '10':'heart'}
# count dictionary to get total data information
count_dict = dict()

for keys, label in class_dic.items():
    count_dict[label] = 0
print(count_dict)

count_dict['others'] = 0
file_count = 0

start_time = datetime.now()
for file in files:
    if file[len(file) - 4:] == '.txt':
        file_count += 1
        with open(os.path.join(path, file), 'r') as f:
            #  create a list for every line
            f_line = f.readlines()
            for lines in f_line:
                line_words = lines.split()
                if line_words[0] not in class_dic.keys() or len(line_words) > 5:
                    print("the label \"{}\" does not meet standards, file \"{}\"".format(lines[:len(lines)-1], file))
                    count_dict['others'] += 1
                    #  os.remove(os.path.join(path,file))
                    #  for elements in lines:
                    #  print(elements)
                    continue
                elif line_words[0] == '0':
                    count_dict['palm'] += 1
                elif line_words[0] == '1':
                    count_dict['thumbup'] += 1
                elif line_words[0] == '2':
                    count_dict['beg'] += 1
                elif line_words[0] == '3':
                    count_dict['fheart'] += 1
                elif line_words[0] == '4':
                    count_dict['okay'] += 1
                elif line_words[0] == '5':
                    count_dict['yeah'] += 1
                elif line_words[0] == '6':
                    count_dict['gun'] += 1
                elif line_words[0] == '7':
                    count_dict['pointup'] += 1
                elif line_words[0] == '8':
                    count_dict['hand2gr'] += 1
                elif line_words[0] == '9':
                    count_dict['honor'] += 1
                elif line_words[0] == '10':
                    count_dict['heart'] += 1
time_elapsed = datetime.now() - start_time
for keys, label in count_dict.items():
    print("There are {} objects annotated on class {}".format(label, keys))
print("Time consumed for reading {} files is {}".format(file_count, time_elapsed))

# TODO START
# Fixing random state for reproducibility
#np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
feed_label = []

for label in class_dic.values():
    feed_label.append(label)

labels = tuple(feed_label)
y_pos = np.arange(len(labels))

img_count = []
for value in count_dict.values():
    img_count.append(value)

performance = img_count

ax.barh(y_pos, performance, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(labels)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Images')
ax.set_title('Image distribution')

plt.show()
# TODO END
