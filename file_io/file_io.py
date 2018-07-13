# Author : Maheshwaran Umapathy
# Tested and Debugged on : 11th July 2018 21:23

import os


class FileOps:
    """

    """
    class_dic = {'0': 'palm', '1': 'thumbup', '2': 'beg', '3': 'fheart', '4': 'okay', '5': 'yeah', '6': 'gun',
                 '7': 'pointup', '8': 'hand2gr', '9': 'honor', '10': 'heart'}

    def read_img(self, img_dir):
        '''
        :param img_dir: directory link containing image
        :return: img_dict
        img_dict -> {key:"img_name", value:[[bb_coordinates_1]..[bb_coordinates_n]}
        STATUS : checked and verified
        '''
        img_dict = dict()
        cwd_files = os.listdir(img_dir)

        for files in cwd_files:
            if files[len(files) - 4:] == '.jpg':
                with open(os.path.join(img_dir, files[:len(files) - 4] + '.txt'), 'r') as f:
                    img_label = f.readlines()
                    img_dict[files] = list(img_label)

        return img_dict

    def anno_sanity(self, img_dir):
        """
        :param img_dir: path to txt file
        :return: None
        STATUS : checked and verified
        """
        txt_dict = dict()

        files = os.listdir(img_dir)
        if 'scrape' not in files:
            os.mkdir(os.path.join(img_dir, 'scrape'))

        #####################################################################
        # add txt files in dictionary and also check
        # 1. if dual entry is present move it to scrape
        # 2. has format [int, float, float, float, float]
        for file in files:
            if file[len(file) - 4:] == '.txt':
                with open(os.path.join(img_dir, file), 'r') as f:
                    # to check format[int, float, float, float, float]
                    f_line = f.readlines()
                    for lines in f_line:
                        line_word = lines.split()
                        if line_word[0] not in self.class_dic.keys() or len(line_word) != 5:
                            print("the \"{}\" file is moved to scrape folder and it is found to be rogue".format(file))
                            # move the txt file to scrape
                            os.rename(os.path.join(img_dir, file), os.path.join(img_dir, os.path.join('scrape', file)))
                            # move the img file to scrape
                            os.rename(os.path.join(img_dir, file[:len(file) - 4] + '.jpg'), os.path.join(img_dir, os.path.join('scrape', file[:len(file) - 4] + '.jpg')))

                # if dual entry is present
                if file in txt_dict:
                    # put the txt file in scrape
                    os.rename(os.path.join(img_dir, file), os.path.join(img_dir, os.path.join('scrape', file)))
                    # put the img file in scrape
                    os.rename(os.path.join(img_dir, file[:len(file) - 4] + '.jpg'),
                              os.path.join(img_dir, os.path.join('scrape', file[:len(file) - 4] + '.jpg')))
                    # delete entry from dictionary
                    del txt_dict[file]
                else:
                    txt_dict[file] = 0

        print(txt_dict)


    # def img_bucketer(self, raw_path, output_path):
    #     '''
    #     :param raw_path:
    #     :return:
    #     STATUS : DEBUGGING
    #     '''
    #     root_wd = raw_path
    #
    #     print("\ncurrent working directory is :", root_wd)
    #     root_files = os.listdir(root_wd)
    #
    #     # create the folder for image and text transfer
    #     for keys, value in self.class_dic.items():
    #         if value not in root_files:
    #             os.mkdir(raw_path + value)
    #
    #     # create a dictionary txt_dict for all txt files in the root directory
    #     for elements in root_files:
    #         if '.txt' in elements:
    #             txt_dict[elements[:len(elements) - 4]] = elements
    #         elif '.jpg' in elements:
    #             jpg_list.append(elements[:len(elements) - 4])
    #
    #     # print(txt_dict)
    #
    #     for images in jpg_list:
    #         # check if corrensponding entry is in txt_dict
    #         if images in txt_dict:
    #             print("found image {} with associated txt".format(images))
    #
    #             # TODO START
    #             # move the image and annotation to corresponding folder
    #             os.rename(os.path.join(root_wd, images + '.jpg'), os.path.join(output_path, images + ".jpg"))
    #             os.rename(os.path.join(root_wd, images + '.txt'), os.path.join(output_path, images + ".jpg"))
    #             # TODO END
    #
    #     # after bucketing files
    #     files_updated = os.listdir(root_wd)
    #
    #     for all_files in files_updated:
    #         if '.jpg' in all_files:
    #             os.rename(root_wd + "/" + all_files, root_wd + "/img/" + all_files)
    #         if '.txt' in all_files:
    #             os.rename(root_wd + "/" + all_files, root_wd + "/txt/" + all_files)

a = FileOps()
a.anno_sanity('/media/usens/My Passport/dataset/11_gesture_master/img_anno')