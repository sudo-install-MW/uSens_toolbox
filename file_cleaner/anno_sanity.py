# This script will perform the following
# 1. create individual folder for each gesture and put image and annotations in it
# 2. create a scrape folder which has rogue annotations
# 3. performs sanity in all the annotations
# HOW TO USE : copy the script in the main directory where .txt exists
# and run the script
import os

class dir_cleaner():
    '''

    '''
    class_dic = {'0': 'body', '1': 'head', '2': 'openPalm', '3': 'thumbsUp', '4': 'beg', '5': 'fingerHeart',
                 '6': 'okay', '7': 'yeah', '8': 'gun', '9': 'pointUp', '10': 'handTogether',
                 '11': 'honor', '12': 'heart'}

    def anno_sanity(self, txt_file_path, scrape_path):
        '''
        :param txt_file_path: path to txt file
        :param scrape_path: path to scrape where rogue annotations are dumped
        :return: None
        '''

        with open(txt_file_path, 'r') as f:
            f_line = f.readlines()
            for lines in f_line:
                if lines[0] not in self.class_dic.keys() or len(lines.split()) > 5:
                    print("the {} file is moved to scrape folder and it is found to be rogue")
                    os.rename(txt_file_path, scrape_path)

    def img_bucketer(self, raw_path, output_path):
        '''
        :param raw_path:
        :return:
        '''
        root_wd = raw_path

        print("\ncurrent working directory is :", root_wd)
        root_files = os.listdir(root_wd)

        # create the folder for image and text transfer
        for keys, value in self.class_dic.items():
            if value not in root_files:
                os.mkdir(raw_path + value)

        # create a dictionary txt_dict for all txt files in the root directory
        for elements in root_files:
            if '.txt' in elements:
                txt_dict[elements[:len(elements) - 4]] = elements
            elif '.jpg' in elements:
                jpg_list.append(elements[:len(elements) - 4])

        # print(txt_dict)

        for images in jpg_list:
            # check if corrensponding entry is in txt_dict
            if images in txt_dict:
                print("found image {} with associated txt".format(images))

                # TODO START
                # move the image and annotation to corresponding folder
                os.rename(os.path.join(root_wd, images + '.jpg'), os.path.join(output_path, images + ".jpg"))
                os.rename(os.path.join(root_wd, images + '.txt'), os.path.join(output_path, images + ".jpg"))
                # TODO END


        # after bucketing files

        files_updated = os.listdir(root_wd)

        for all_files in files_updated:
            if '.jpg' in all_files:
                os.rename(root_wd + "/" + all_files, root_wd + "/img/" + all_files)
            if '.txt' in all_files:
                os.rename(root_wd + "/" + all_files, root_wd + "/txt/" + all_files)


