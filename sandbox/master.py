import cv2
import numpy as np
from os import listdir


class FILE_OPERATION():
    '''

    '''
    def read_img(img_dir):
        '''
        :param img_dir: directory link containing image
        :return: img_dict
        img_dict -> {key:"img_name", value:[[img], [bb_coordinates]]}
        '''

        class_dic = {'0': 'body', '1': 'head', '2': 'openPalm', '3': 'thumbsUp', '4': 'beg', '5': 'fingerHeart',
                     '6': 'okay', '7': 'yeah', '8': 'gun', '9': 'pointUp', '10': 'handTogether',
                     '11': 'honor', '12': 'heart'}

        img_dict = {}
        for images in img_dir:
            if images[-4:] == '.jpg' or images[-4:] == '.png':
                textName = images.replace('.jpg', '.txt')
                textName = textName.replace('.png', '.txt')
                boundingBox = open(textName, 'r')
                imgData = cv2.imread(images)
                number_line = boundingBox.readline()
                boundingList = []
                while number_line:
                    arrayNumber = number_line.split()
                    gesture, xcord, ycord, width, height = (float(x) for x in number_line.split())
                    if number_line == "":
                        break
                    number_line = boundingBox.readline()
                    boundingList.append([int(gesture), float(xcord), float(ycord), float(width), float(height)])
                    img_dict[images] = [imgData, boundingList]
                boundingBox.close()
                print(img_dict[images])

    def save_img(p_img_dict, s_path):
        '''
        :param p_img_dict: p_img_dict, s_path

         p_img_dict -> {key:"img_name", value:[[img], [img_class]]}
         s_path -> path to create 12 gesture directory and save the images correspondingly

        :return: none
        save the image to corresponding 12 gesture directory
        '''

        def make_if_not_exist(dir):
            if not os.path.exists(dir):
                os.makedirs(dir)

        for key, value in p_img_dict.items():
            # destructure the value
            img, img_class, *_ = value

            # create the new path
            new_dir = os.path.join(s_path, img_class)

            make_if_not_exist(new_dir)
            image_path = os.path.join(new_dir, key)

            cv2.imwrite(image_path, img)


class CV_OPERATION():
    '''
    doc string
    '''
    crop_scale = 20

    def cvt_anno(self, coordinates, img_dims):
        '''
        :param coordinates: yolo_mark format coordinates [cat, center_x, center_y, x, y]
        :return: coordinates for slicing image in numpy
        '''
        width = img_dims[1]
        height = img_dims[0]

        cat, center_x, center_y, x, y = coordinates
        dx = float(x) / 2.0
        dy = float(y) / 2.0

        xmin = float(center_x) - dx
        ymin = float(center_y) - dy

        xmax = float(center_x) + dx
        ymax = float(center_y) + dy

        xmin = xmin if xmin > 0 else 0.0
        ymin = ymin if ymin > 0 else 0.0
        xmax = xmax if xmax < 1.0 else 1.0
        ymax = ymax if ymax < 1.0 else 1.0

        return [xmin * width, ymin * height, xmax * width, ymax * height], cat


    def draw_box(self, img, coordinates):
        '''

        :param img:
        :param coordinates:
        :return:
        '''
        pt1 = (int(coordinates[0]), int(coordinates[1]))
        pt2 = (int(coordinates[2]), int(coordinates[3]))
        cv2.rectangle(img, pt1, pt2,(0,255,0),2)


    def crop_img(self, img, img_dims, coordinates, crop_pixel):
        '''
        :param img:
        :param coordinates:
        :return:
        '''
        '''
        if coordinates[0] != 0 & coordinates[0] > crop_pixel:
            coordinates[0] = coordinates[0] - crop_pixel

        if coordinates[1] != 0 & coordinates[1] > crop_pixel:
            coordinates[1] = coordinates[1] - crop_pixel

        if coordinates[2] < img_dims[0]:
            coordinates[2] = coordinates[2] + crop_pixel

        if coordinates[3] < img_dims[1]:
            coordinates[3] = coordinates[3] + crop_pixel
        '''

        img = img[coordinates[1]:coordinates[3], coordinates[0]:coordinates[2]]

        return img


    def extract_img(self, img_dict):
        '''
        :param img_dict: img_dict
        img_dict -> {key:"img_name", value:[[img], [[cls, x_c, y_c, w, h]....[cls, x_c, y_c, w, h]]}

        :return: p_img_dict
        p_img_dict -> {key:"img_name", value:[[[img], [img_class]]....[[img], [img_class]]]}
        '''
        p_img_dict = dict()
        c_img = []

        for keys, value in img_dict.items():
            #save cropped image inside the dict
            img_dims = np.shape(value[0])
            img = value[0]


            for bb in value[1]:
                img_buff = []
                # get bb in np format
                np_coord, img_cls = self.cvt_anno(bb, img_dims)

                # draw boxes around the gesture
                self.draw_box(img, np_coord)

                # crop the image
                img_cropped = self.crop_img(img, img_dims, np_coord, self.crop_scale)
                img_buff.append(img_cropped, img_cls)
                c_img.append(img_buff)

            p_img_dict[keys] = c_img

        return p_img_dict




