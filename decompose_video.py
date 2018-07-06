import argparse
import datetime
import os
import cv2
import sys
import skvideo.io


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parser = argparse.ArgumentParser()
    parser.add_argument('--videoes_dir',
                        type=str,
                        default=dir_path+'/videos/',
                        help='Path to folders with videos'
                        )

    # parser = argparse.ArgumentParser()
    parser.add_argument('--photoes_dir',
                        type=str,
                        default=dir_path+'/objects/',
                        help='Path to folders with photoes'
                        )
    FLAGS, unparsed = parser.parse_known_args()

    for directory in os.listdir(FLAGS.videoes_dir):
        # print(directory)
        if (directory == '.DS_Store'): continue
        product_video_dir = FLAGS.videoes_dir + directory
        product_objects_dir = FLAGS.photoes_dir + directory

        if not os.path.exists(product_objects_dir):
            os.makedirs(product_objects_dir)

        for product_video in os.listdir(product_video_dir):
            tmp = './' + '/'.join(product_video_dir.split('/')[5:]) + '/'
            vidcap = cv2.VideoCapture(tmp + product_video)
            success, image = vidcap.read()
            count = 0
            success = True
            while success:
                cv2.imwrite(product_objects_dir + "/frame%d-%s.jpg" % (count, datetime.datetime.now().second), image)  # save frame as JPEG file
                success, image = vidcap.read()
                count += 1