import sys
sys.path.append("/home/usens/universe/detector/include/models/research/slim")
sys.path.append("/home/usens/universe/detector/include/models/research")
import os
import tensorflow as tf
from tf_helper import create_tf_example
from datetime import datetime


flags = tf.app.flags
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
FLAGS = flags.FLAGS


def main(_):
    writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
    # fill in with directory info if working from different directory
    cur_w_dir = '/media/usens/My Passport/dataset/11_gesture/11_gesture_1080_1920/'  # ENTER PATH HERE  ## os.getcwd()
    cur_w_dir_files = os.listdir(cur_w_dir)

    # create empty list to store img and txt file info
    img_list = []
    ano_list = []

    # append images in img_list and txt to ano_list
    for files in cur_w_dir_files:
      if files[len(files) - 4:] == '.jpg':
          img_list.append(files[:len(files) - 4])
      #elif files[len(files) - 4:] == '.txt':
          #ano_list.append(files)

    count = 0

    for data_and_label_info in img_list:
        if count % 100 == 0:
            print("Created tf_record for {} images out of {} images".format(count, len(img_list)))
        tf_example = create_tf_example(data_and_label_info)
        writer.write(tf_example.SerializeToString())
        count += 1
    writer.close()

if __name__ == '__main__':
    start = datetime.now()
    tf.app.run()
    end = datetime.now() - start
    print("total time taken to convert all images to tf record is :", end)
