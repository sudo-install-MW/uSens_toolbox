# This script will perform the following
# 1. create individual folder for each gesture and put image and annotations in it
# 2. create a scrape folder which has rogue annotations
# 3. performs sanity in all the annotations
# HOW TO USE : copy the script in the main directory where .txt exists
# and run the script ASAT

import os

# path = "/home/mahesh/Universe/data_sets/12_gesture_master/img_anno"

path = '/home/mahesh/All'

cur_w_dir = path # enter path if operating on diff directory
files = os.listdir(cur_w_dir)

# Label class dictionary
class_dic = {'0': 'body', '1': 'head', '2':'openPalm', '3':'thumbsUp', '4':'beg', '5':'fingerHeart', '6':'okay', '7':'yeah', '8':'gun', '9':'pointUp', '10':'handTogether',
            '11':'honor', '12':'heart'}

# count dictionary to get total data information
count_dict = dict()
for keys, label in class_dic.items():
    count_dict[label] = 0
print(count_dict)

count_dict['others'] = 0


for file in files:
    if file[len(file)- 4:] == '.txt':
        with open(os.path.join(path, file), 'r') as f:
            f_line = f.readlines()
            #print(f_line)
            for lines in f_line:
                if lines[0] not in class_dic.keys() or len(lines.split()) > 5:
                    print("the label \"{}\" does not meet the standard in the file \"{}\"".format(lines[:len(lines)-1], file))
                    count_dict['others'] += 1
                    os.remove(os.path.join(path,file))
                    #for elements in lines:
                        #print(elements)
                    continue
                elif lines[0] == '0':
                    #print(lines[0])
                    count_dict['body'] += 1
                elif lines[0] == '1':
                    #print(lines[0])
                    count_dict['head'] += 1
                elif lines[0] == '2':
                    #print(lines[0])
                    count_dict['openPalm'] += 1
                elif lines[0] == '3':
                    #print(lines[0])
                    count_dict['thumbsUp'] += 1
                elif lines[0] == '4':
                    #print(lines[0])
                    count_dict['beg'] += 1
                elif lines[0] == '5':
                    #print(lines[0])
                    count_dict['fingerHeart'] += 1
                elif lines[0] == '6':
                    #print(lines[0])
                    count_dict['okay'] += 1
                elif lines[0] == '7':
                    #print(lines[0])
                    count_dict['yeah'] += 1
                elif lines[0] == '8':
                    #print(lines[0])
                    count_dict['gun'] += 1
                elif lines[0] == '9':
                    #print(lines[0])
                    count_dict['pointUp'] += 1
                elif lines[0] == '10':
                    #print(lines[0])
                    count_dict['handTogether'] += 1
                elif lines[0] == '11':
                    #print(lines[0])
                    count_dict['honor'] += 1
                elif lines[0] == '12':
                    #print(lines[0])
                    count_dict['heart'] += 1

for keys, label in count_dict.items():
    print("There are {} objects annotated on class {}".format(label, keys))

