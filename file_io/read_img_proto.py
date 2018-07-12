import cv2
import os

def read_img(img_dir):
    '''
    :param img_dir: directory link containing image
    :return: img_dict
    img_dict -> {key:"img_name", value:[[img], [bb_coordinates]]}
    '''

    cwd_files = os.listdir(img_dir)
    img_list = []
    txt_list = []
    img_dict = dict()

    for files in cwd_files:
        if files[-4:] == '.txt':
            txt_list.append(files)
    txt_set = set(txt_list)

    for files in cwd_files:
        if files[-4:] == '.jpg' or files[-4:] == '.png':
            if files[:len(files) - 4] + '.txt' in txt_set:
                img_list.append(files)

    for images in img_list:

        textName = images.replace('.jpg', '.txt')
        textName = textName.replace('.png', '.txt')

        boundingBox = open(os.path.join(img_dir, textName), 'r')
        number_line = boundingBox.readline()
        boundingList = []

        arrayNumber = number_line.split()
        # if len(arrayNumber) > 6:
        #     os.remove(os.path.join(img_dir, images))
        #     #os.remove(os.path.join(img_dir, images[:len(files) - 4] + '.txt'))
        #     continue

        imgData = cv2.imread(os.path.join(img_dir,images))


        while number_line:

            #print(images)
            #print(number_line)
            gesture, xcord, ycord, width, height = (float(x) for x in number_line.split())
            #print("read annotations success")
            if number_line == "":
                break
            number_line = boundingBox.readline()
            boundingList.append([int(gesture),float(xcord),float(ycord),float(width),float(height)])
            img_dict[images] = [imgData,boundingList]
        boundingBox.close()
        #print(img_dict[images])

    #print(img_dict)
    return img_dict

a = read_img('/home/mahesh/All/img_anno')
print(a)