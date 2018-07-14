import tensorflow as tf
import cv2
from object_detection.utils import dataset_util

# export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim


label_dict = {'0': 'palm', '10': 'heart'}


def create_tf_example(data_name):
    """
    function to prep the input data to tf_record format

    args   : label_and_data_info
    return : tf_label_and_data
    """
    img_file = '/media/usens/My Passport/dataset/RGBHT0630/clean_images/palm_heart/' + data_name + '.jpg'
    txt_file = '/media/usens/My Passport/dataset/RGBHT0630/clean_images/palm_heart/' + data_name + '.txt'

    with tf.gfile.GFile(img_file, 'rb') as fid:
        encoded_image = fid.read()

    img = cv2.imread(img_file)
    height, width, channels = img.shape
    filename = data_name.encode()  # Filename of the image. Empty if image is not from file

    image_format = 'jpeg'.encode()  # b'jpeg' or b'png'

    xmins = []  # List of normalized left x coordinates in bounding box (1 per box)
    xmaxs = []  # List of normalized right x coordinates in bounding box (1 per box)

    ymins = []  # List of normalized top y coordinates in bounding box (1 per box)
    ymaxs = []  # List of normalized bottom y coordinates in bounding box (1 per box)

    classes_text = []  # List of string class name of bounding box (1 per box)
    classes = []  # List of integer class id of bounding box (1 per box)

    with open(txt_file, 'r') as f:
        lines = f.readlines()

        for line in lines:
            cat, center_x, center_y, x, y = line.split()
            # print(cat)
            # print(cat == '0')
            # print(cat, 2)
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

            xmins.append(xmin)
            xmaxs.append(xmax)
            ymins.append(ymin)
            ymaxs.append(ymax)

            classes_text.append(label_dict[cat].encode())
            # open palm has cat 0 and heart has cat 10 so make changes accordingly
            classes.append(int(cat) + 1 if cat == '0' else int(cat) - 8)
            print(classes)
    # TODO END

    tf_label_and_data = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_image),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_label_and_data
