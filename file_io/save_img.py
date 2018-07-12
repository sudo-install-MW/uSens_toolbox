import os
import cv2

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
        #destructure the value
        img, img_class, *_ = value

        #create the new path
        new_dir = os.path.join(s_path, img_class)

        make_if_not_exist(new_dir)
        image_path = os.path.join(new_dir, key)

        cv2.imwrite(image_path, img)