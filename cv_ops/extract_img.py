class CV_OPERATION():
    '''
    class to wrap all CV operation
    cvt_anno :
    draw_box :
    crop_img :
    extract_img :
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